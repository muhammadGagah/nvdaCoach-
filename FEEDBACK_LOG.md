# NVDA Coach — Feedback Log

Tracks user feedback for prioritization, implementation, and release planning.

---

## Status Key
- `[ ]` Open — not yet addressed
- `[~]` In progress
- `[x]` Implemented — include version and commit when resolved

---

## Feedback #001 — Joseph (received 2026-03-14)

**Source:** Email / community feedback

### Bug Reports / Conflicts
- `[x]` **Hotkey conflict:** `NVDA+Shift+C` conflicts with Excel's "set column headers" command. **Resolution (v1.1.0):** The gesture is already registered in NVDA's input system via the `@script` decorator. Users can remap it via NVDA menu > Preferences > Input Gestures > NVDA Coach. Documented in README.

### Store / Release Notes
- `[x]` Add-on will not appear in the NV Access add-on store until approved. First-time submission requires NV Access review. No action needed beyond awaiting approval — noted in release comms.

### Lesson Suggestions
- `[x]` Add a lesson collection on **object navigation** (navigating keyboard-inaccessible controls). **Resolution (v1.1.0):** New chapter `object_navigation.json` — 6 lessons.
- `[x]` Add a lesson on **changing NVDA keyboard layout** (desktop vs. laptop). **Resolution (v1.1.0):** New chapter `nvda_settings.json`, lesson 1.
- `[x]` Add browse mode lesson: **NVDA Find command** (`NVDA+Ctrl+F`). **Resolution (v1.1.0):** Added as lesson 9 in `browse_mode.json`.
- `[x]` Add browse mode lesson: **toggling single letter navigation** (`NVDA+Shift+Space`). **Resolution (v1.1.0):** Added as lesson 10 in `browse_mode.json`.
- `[ ]` Add browse mode lesson: **interacting with math content**. Deferred — requires MathPlayer which many users won't have. Added a note in browse mode resources instead.

---

## Feedback #002 — Gene (received 2026-03-14)

**Source:** Email / community feedback

### Sound / Audio
- `[x]` **Sounds should be removable or togglable.** **Resolution (v1.1.0):** Added NVDA Settings panel (NVDA menu > Preferences > Settings > NVDA Coach) with a "Play sounds during lessons" checkbox. All tones are gated on this setting.

### Content / Pedagogy
- `[x]` **Distinguish NVDA commands from Windows/application commands.** **Resolution (v1.1.0):** All lesson step instructions now include `[NVDA command]`, `[NVDA browse mode key]`, or `[Universal shortcut]` labels.
- `[x]` **Provide context for why screen reader commands exist.** **Resolution (v1.1.0):** All lessons updated with "sighted equivalent" framing (e.g., "Sighted users can glance at the title bar. NVDA+T speaks it to you.").

---

## Feedback #003 — Darrell Hilliker (received 2026-03-17)

**Source:** Email / community feedback
**Credentials:** CPWA, Salesforce Certified UX Designer, NU7I (ham radio)

### UX / Navigation
- `[x]` **Enable Enter key to advance to next lesson after completion.** **Resolution (v1.1.0):** In `CoachWindow._onKey`, idle state now handles Enter/Numpad Enter by calling `nextLesson()`.

### Practice Windows / Focus Management
- `[x]` **Practice windows steal focus before users are ready.** **Resolution (v1.1.0):** Practice frames no longer open at lesson start. A priming step with `openPracticeFrameAfter: true` is added to the affected lessons (`where_am_i`, `tab_navigation`, `activate_controls`). The window opens only after the user reads the Alt+Tab reminder and presses Enter.

---

## Feedback #004 — Darrell Hilliker (received 2026-03-17)

**Source:** Email / community feedback

### Prompt Announcement / Auto-read
- `[x]` **"Try it now" prompts are not auto-announced in some lessons.** **Resolution (v1.1.0):** In `lessonRunner._speakCurrentStep()`, the spoken message for gesture-type steps now includes the "Try it now. When you are ready to continue, press Enter or click Next Step." cue.

---

## Feedback #005 — Rui Fontes (received 2026-03-20)

**Source:** Email / community feedback
**Credentials:** NVDA Portuguese translation team

