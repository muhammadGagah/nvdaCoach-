# Translating NVDA Coach

Thank you for your interest in translating NVDA Coach!
This guide covers everything you need to contribute a translation of the add-on UI strings and lesson content.

---

## What can be translated

NVDA Coach has two layers of translatable content:

| Layer | What it is | Where to find it |
|---|---|---|
| **UI strings** | Button labels, spoken announcements, status messages, hint output | `locale/<lang>/LC_MESSAGES/nvda.po` |
| **Lesson content** | Full lesson text, step instructions, hints | `globalPlugins/nvdaCoach/lessons/<lang>/` |

Both layers are needed for a complete translation.
A UI-only translation is still valuable and can be submitted on its own.

---

## Translating UI strings (the .po file)

### 1. Copy the template

The translation template is at:

```
locale/nvda.pot
```

Copy it to a new file at:

```
locale/<your-language-code>/LC_MESSAGES/nvda.po
```

For example, for Portuguese (Portugal):

```
locale/pt_PT/LC_MESSAGES/nvda.po
```

For Russian:

```
locale/ru/LC_MESSAGES/nvda.po
```

Use the standard NVDA language codes (e.g. `de`, `fr`, `es`, `pt_BR`, `zh_CN`).

### 2. Fill in the file header

At the top of your `.po` file, fill in:

```
"Language: ru\n"
"Language-Team: Russian NVDA user community\n"
"Last-Translator: Your Name <your@email.com>\n"
"PO-Revision-Date: YYYY-MM-DD HH:MM+0000\n"
```

Remove the `#, fuzzy` line from the header once you have filled it in.

### 3. Translate each string

For each entry, fill in the `msgstr` with your translation:

```po
msgid "Lesson stopped."
msgstr "Leçon arrêtée."
```

Leave `msgstr ""` empty for any string you are not yet sure about — NVDA Coach will fall back to English for untranslated strings.

### Tips

- Strings containing `{placeholders}` like `{title}` or `{stepNum}` must keep those placeholders exactly as written. Only translate the surrounding text.
- Unicode characters (arrows, bullets, em-dashes) can be kept as-is or replaced with equivalents that make sense in your language.
- You do not need to compile the `.po` to a `.mo` file — NVDA handles that automatically during installation.

---

## Translating lesson content

Lesson files are JSON. Each lesson is a plain text file you can open in any editor.

### 1. Copy the English lesson folder

```
globalPlugins/nvdaCoach/lessons/en/
```

Copy the entire folder to:

```
globalPlugins/nvdaCoach/lessons/<your-language-code>/
```

### 2. Translate each JSON file

There are five lesson files:

| File | Chapter |
|---|---|
| `getting_started.json` | Chapter 1: Getting Started with NVDA |
| `reading_text.json` | Chapter 2: Reading and Moving Through Text |
| `browse_mode.json` | Chapter 3: Browse Mode and Web Navigation |
| `object_navigation.json` | Chapter 4: Object Navigation |
| `nvda_settings.json` | Chapter 5: Customizing NVDA |

For each file, translate:
- `"title"` — the chapter/lesson title
- `"description"` — the chapter description shown in the lesson picker
- `"instruction"` — the spoken instruction for each step
- `"hints"` — the three hint strings for each step

Do **not** change:
- `"id"` values
- `"type"` values
- `"monitorGestures"` or `"expectedGestures"` — these are key codes, not text
- `"practiceText"` — leave in English unless you have verified screen reader behaviour with translated text

### 3. Key command names in instructions

When referring to key names in instructions (e.g. "Press NVDA+T"), keep the key names in their standard form for your locale. NVDA's own documentation for your language is the best reference.

---

## Submitting your translation

1. Fork the repository: https://github.com/tonygeb23/nvdaCoach-
2. Add your files under `locale/<lang>/` and/or `globalPlugins/nvdaCoach/lessons/<lang>/`
3. Open a pull request with the title: `[Translation] <Language name>`
4. Include your name and contact in the PR description so you can be acknowledged in the release notes

Questions? Email: info@tonygebhard.me

---

## Language codes reference

| Language | Code |
|---|---|
| English | `en` |
| French | `fr` |
| German | `de` |
| Spanish | `es` |
| Portuguese (Portugal) | `pt_PT` |
| Portuguese (Brazil) | `pt_BR` |
| Russian | `ru` |
| Chinese (Simplified) | `zh_CN` |
| Chinese (Traditional) | `zh_TW` |
| Japanese | `ja` |
| Arabic | `ar` |

Use the same codes NVDA uses — see the NVDA source for the full list.

---

## Maintainer

Tony Gebhard — Assistive Technology Instructor
info@tonygebhard.me
https://github.com/tonygeb23/nvdaCoach-
