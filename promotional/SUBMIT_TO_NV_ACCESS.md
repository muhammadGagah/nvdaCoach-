# Submitting NVDA Coach to the NV Access Add-on Store

## Overview

The NV Access Add-on Store accepts submissions via a GitHub pull request to the
`nvaccess/addon-store-submission` repository. The process is entirely free.
Your add-on will appear in NVDA's built-in Add-on Store once reviewed and merged.

Official documentation:
  https://github.com/nvaccess/addon-store-submission

---

## What You Need Before Submitting

1. **A GitHub account** (free at https://github.com)
2. **The built .nvda-addon file** — `nvdaCoach-1.0.0.nvda-addon` (included in this folder)
3. **A public release URL** — Host the addon file somewhere publicly downloadable.
   Recommended options:
   - GitHub Releases (free, reliable, preferred by NV Access)
   - Your own web server at tonygebhard.me/NVDACoach

---

## Step 1 — Host the Release on GitHub

1. Create a GitHub repository for NVDA Coach (e.g., `github.com/tonygebhard/nvdaCoach`)
2. Push your source code to it
3. Create a **Release** on GitHub:
   - Go to your repo → Releases → "Create a new release"
   - Tag: `v1.0.0`
   - Title: `NVDA Coach 1.0.0`
   - Upload `nvdaCoach-1.0.0.nvda-addon` as the release asset
   - Publish the release
4. Copy the direct download URL for the .nvda-addon file, which will look like:
   `https://github.com/tonygebhard/nvdaCoach/releases/download/v1.0.0/nvdaCoach-1.0.0.nvda-addon`

---

## Step 2 — Fork the Submission Repository

1. Go to: https://github.com/nvaccess/addon-store-submission
2. Click **Fork** (top right) to create your own copy
3. Clone your fork locally, or use GitHub's web editor

---

## Step 3 — Create the Submission JSON File

In your fork, create the following file path:

  addons/nvdaCoach/1.0.0.json

Paste the content below, updating the `URL` field with your actual release URL:

```json
{
  "addonId": "nvdaCoach",
  "addonVersionName": "1.0.0",
  "addonVersionNumber": {
    "major": 1,
    "minor": 0,
    "patch": 0
  },
  "displayName": "NVDA Coach",
  "description": "An interactive, in-NVDA training system that teaches screen reader commands through guided, hands-on drills with real-time feedback. Built by an assistive technology instructor for absolute beginners.",
  "author": "Tony Gebhard",
  "homepage": "https://tonygebhard.me/NVDACoach",
  "minNVDAVersion": {
    "major": 2024,
    "minor": 1,
    "patch": 0
  },
  "lastTestedVersion": {
    "major": 2025,
    "minor": 1,
    "patch": 0
  },
  "channel": "stable",
  "URL": "https://github.com/tonygebhard/nvdaCoach/releases/download/v1.0.0/nvdaCoach-1.0.0.nvda-addon",
  "sha256": "REPLACE_WITH_SHA256_HASH_OF_NVDA_ADDON_FILE"
}
```

### How to get the SHA256 hash

Run this command in PowerShell:

```powershell
Get-FileHash nvdaCoach-1.0.0.nvda-addon -Algorithm SHA256
```

Or on any system with Python:

```python
import hashlib
with open("nvdaCoach-1.0.0.nvda-addon", "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())
```

Replace `REPLACE_WITH_SHA256_HASH_OF_NVDA_ADDON_FILE` in the JSON with the result.

---

## Step 4 — Open the Pull Request

1. Commit your new `addons/nvdaCoach/1.0.0.json` file to your fork
2. Go to your fork on GitHub and click **Contribute → Open pull request**
3. Base repository: `nvaccess/addon-store-submission`  Base branch: `master`
4. PR title: `Add nvdaCoach 1.0.0`
5. In the PR description, include:
   - A brief description of what NVDA Coach does
   - Confirmation that you have tested with NVDA 2025.1
   - Your contact email: info@tonygebhard.me
6. Submit the pull request

NV Access reviewers typically respond within a few days to a couple of weeks.
They may ask for minor changes to the JSON or the manifest before merging.

---

## Add-on Store Listing Details

Use this text when filling out any additional listing fields:

**Short description (one line):**
Interactive screen reader training for NVDA beginners — guided, hands-on drills from inside NVDA itself.

**Full description:**
NVDA Coach is an interactive training add-on built by an assistive technology instructor for people who are just learning to use NVDA. Instead of reading a manual, students practice real NVDA commands step by step inside the add-on itself, with spoken instructions, hints, and progress tracking.

Version 1.0.0 includes 24 lessons across three chapters:
- Getting Started (10 lessons): the essential NVDA commands every beginner needs
- Reading and Moving Through Text (6 lessons): character, word, line, and selection navigation with inline practice text
- Browse Mode and Web Navigation (8 lessons): heading, link, form, and landmark navigation with a live practice web page

Features:
- Persistent Coach window with spoken step-by-step instructions
- Live practice form windows for Tab navigation and control activation lessons
- Inline practice text areas embedded directly in the lesson window
- Practice HTML web page for browse mode lessons
- Progress tracking across NVDA sessions
- Instructor-extensible: lessons are plain JSON files
- Free, open source, no internet connection required

**Category:** Training / Education
**License:** GPL v2

---

## After Your PR Is Merged

Once NV Access merges your pull request:
- NVDA Coach will appear in the NVDA Add-on Store (Tools → Add-on Store)
- Users can install it with a single click from inside NVDA
- Future updates are submitted the same way: create a new `1.0.1.json` (or `1.1.0.json`, etc.) file in a new PR

---

## Contact for Questions

NV Access GitHub: https://github.com/nvaccess/addon-store-submission/issues
Your email: info@tonygebhard.me