### Localization / i18n
- `[ ]` **Localize the add-on and lessons by language subfolder.** Support language-specific lesson content by organizing the `lessons/` directory into language subfolders (e.g., `lessons/en/`, `lessons/pt/`). The add-on would detect NVDA's current language setting and load the matching subfolder, falling back to `en/` if no translation exists. This would allow the Portuguese team (and others) to translate lesson content without touching Python code.

**Notes:**
- Rui is on the NVDA Portuguese translation team — potential collaborator for a `pt/` lesson set
- UI strings (button labels, error messages, settings panel) would also need gettext/`.po` file support to be fully localizable
- Consider reaching out to Rui if/when localization work begins

---

## Feedback #006 — Brian (received 2026-03-21)

**Source:** Email / community feedback
**Context:** Builds on and refines #002 (Gene) — the v1.1.0 inline label approach (`[NVDA command]`, `[Universal shortcut]`) is a step in the right direction but doesn't go far enough

### Content / Pedagogy — Command Category Framework
- `[ ]` **Teach the three-way command framework as a concept, not just a label.** Instead of tagging individual commands inline, teach users *once* — clearly and early — what the three categories are and how to identify them:
  1. **Windows commands** — handled by the OS. Cut/Copy/Paste, opening Start Menu. Many programs call Windows to do these; the programs themselves are not performing the operation.
  2. **Program/application commands** — handled by the application. Ctrl+N in Word opens a new document. Pressing down arrow moves the cursor — the screen reader reads what you moved to, but the *program* moved the cursor.
  3. **Screen reader commands** — handled by NVDA. They **take no action** in the program. They only announce, read, or describe. NVDA+T announces the title bar — nothing changes, you just find out where you are. A sighted person can glance at the title bar; a blind person cannot, so NVDA supplies the equivalent.
- `[x]` **Remove inline labels entirely in favor of conceptual understanding.** **Resolution (v1.2.0):** All `[NVDA command]`, `[NVDA browse mode key]`, `[NVDA feature]`, `[NVDA browse mode keys]`, and `[Universal shortcut]` tags stripped from every step across all five lesson JSON files (28 instances total).
- `[x]` **Add a dedicated "Understanding Command Categories" lesson** as a new lesson in Chapter 1. **Resolution (v1.2.0):** New lesson `command_categories` added as order 1 in `getting_started.json`. Four steps teach the Windows / program / screen reader framework before any command practice begins. All existing Chapter 1 lessons shifted to orders 2–11.

**Notes:**
- Brian explicitly called out that Cut/Copy/Paste are Windows shortcuts — many users and even documentation sources misattribute these to the application
- The key differentiator for screen reader commands: "It takes no action. It reads." — this framing is highly teachable
- **v1.2 decision: Option B.** Add the framework lesson. Remove all inline labels. Trust the learner.

---

## Change Log

| Version | Date       | Item         | Description |
|---------|------------|--------------|-------------|
| 1.2.0   | 2026-03-21 | #006         | New lesson: Understanding Command Categories (Chapter 1, lesson 1) |
| 1.2.0   | 2026-03-21 | #006         | Removed all inline command labels from all five lesson files (28 instances) |
| 1.1.0   | 2026-03-19 | #004         | "Try it now" cue now spoken aloud for all gesture steps |
| 1.1.0   | 2026-03-19 | #003         | Enter key advances to next lesson after completion |
| 1.1.0   | 2026-03-19 | #003         | Practice windows now open only after priming step |
| 1.1.0   | 2026-03-19 | #002         | Added sound toggle in NVDA Settings panel |
| 1.1.0   | 2026-03-19 | #002         | NVDA-vs-Windows labels added to all lesson steps |
| 1.1.0   | 2026-03-19 | #002         | "Why" framing added to all lesson instructions |
| 1.1.0   | 2026-03-19 | #001         | Hotkey remapping documented (Input Gestures) |
| 1.1.0   | 2026-03-19 | #001         | New chapter: Object Navigation (6 lessons) |
| 1.1.0   | 2026-03-19 | #001         | New chapter: Customizing NVDA (2 lessons) |
| 1.1.0   | 2026-03-19 | #001         | Browse mode lesson 9: NVDA Find |
| 1.1.0   | 2026-03-19 | #001         | Browse mode lesson 10: Toggle single-letter navigation |
