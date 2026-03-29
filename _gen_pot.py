"""
Generate locale/nvda.pot and locale/en/LC_MESSAGES/nvda.po
from all _() strings in the NVDA Coach plugin files.
"""
import ast, os

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCE_FILES = [
    "globalPlugins/nvdaCoach/__init__.py",
    "globalPlugins/nvdaCoach/lessonRunner.py",
]

seen = set()
strings = []  # (filepath_relative, lineno, msgid)

class Visitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
    def visit_Call(self, node):
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "_"
            and len(node.args) == 1
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
        ):
            s = node.args[0].value
            if s and s not in seen:
                seen.add(s)
                strings.append((self.filename, node.lineno, s))
        self.generic_visit(node)

for rel in SOURCE_FILES:
    path = os.path.join(BASE, rel)
    with open(path, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    Visitor(rel).visit(tree)

print(f"Extracted {len(strings)} unique translatable strings.")

# ── helpers ──────────────────────────────────────────────────────────────────

def po_escape(s):
    """Escape a Python string for use as a PO msgid / msgstr value."""
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    s = s.replace("\n", "\\n")
    s = s.replace("\r", "\\r")
    s = s.replace("\t", "\\t")
    return s

def build_pot(strings, revision_date="2026-03-28 00:00+0000"):
    lines = []
    lines += [
        "# NVDA Coach Add-on — Translation Template",
        "# Copyright (C) 2025-2026 Tony Gebhard <info@tonygebhard.me>",
        "# This file is distributed under the same license as the NVDA Coach package.",
        "#",
        "# Translators:",
        "#   FIRST AUTHOR <EMAIL@ADDRESS>, YEAR",
        "#",
        "#, fuzzy",
        'msgid ""',
        'msgstr ""',
        '"Project-Id-Version: NVDA Coach 1.3\\n"',
        '"Report-Msgid-Bugs-To: info@tonygebhard.me\\n"',
        f'"POT-Creation-Date: {revision_date}\\n"',
        '"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"',
        '"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"',
        '"Language-Team: LANGUAGE <LL@li.org>\\n"',
        '"Language: \\n"',
        '"MIME-Version: 1.0\\n"',
        '"Content-Type: text/plain; charset=UTF-8\\n"',
        '"Content-Transfer-Encoding: 8bit\\n"',
        '"Plural-Forms: nplurals=2; plural=(n != 1);\\n"',
        "",
    ]
    for (filepath, lineno, s) in strings:
        lines.append(f"#: {filepath}:{lineno}")
        lines.append(f'msgid "{po_escape(s)}"')
        lines.append('msgstr ""')
        lines.append("")
    return "\n".join(lines)

pot_content = build_pot(strings)

# ── write files ───────────────────────────────────────────────────────────────

locale_root = os.path.join(BASE, "locale")
en_lc = os.path.join(locale_root, "en", "LC_MESSAGES")
os.makedirs(en_lc, exist_ok=True)

pot_path = os.path.join(locale_root, "nvda.pot")
with open(pot_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(pot_content)
print(f"Wrote: locale/nvda.pot  ({os.path.getsize(pot_path):,} bytes)")

po_path = os.path.join(en_lc, "nvda.po")
with open(po_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(pot_content)
print(f"Wrote: locale/en/LC_MESSAGES/nvda.po  ({os.path.getsize(po_path):,} bytes)")

print("Done.")
