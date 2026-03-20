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

## Change Log

| Version | Date       | Item         | Description |
|---------|------------|--------------|-------------|
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
