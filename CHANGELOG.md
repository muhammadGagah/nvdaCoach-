# NVDA Coach — Changelog

## v1.3.2 (2026-03-29)

### Bug Fixes — Localization
- **`addonHandler.initTranslation()` added to both plugin modules:** This call was missing from `__init__.py` and `lessonRunner.py`, which meant all `_()` wrapped strings silently fell back to English regardless of the user's NVDA language. Translation was structurally in place but never activated. Identified by Valentin Kupriyanov.
- **Dialog title now translatable:** The lesson picker window title ("NVDA Coach — Choose a Lesson") was not wrapped in `_()`.
- **Introduction / About NVDA Coach text now translatable:** The full introduction text shown when a user selects "Introduction / About NVDA Coach" from the lesson picker was not wrapped in `_()`.
- **Welcome screen text now translatable:** The initial welcome text displayed in the Coach window on first launch was not wrapped in `_()`.
- **`showIdle()`, `showBrowseModeCompletion()`, and `beginEscapeSequence()` text blocks now translatable:** These display strings were bare Python string literals with no `_()` wrapper.
- **Language-aware doc file resolution:** The resources page, browse mode practice page, and user guide (readme.html) were hardcoded to open from `doc/en/` regardless of the user's language. A new `_localizedDocPath()` helper now resolves to `doc/{lang}/` first, falling back to `doc/en/`. Identified by Valentin Kupriyanov.

### New Translation — Russian
- **First complete Russian localization of NVDA Coach**, contributed by Valentin Kupriyanov, Head of the Russian-speaking NVDA user community (nvda.ru):
  - `locale/ru/LC_MESSAGES/nvda.po` — full translation of all UI strings
  - `locale/ru/manifest.ini` — localized add-on summary and description
  - `globalPlugins/nvdaCoach/lessons/ru/` — all five lesson chapters translated into Russian
  - `doc/ru/` — practice page, user guide, resources page, and TTS scripts translated into Russian

### Acknowledgments
- Valentin Kupriyanov, Head of the Russian-speaking NVDA user community — first complete Russian localization of NVDA Coach, and detailed localization bug report identifying all issues fixed in this release

---

## v1.3.1 (2026-03-28)

### Bug Fixes / Patch
- **Localization scaffolding added:** `locale/nvda.pot` (101-string translation template), `locale/en/LC_MESSAGES/nvda.po` (English base file), and `TRANSLATING.md` (contributor guide) were missing from v1.3. The `_()` wrapping was in place but translators had no `.pot` file to work from and no `locale/` folder structure. Issue identified by Rui Fontes of the NVDA Portuguese translation team.

### Acknowledgments
- Rui Fontes, NVDA Portuguese translation team — identified missing `.pot` file and `locale/` folder structure

---

## v1.3 (2026-03-28)

### New Features
- **Localization infrastructure:** Lesson content is now organized into language subfolders (`lessons/en/`). NVDA Coach automatically detects the active NVDA language using `languageHandler.getLanguage()` and loads lessons from the matching subfolder (e.g. `lessons/fr/` for French, `lessons/pt/` from `pt_BR`), falling back to `lessons/en/` when no translation is available. Translators can contribute localized lesson sets by adding a language folder — no code changes required. Proposed by Valentin Kupriyanov, Head of the Russian-speaking NVDA user community.
- **Full i18n string wrapping (`__init__.py` and `lessonRunner.py`):** All user-facing strings in the add-on code are now wrapped with `_()` for gettext translation. This covers button labels, status bar text, spoken announcements, hint output, lesson picker UI, practice frame headings and feedback messages, and all `ui.message()` calls throughout both plugin files. Combined with the lesson folder architecture, this provides the complete foundation for community-contributed localizations.

### Acknowledgments
- Valentin Kupriyanov, Head of the Russian-speaking NVDA user community — internationalization and localization architecture proposal

---

## v1.2.2 (2026-03-28)

### Bug Fixes
- **Synth settings ring — Customizing NVDA chapter:** The lesson previously stated that NVDA+Ctrl+Right/Left Arrow changes speech speed. This is incorrect. NVDA+Ctrl+Right/Left Arrow navigates between synth settings ring items (Rate, Pitch, Volume, Voice, Variant). Speech speed (Rate) is increased with NVDA+Ctrl+Up Arrow and decreased with NVDA+Ctrl+Down Arrow. Both desktop and laptop layouts documented throughout. Reported by Brandon Patterson.

### New Features
- **F2 hint cycling:** Pressing F2 during a lesson now cycles through up to three hints per step, announced as "Hint 1 of 3", "Hint 2 of 3", etc. The hint index resets automatically when advancing to the next step. Falls back gracefully to the legacy single-hint string format for any steps that use it. Previously, many steps returned "no hint available."
- **All steps fully hinted:** Every step across all five chapters and 35 lessons now has a hints array covering key location, finger placement, and real-world context. Previously only gesture steps had hints; info steps had none.
- **Full cross-chapter connectivity:** Every chapter's final lesson now names the next chapter and references earlier lessons where relevant. Key chapters cross-reference each other — e.g., the synth settings ring step references the Tab navigation lesson from Getting Started; the chapter complete screens name the next chapter explicitly.

### Acknowledgments
- Brandon Patterson — synth settings ring keystroke correction
- Valentin Kupriyanov, Head of the Russian-speaking NVDA user community — internationalization and localization proposal (logged for a future release)

---

## v1.2.1 (2026-03-27)

### Bug Fixes
- **Object Navigation — laptop layout:** Four laptop layout gestures were missing the Shift key. Moving to the next and previous object at the same level is NVDA+Shift+Right/Left Arrow; moving to parent and first child is NVDA+Shift+Up/Down Arrow. Without Shift, those keystrokes invoke review cursor movement (by character/line) instead of object navigation. Reported and verified via NVDA input help by John Hess, AT Specialist, State Services for the Blind, Saint Paul, MN.
- **Say All lesson — laptop layout:** The lesson previously showed only the desktop layout keystroke (NVDA+Down Arrow). Laptop layout users press NVDA+A. Both layouts are now documented in the lesson intro, practice step, and chapter summary. Reported by an anonymous community member using laptop layout.

### Audio
- Lesson complete sound volume raised by 15%.

### Documentation
- README.md, CHANGELOG.md, and doc/en/readme.html updated in tandem.
- Acknowledgments updated to include John Hess and anonymous contributors.

---

## v1.2.0 (2026-03-21)

### New Lesson Content
- **New lesson: Understanding Command Categories** — added as Lesson 1 of Chapter 1 (Getting Started). Four steps teach learners to distinguish Windows commands, program/application commands, and screen reader commands before any command practice begins. Key framing: screen reader commands take no action — they only inform. (#006 — Brian)

### Lesson Content Changes
- **Removed all inline command labels** — all `[NVDA command]`, `[NVDA browse mode key]`, `[NVDA feature]`, and `[Universal shortcut]` tags stripped from every step across all five lesson files (28 instances). The Understanding Command Categories lesson carries this pedagogical weight instead, trusting learners to apply the framework themselves. (#006 — Brian)

### Sound and Audio
- **Sound branding overhaul** — all five sound moments (lesson start, step advance, hint, lesson stop, lesson complete) replaced with custom WAV audio files. The sound toggle in NVDA Settings disables all of them.

### New Features
- **NVDA Coach Help in the NVDA Help menu** — NVDA menu → Help → NVDA Coach Help opens the user guide directly. (#008 — Jessica Tegner)
- **Chapter navigation keys** — Ctrl+N (next lesson), Ctrl+B (previous lesson), Ctrl+R (restart current lesson) added to the Coach window.

---

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
