# NVDA Coach

**Interactive screen reader training built right into NVDA.**

NVDA Coach is a free add-on for the [NVDA screen reader](https://nvaccess.org) that teaches commands through guided, step-by-step practice sessions — from inside NVDA itself. No videos, no PDFs, no switching between windows. Press one key combination and the Coach walks you through what to do and why, one step at a time.

**Current version:** 1.1.0
**Author:** Tony Gebhard, Assistive Technology Instructor
**License:** GPL v2

---

## Download and Install

**[Download NVDA Coach v1.1.0](https://github.com/tonygeb23/nvdaCoach-/releases/download/v1.1.0/nvdaCoach-1.1.0.nvda-addon)**

1. Download the `.nvda-addon` file above
2. Open the file — NVDA handles the installation automatically and asks you to confirm
3. Press **NVDA+Shift+C** — the Coach window opens and you're ready to begin

NVDA 2024.1 or later required. Available in the NVDA Add-on Store (Tools → Add-on Store).

---

## What's New in v1.1.0

- **Sound toggle** — NVDA menu → Preferences → Settings → NVDA Coach to turn chimes on or off
- **Practice windows open on your cue** — a priming step gives the Alt+Tab reminder before any practice form appears
- **Enter advances after lesson completion** — consistent with all other key behavior in the Coach window
- **"Try it now" prompts now spoken aloud** — NVDA announces the advance cue automatically, not just on screen
- **NVDA vs. Windows command labels** — every step now tells you whether a command is NVDA-specific or universal
- **New chapter: Object Navigation** — 6 lessons on navigating controls that Tab cannot reach
- **New chapter: Customizing NVDA** — keyboard layout, speech rate, and voice settings
- **Two new browse mode lessons** — NVDA Find (`NVDA+Ctrl+F`) and toggling single-letter navigation (`NVDA+Shift+Space`)

See [CHANGELOG.md](CHANGELOG.md) for the full history.

---

## What's Included — 34 Lessons Across Five Chapters

### Chapter 1: Getting Started with NVDA — 10 lessons
The essential commands every new NVDA user needs: the NVDA modifier key, reading the title bar, checking the time, silencing speech, identifying current focus, Tab navigation, activating buttons and checkboxes, reading the current line, Input Help mode, and opening the user guide. Several lessons include a live accessible practice form with real buttons, checkboxes, and text fields.

### Chapter 2: Reading and Moving Through Text — 6 lessons
Character-by-character, word-by-word, and line-by-line navigation; jumping to document start and end; Say All (continuous reading); and text selection with Shift+arrows. Every lesson embeds a practice text area directly in the Coach window — no switching to Notepad or another application.

### Chapter 3: Browse Mode and Web Navigation — 10 lessons
What browse mode is and how it works, heading navigation, heading level shortcuts, link navigation, form field navigation, toggling between browse mode and focus mode, landmark and list navigation, the Elements List dialog, finding text with NVDA Find, and toggling single-letter navigation. A fully accessible practice web page opens automatically in your browser when you start any lesson in this chapter.

### Chapter 4: Object Navigation — 6 lessons
How NVDA's object tree works, moving to next and previous objects, moving to parent and child objects, reading the current navigator object, routing keyboard focus to any control on screen, and when object navigation is the right tool. Desktop and laptop keyboard layouts are both documented throughout. This chapter covers controls that Tab cannot reach.

### Chapter 5: Customizing NVDA — 2 lessons
Changing your keyboard layout between desktop (numpad) and laptop (letter keys), and adjusting speech rate, voice, and synthesizer settings — including on-the-fly speed shortcuts.

---

## How It Works

The Coach presents one step at a time. Each step:
- Speaks an instruction, labels it as an NVDA command or universal shortcut, and tells you which key to press
- Waits for you to perform the action and press Enter to continue
- Offers **F1** to repeat the instruction, **F2** for a hint, **F3** to skip the step

### Coach Window Keyboard Shortcuts
| Key | Action |
|-----|--------|
| Enter / Space | Advance to next step (or next lesson after completion) |
| F1 | Repeat current instruction |
| F2 | Get a hint |
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
output = 'nvdaCoach-1.1.0.nvda-addon'
if os.path.exists(output): os.remove(output)
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('manifest.ini', 'manifest.ini')
    for root, dirs, files in os.walk('globalPlugins'):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for file in files:
            if not file.endswith('.pyc'): zf.write(os.path.join(root,file), os.path.join(root,file).replace(os.sep,'/'))
    for root, dirs, files in os.walk('doc'):
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

## Contact

**Tony Gebhard**, Assistive Technology Instructor
[info@tonygebhard.me](mailto:info@tonygebhard.me) · [tonygebhard.me](https://tonygebhard.me)
