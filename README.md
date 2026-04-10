# NVDA Coach

**Interactive screen reader training built right into NVDA.**

NVDA Coach is a free add-on for the [NVDA screen reader](https://nvaccess.org) that teaches commands through guided, step-by-step practice sessions — from inside NVDA itself. No videos, no PDFs, no switching between windows. Press one key combination and the Coach walks you through what to do and why, one step at a time.

**Current version:** 1.5
**Author:** Tony Gebhard, Assistive Technology Instructor
**License:** GPL v2

---

## Download and Install

**[Download NVDA Coach v1.5](https://github.com/tonygeb23/nvdaCoach-/releases/download/v1.5/nvdaCoach-1.5.nvda-addon)**

1. Download the `.nvda-addon` file above
2. Open the file — NVDA handles the installation automatically and asks you to confirm
3. Press **NVDA+Shift+C** — the Coach window opens and you're ready to begin

NVDA 2024.1 or later required. Available in the NVDA Add-on Store (Tools → Add-on Store).

---

## What's New in v1.5

- **Personalization (F7):** Press F7 to open a profile dialog and enter your name, instructor's name, and training program. NVDA Coach uses these throughout: a one-time greeting when you start your first lesson ("Hello, Tony! Your instructor today is Sarah."), personalized lesson completions ("Well done, Tony!"), and a named congratulations screen at the end of the course.
- **F4–F7 quick keys:** Available at all times in the Coach window and the lesson picker. F4 opens the NVDA Coach help page (press twice to confirm). F5 opens a feedback email to the developer (press twice to confirm). F6 immediately toggles lesson sounds on or off and announces the new state. F7 opens the personalization profile dialog.
- **Certificate of Completion:** Finishing all lessons in the Customizing NVDA chapter triggers a heartfelt congratulations screen with a button to export your Certificate of Completion. The certificate is an HTML file saved automatically to your Downloads folder and opened in your browser — ready to print or save as PDF. Includes your name, date, instructor, and training program if set.
- **Chapter reordering:** "Your Keyboard" is now Chapter 2 — immediately after Getting Started — so students get physical keyboard orientation before command learning begins. "Customizing NVDA" is now the final chapter (Chapter 6), serving as the natural course conclusion that triggers the certificate.
- **Heartfelt final completion screen:** Completing Chapter 6 replaces the standard lesson-complete screen with a dedicated congratulations message listing all six chapters mastered and step-by-step instructions for printing or saving the certificate.

## What's New in v1.4

- **6 new lessons** across all chapters (now 41 lessons, 6 chapters): Understanding Your Keyboard, Switching Windows with Alt+Tab, Navigate by Paragraph and Page, Navigate Tables, and a brand-new Chapter 6 (Your Keyboard) with 3 lessons on modifier keys, function keys, and NVDA layout selection.
- **Bug fix — practice frame button feedback:** Button now correctly says "You activated the button" instead of "with Enter" when Space is used to activate it.
- **Object Navigation — new terminology:** Parent/child language replaced with levels/pyramid metaphor ("one level above/below") throughout. Maximize window tip added. NVDA+Tab distinction clarified.
- **Browse Mode — table navigation:** New lesson covers Ctrl+Alt+Arrow keys for navigating table cells in browse mode.
- **Browse Mode — Toggle Single-Letter Navigation lesson removed:** Per instructor feedback — students discover this through practice.
- **Focus Mode enhanced:** Added explicit statement that focus mode "puts the cursor in the edit box."
- **Report highlighted text:** New step in the selection lesson — NVDA+Shift+Up Arrow (desktop) / NVDA+Shift+S (laptop) reads back selected text before copying.
- **Command category labels:** [NVDA command] / [Windows command] labels added throughout all five chapters where commands are introduced.
- **Turkish localization:** First Turkish translation contributed by Umut KORKMAZ (pending integration).
- Thank you to **Chris, Mike, Kevin, Julie, Larry, Jim, McKayla, and Skyler** — AT specialists with Pacific Northwest state agencies — for hands-on feedback from April 2026 training sessions that drove this release.

## What's New in v1.3.2

- **Localization fully activated:** `addonHandler.initTranslation()` was missing from both plugin modules — meaning all `_()` wrapped strings silently fell back to English for every user. This is now fixed. Identified by Valentin Kupriyanov.
- **Language-aware doc file resolution:** The resources page, browse mode practice page, and user guide now open from the user's language folder (e.g. `doc/ru/`) when a translation exists, falling back to `doc/en/`. Previously hardcoded to English.
- **Additional strings wrapped for translation:** Dialog title, introduction text, welcome screen, and several display text blocks were bare string literals not accessible to translators. All wrapped.
- **First complete Russian localization:** All UI strings, all five lesson chapters, the user guide, practice page, and resources page are now available in Russian. Contributed by Valentin Kupriyanov, Head of the Russian-speaking NVDA user community (nvda.ru).

See [CHANGELOG.md](CHANGELOG.md) for the full version history.

---

## What's Included — 41 Lessons Across Six Chapters

### Chapter 1: Getting Started with NVDA — 13 lessons
An orientation to the three categories of keyboard commands (Windows, program, and screen reader), followed by the essential NVDA commands every new user needs: the NVDA modifier key, reading the title bar, checking the time, silencing speech, identifying current focus, Tab navigation, activating buttons and checkboxes, reading the current line, Input Help mode, opening the user guide, keyboard physical orientation, and switching windows with Alt+Tab. Several lessons include a live accessible practice form with real buttons, checkboxes, and text fields.

### Chapter 2: Your Keyboard — 3 lessons
Where modifier keys live on standard and laptop keyboards (Ctrl, Shift, Alt, Windows key, NVDA key), how function keys and the Fn key work (Fn+arrows for Home/End/Page Up/Page Down, Fn Lock, multimedia vs F-key mode), and how to select and switch your NVDA keyboard layout setting. Placed early so students have physical keyboard confidence before command learning begins.

### Chapter 3: Reading and Moving Through Text — 7 lessons
Character-by-character, word-by-word, and line-by-line navigation; jumping to document start and end; Say All (desktop: NVDA+Down Arrow, laptop: NVDA+A); text selection with Shift+arrows including NVDA's report-selection command; and navigating by paragraph (Ctrl+Up/Down) and page (Page Up/Down). Every lesson embeds a practice text area directly in the Coach window — no switching to another application required.

### Chapter 4: Browse Mode and Web Navigation — 10 lessons
What browse mode is and how it works, heading navigation, heading level shortcuts, link navigation, form field navigation, toggling between browse mode and focus mode, landmark and list navigation, the Elements List dialog, finding text with NVDA Find, and navigating table cells with Ctrl+Alt+Arrow keys. A fully accessible practice web page opens automatically when you start any lesson in this chapter.

### Chapter 5: Object Navigation — 6 lessons
How NVDA's object pyramid works, moving across objects at the same level, climbing up and descending through levels, reading the current navigator object, routing keyboard focus to any control on screen, and when object navigation is the right tool. Uses levels/pyramid terminology throughout. Desktop and laptop layouts documented.

### Chapter 6: Customizing NVDA — 2 lessons
Changing your keyboard layout between desktop (numpad) and laptop (letter keys), and adjusting speech rate, voice, and synthesizer settings — including on-the-fly speed shortcuts with the synth settings ring. Completing this chapter triggers the Certificate of Completion.

---

## How It Works

The Coach presents one step at a time. Each step:
- Speaks an instruction and tells you which key to press
- Waits for you to perform the action and press Enter to continue
- Offers **F1** to repeat the instruction, **F2** for a hint, **F3** to skip the step

### Coach Window Keyboard Shortcuts
| Key | Action |
|-----|--------|
| Enter / Space | Advance to next step (or next lesson after completion) |
| F1 | Repeat current instruction |
| F2 | Get a hint (press again to cycle through up to 3 hints per step) |
| F3 | Skip this step |
| Ctrl+N | Move to next lesson |
| Ctrl+B | Go back to previous lesson |
| Ctrl+R | Restart current lesson from the beginning |
| NVDA+Shift+C | Open the lesson picker (or return to the Coach window) |
| Escape × 3 | Close the Coach window |

> **Hotkey conflict?** `NVDA+Shift+C` can be remapped via NVDA menu → Preferences → Input Gestures → NVDA Coach.

### Progress Tracking
Completed lessons are marked in the lesson picker and saved across NVDA restarts, so you can pick up exactly where you left off.

---

## For AT Instructors and TVIs

NVDA Coach was built by an AT instructor for classroom and one-on-one use. Assign a chapter before a session, use it as a structured warm-up, or give it to students for independent practice between appointments. The lesson picker shows completed lessons at a glance so you and the student can track progress together.

### Custom Lessons

All lessons are plain JSON files in `globalPlugins/nvdaCoach/lessons/`. Adding a new lesson set is as simple as dropping a new `.json` file in that folder. The existing files serve as templates, and the format is documented in the [user guide](doc/en/readme.html).

Get in touch at [info@tonygebhard.me](mailto:info@tonygebhard.me) to discuss custom lesson development for your program, organization, or student population.

---

## Building from Source

```bash
cd nvdaCoach-source
python -c "
import zipfile, os
output = 'nvdaCoach-1.5.nvda-addon'
if os.path.exists(output): os.remove(output)
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('manifest.ini', 'manifest.ini')
    for root, dirs, files in os.walk('globalPlugins'):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for file in files:
            if not file.endswith('.pyc'): zf.write(os.path.join(root,file), os.path.join(root,file).replace(os.sep,'/'))
    for root, dirs, files in os.walk('doc'):
        for file in files: zf.write(os.path.join(root,file), os.path.join(root,file).replace(os.sep,'/'))
    for root, dirs, files in os.walk('locale'):
        for file in files: zf.write(os.path.join(root,file), os.path.join(root,file).replace(os.sep,'/'))
"
```

---

## Planned for Future Versions

- Working with email and Microsoft Office chapters
- Braille display interaction module
- Lesson difficulty and pace settings
- Instructor progress reporting

If you have ideas for lessons, commands that should be covered, or feedback on your experience, [open an issue](https://github.com/tonygeb23/nvdaCoach-/issues) or email [info@tonygebhard.me](mailto:info@tonygebhard.me).

---

## Acknowledgments

Thank you to the testers and community members who have shaped NVDA Coach through their feedback:

- **Jessica Tegner** (Be My Eyes) — invaluable early feedback and feature and lesson requests
- **Darrell Hilliker**, CPWA, Salesforce Certified UX Designer
- **Rui Fontes** (NVDA Portuguese translation team)
- **John Hess**, Adaptive Technology Specialist, State Services for the Blind — detailed correction of laptop keyboard layout gestures in the Object Navigation chapter
- **Brandon Patterson** — correction of synth settings ring keystrokes in the Customizing NVDA chapter
- **Valentin Kupriyanov**, Head of the Russian-speaking NVDA user community — internationalization and localization proposal, first complete Russian localization, and detailed localization bug report
- **Umut KORKMAZ** (Turkey) — Turkish translation
- **Chris, Mike, Kevin, Julie, Larry, Jim, McKayla, and Skyler** — assistive technology specialists with Pacific Northwest state agencies, hands-on feedback from April 2026 training sessions
- **Nash** — feature and lesson requests
- **Brian**
- **Gene**
- **Joseph**
- Anonymous community members who have written in with corrections and encouragement

---

## Support This Project

NVDA Coach is free and will always remain free. If it has been useful to you, your students, or someone you care about, a contribution helps keep it going — covering development time, testing, and continued expansion of lessons and language support.

**[Contribute via PayPal](https://paypal.me/tonygebhard)**

Contributors are recognized by name in the project's acknowledgments with their permission. If you'd prefer to remain anonymous, just note that when you contribute and your name will not be listed. Every contribution, at any amount, is genuinely appreciated.

---

## Contact

**Tony Gebhard**, Assistive Technology Instructor
[info@tonygebhard.me](mailto:info@tonygebhard.me) · [tonygebhard.me](https://tonygebhard.me)
