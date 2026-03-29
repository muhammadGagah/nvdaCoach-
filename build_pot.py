"""
Generate locale/nvda.pot and locale/en/LC_MESSAGES/nvda.po
from all _() strings in the add-on Python source files.
"""
import ast, os

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCE_FILES = [
    "globalPlugins/nvdaCoach/__init__.py",
    "globalPlugins/nvdaCoach/lessonRunner.py",
]

seen = set()
strings = []  # (filepath, lineno, msgid)


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

# Build PO/POT content
def escape_po(s):
    return (
        s.replace("\\", "\\\\")
         .replace('"', '\\"')
         .replace("\n", "\\n")
         .replace("\t", "\\t")
         .replace("\r", "\\r")
    )

lines = [
    "# NVDA Coach Add-on - Translation Template",
    "# Copyright (C) 2025-2026 Tony Gebhard",
    "# This file is distributed under the same license as the NVDA Coach package.",
    "#",
    "# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.",
    "#",
    "#, fuzzy",
    'msgid ""',
    'msgstr ""',
    '"Project-Id-Version: NVDA Coach 1.3\\n"',
    '"Report-Msgid-Bugs-To: info@tonygebhard.me\\n"',
    '"POT-Creation-Date: 2026-03-28 00:00+0000\\n"',
    '"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"',
    '"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"',
    '"Language-Team: LANGUAGE <LL@li.org>\\n"',
    '"Language: \\n"',
    '"MIME-Version: 1.0\\n"',
    '"Content-Type: text/plain; charset=UTF-8\\n"',
    '"Content-Transfer-Encoding: 8bit\\n"',
    "",
]

for filepath, lineno, s in strings:
    lines.append(f"#: {filepath}:{lineno}")
    lines.append(f'msgid "{escape_po(s)}"')
    lines.append('msgstr ""')
    lines.append("")

pot_content = "\n".join(lines)

# Write locale/nvda.pot (template for translators)
locale_dir = os.path.join(BASE, "locale")
os.makedirs(locale_dir, exist_ok=True)
pot_path = os.path.join(locale_dir, "nvda.pot")
with open(pot_path, "w", encoding="utf-8") as f:
    f.write(pot_content)
print(f"Wrote: locale/nvda.pot  ({len(strings)} strings)")

# Write locale/en/LC_MESSAGES/nvda.po (English base)
en_dir = os.path.join(locale_dir, "en", "LC_MESSAGES")
os.makedirs(en_dir, exist_ok=True)
po_path = os.path.join(en_dir, "nvda.po")
with open(po_path, "w", encoding="utf-8") as f:
    f.write(pot_content)
print(f"Wrote: locale/en/LC_MESSAGES/nvda.po")

print("Done.")
