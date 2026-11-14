#!/usr/bin/env python3
"""Validate local skill packaging; no network, writes, or game execution."""
from pathlib import Path
import re
import sys

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

def validate(root: Path) -> list[str]:
    errors = []
    folders = sorted(p for p in (root / 'skills').glob('*') if p.is_dir())
    if not folders:
        return ['no skill folders found']
    names = set()
    for folder in folders:
        entry = folder / 'SKILL.md'
        if not entry.is_file():
            errors.append(f'{folder.name}: missing SKILL.md'); continue
        data = entry.read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', data, re.S)
        if not match:
            errors.append(f'{folder.name}: missing YAML frontmatter'); continue
        fields = dict(re.findall(r'^([a-z_-]+):\s*(.+)$', match[1], re.M))
        name = fields.get('name', '')
        if not NAME.fullmatch(name) or name != folder.name:
            errors.append(f'{folder.name}: invalid or mismatched name')
        if name in names: errors.append(f'{folder.name}: duplicate name')
        names.add(name)
        if not fields.get('description', '').strip():
            errors.append(f'{folder.name}: missing description')
        for file in folder.rglob('*.md'):
            content = file.read_text(encoding='utf-8')
            if re.search(r'\[TODO:|\[Insert |\[Replace ', content):
                errors.append(f'{file.relative_to(root)}: unfinished scaffold')
            for link in LINK.findall(content):
                target = link.split('#', 1)[0]
                if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                resolved = (file.parent / target).resolve()
                if not resolved.is_relative_to(folder.resolve()):
                    errors.append(f'{file.relative_to(root)}: reference escapes portable skill: {target}')
                elif not resolved.exists():
                    errors.append(f'{file.relative_to(root)}: missing reference: {target}')
    return errors

if __name__ == '__main__':
    errors = validate(Path(__file__).resolve().parents[1])
    for item in errors: print('FAIL:', item)
    print('FAIL' if errors else 'PASS: local skill package checks')
    sys.exit(bool(errors))
