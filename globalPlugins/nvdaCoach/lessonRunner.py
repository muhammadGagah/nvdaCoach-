# NVDA Coach - Lesson Runner
# Delivers lessons step-by-step through the CoachWindow.
# There is NO global gesture interception — the student tries each command
# freely on their own, then returns to the CoachWindow and presses Enter
# (or clicks Next Step) to confirm and move on.

import os
import wx
import ui
import nvwave
import config
from logHandler import log

_SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "sounds")


def _playSound(filename):
	"""Play a WAV file from the sounds/ folder, gated on the playSounds setting."""
	if config.conf["nvdaCoach"]["playSounds"]:
		path = os.path.join(_SOUNDS_DIR, filename)
		nvwave.playWaveFile(path)


class LessonRunner:
	"""Runs an interactive lesson, advancing through steps when the student confirms."""

	# Show full controls reminder only on first lesson per NVDA session.
	_controlsIntroShown = False

	def __init__(self, progressTracker):
		self._progressTracker = progressTracker
		self.isActive = False
		self._categoryId = None
		self._categoryTitle = ""
		self._lesson = None
		self._stepIndex = 0
		self._pendingTimer = None
		self.coachWindow = None  # Set by GlobalPlugin after creation.
		self.onOpenPracticePage = None  # Callback: fired when a step with openPracticePageAfter is advanced past.
		self.onOpenPracticeFrame = None  # Callback: fired when a step with openPracticeFrameAfter is advanced past.
		self.onChapterComplete = None   # Callback: fired when a lesson with chapterComplete: true finishes.
		self._hintIndex = 0  # Tracks which hint in a hints array to show next.

	# ------------------------------------------------------------------
	# Public API
	# ------------------------------------------------------------------

	def startLesson(self, categoryId, lesson, categoryTitle=""):
		"""Begin running a lesson."""
		if self.isActive:
			return
		self._categoryId = categoryId
		self._categoryTitle = categoryTitle
		self._lesson = lesson
		self._stepIndex = 0
		self.isActive = True

		# Lesson start sound.
		_playSound("lesson_start.wav")

		lessonTitle = self._lesson.get("title", "Lesson")
		if LessonRunner._controlsIntroShown:
			introMsg = f"Starting lesson: {lessonTitle}."
		else:
			introMsg = (
				f"Starting lesson: {lessonTitle}. "
				"Press Enter or the Next Step button to advance. "
				"F1 repeats the instruction, F2 gives a hint, "
				"Escape stops the lesson."
			)
			LessonRunner._controlsIntroShown = True

		wx.CallLater(600, ui.message, introMsg)
		wx.CallLater(600 + self._estimateReadTime(introMsg), self._speakCurrentStep)

	def stopLesson(self, announce=True):
		"""Stop the current lesson."""
		if not self.isActive:
			return
		self._cancelPendingTimer()
		self.isActive = False
		if announce:
			_playSound("lesson_stop.wav")
			ui.message(
				"Lesson stopped. "
				"Press NVDA+Shift+C to choose another lesson, "
				"or Ctrl+R to restart this one."
			)
		if self.coachWindow:
			self.coachWindow.showIdle("Lesson stopped.")

	def cleanup(self):
		"""Called when the add-on terminates."""
		self.stopLesson(announce=False)

	# ------------------------------------------------------------------
	# Actions called by CoachWindow keyboard handler and buttons
	# ------------------------------------------------------------------

	def advanceCurrentStep(self):
		"""Move to the next step. Called by Enter key or Next Step button."""
		if not self.isActive:
			return
		self._cancelPendingTimer()
		_playSound("step_advance.wav")
		self._advanceStep()

	def repeatInstruction(self):
		"""Re-read the current step instruction. Called by F1."""
		if not self.isActive:
			return
		step = self._currentStep()
		if step:
			ui.message(step.get("instruction", ""))

	def speakHint(self):
		"""Read the hint for the current step. Called by F2. Cycles through hints array."""
		if not self.isActive:
			return
		step = self._currentStep()
		if not step:
			return
		hints = step.get("hints")
		if hints and isinstance(hints, list) and len(hints) > 0:
			hint = hints[self._hintIndex % len(hints)]
			self._hintIndex += 1
			count_label = f" {(self._hintIndex - 1) % len(hints) + 1} of {len(hints)}" if len(hints) > 1 else ""
			_playSound("hint.wav")
			ui.message(f"Hint{count_label}: {hint}")
		else:
			# Fall back to legacy single hint string.
			hint = step.get("hint", "No additional hint is available for this step.")
			_playSound("hint.wav")
			ui.message(f"Hint: {hint}")

	def skipStep(self):
		"""Skip the current step without marking it correct. Called by F3."""
		if not self.isActive:
			return
		ui.message("Step skipped.")
		self._advanceStep()

	# ------------------------------------------------------------------
	# Step navigation
	# ------------------------------------------------------------------

	def _currentStep(self):
		"""Return the current step dict, or None if out of bounds."""
		steps = self._lesson.get("steps", [])
		if 0 <= self._stepIndex < len(steps):
			return steps[self._stepIndex]
		return None

	def _speakCurrentStep(self):
		"""Announce the instruction for the current step and update CoachWindow."""
		if not self.isActive:
			return
		self._hintIndex = 0  # Reset hint cycling whenever a new step begins.
		step = self._currentStep()
		if step is None:
			self._completeLesson()
			return

		instruction = step.get("instruction", "")
		stepType = step.get("type", "info")
		stepNum = self._stepIndex + 1
		totalSteps = len(self._lesson.get("steps", []))
		prefix = f"Step {stepNum} of {totalSteps}. "

		# Gesture steps tell the student to try the key themselves, then confirm.
		if stepType == "gesture":
			advance_cue = (
				"\n\nTry it now. When you are ready to continue, "
				"press Enter or click Next Step."
			)
			displayInstruction = instruction + advance_cue
		else:
			displayInstruction = instruction

		# If the step defines inline practice text, append it to the display.
		# The student can arrow down into it directly within the CoachWindow.
		practiceText = step.get("practiceText", "")
		if practiceText:
			displayInstruction += (
				"\n\n"
				"PRACTICE AREA \u2014 NAVIGATE WITH ARROW KEYS:\n\n"
				+ practiceText
			)

		if self.coachWindow:
			self.coachWindow.updateDisplay(
				self._categoryTitle,
				self._lesson.get("title", ""),
				self._stepIndex,
				totalSteps,
				displayInstruction,
			)

		spokenMsg = prefix + instruction
		if stepType == "gesture":
			spokenMsg += " Try it now. When you are ready to continue, press Enter or click Next Step."
		ui.message(spokenMsg)

	def _advanceStep(self):
		"""Move to the next step, or complete the lesson if done."""
		if not self.isActive:
			return
		self._pendingTimer = None
		prevStep = self._currentStep()  # Capture before incrementing.
		self._stepIndex += 1
		steps = self._lesson.get("steps", [])
		if self._stepIndex >= len(steps):
			self._completeLesson()
		else:
			if prevStep and prevStep.get("openPracticePageAfter") and self.onOpenPracticePage:
				wx.CallAfter(self.onOpenPracticePage)
			if prevStep and prevStep.get("openPracticeFrameAfter") and self.onOpenPracticeFrame:
				wx.CallAfter(self.onOpenPracticeFrame)
			self._speakCurrentStep()

	def _completeLesson(self):
		"""Handle lesson completion."""
		self.isActive = False
		self._cancelPendingTimer()

		totalSteps = len(self._lesson.get("steps", []))
		self._progressTracker.markLessonComplete(
			self._categoryId,
			self._lesson.get("id", "unknown"),
			{},
			totalSteps,
		)

		# Lesson complete sound.
		_playSound("lesson_complete.wav")

		lessonTitle = self._lesson.get("title", "Lesson")
		msg = (
			f"Lesson complete: {lessonTitle}! Well done. "
			"Press NVDA+Shift+C to open the lesson picker and choose your next lesson "
			"or continue to the next chapter. "
			"Ctrl+N moves to the next lesson in this category, "
			"or Ctrl+R repeats this one."
		)
		wx.CallLater(600, ui.message, msg)
		if self.coachWindow:
			wx.CallLater(
				600,
				self.coachWindow.showIdle,
				f"Lesson complete: {lessonTitle}!\n\n"
				"Well done.\n\n"
				"--- WHAT TO DO NEXT ---\n"
				"  Press NVDA+Shift+C to open the lesson picker.\n"
				"  Choose the next lesson in this chapter, or start the next chapter.\n\n"
				"--- STAY IN THIS CHAPTER ---\n"
				"  Ctrl+N  \u2014  Next lesson in this category.\n"
				"  Ctrl+R  \u2014  Repeat this lesson.\n"
				"  Ctrl+B  \u2014  Go back to the previous lesson."
			)
		# If this lesson marks the end of a chapter, fire the chapter-complete callback
		# after the normal completion screen has been shown.
		if self._lesson.get("chapterComplete") and self.onChapterComplete:
			wx.CallLater(3000, self.onChapterComplete)

	# ------------------------------------------------------------------
	# Utility helpers
	# ------------------------------------------------------------------

	def _cancelPendingTimer(self):
		"""Cancel any pending wx.CallLater timer."""
		if self._pendingTimer is not None:
			try:
				self._pendingTimer.Stop()
			except Exception:
				pass
			self._pendingTimer = None

	def _estimateReadTime(self, text):
		"""Estimate milliseconds needed to read a message at typical speech rate."""
		chars = len(text)
		return max(1500, min(8000, int(chars / 15 * 1000)))
