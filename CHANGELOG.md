# NVDA Coach — Changelog

## v1.1.0 (2026-03-19)

### Bug Fixes
- **"Try it now" prompts now spoken aloud** — gesture steps now include the "Try it now. When you are ready to continue, press Enter" cue in the spoken announcement, not just in the on-screen text (#004 — Darrell Hilliker)
- **Enter key advances after lesson completion** — in the idle/between-lesson state, pressing Enter or Numpad Enter now moves to the next lesson, consistent with other key behaviors (#003 — Darrell Hilliker)
- **Practice windows no longer open unexpectedly** — the Tab Navigation, Activate Controls, and Find Out Where You Are lessons now show a priming step first, giving users the Alt+Tab reminder before the practice window appears (#003 — Darrell Hilliker)

### New Features
- **Sound toggle** — NVDA Settings panel added (NVDA menu > Preferences > Settings > NVDA Coach) with a "Play sounds during lessons" checkbox; all coaching chimes respect this setting (#002 — Gene)

### Lesson Content
- **NVDA vs. Windows labels** — all lesson step instructions now include a `[NVDA command]`, `[NVDA browse mode key]`, or `[Universal shortcut]` label so learners understand which commands are specific to NVDA and which work in any Windows application (#002 — Gene)
- **"Why" framing** — all lessons updated with sighted-equivalent context (e.g., "Sighted users can glance at the title bar. NVDA+T speaks it to you.") (#002 — Gene)
- **New chapter: Object Navigation** — 6 lessons covering the NVDA object tree, moving to next/previous/parent/child objects, reading and examining objects, and routing keyboard focus to inaccessible controls (desktop and laptop layout keys documented throughout) (#001 — Joseph)
- **New chapter: Customizing NVDA** — 2 lessons on changing keyboard layout (desktop vs. laptop) and adjusting speech rate and voice (#001 — Joseph)
- **Browse Mode lesson 9: Find Text on a Page** — NVDA+Ctrl+F, NVDA+F3, NVDA+Shift+F3 (#001 — Joseph)
- **Browse Mode lesson 10: Toggle Single-Letter Navigation** — NVDA+Shift+Space (#001 — Joseph)

### Hotkey Conflict Note
The default gesture `NVDA+Shift+C` conflicts with Excel's "set column headers" command. Users can remap it via NVDA menu > Preferences > Input Gestures > NVDA Coach (#001 — Joseph)

---

## v1.0.0 (2026-03-14)

Initial release. Three chapters covering Getting Started, Reading and Moving Through Text, and Browse Mode and Web Navigation. 24 lessons total.
