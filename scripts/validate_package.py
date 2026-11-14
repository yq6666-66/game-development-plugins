#!/usr/bin/env python3
"""Validate local skill packaging; no network, writes, or game execution."""
from pathlib import Path
import re
import sys

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
REFERENCE = re.compile(r"\[([^\]\n]+)\]\[([^\]\n]*)\]")
DEFINITION = re.compile(r'^ {0,3}\[([^\]\n]+)\]:[ \t]*(?:<([^>\n]+)>|(\S+))[ \t]*$', re.M)

def markdown_targets(content: str) -> tuple[list[str], list[str]]:
    """Supported subset: inline, explicit/collapsed and defined shortcut references.

    Ignore fenced and inline code examples. This is not a CommonMark parser;
    titles, multiline destinations and fragment validity are outside this check.
    """
    lines, fence = [], None
    for line in content.splitlines():
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            continue
        if match:
            fence = match[1]
            continue
        lines.append(line)
    # Mask escaped syntax with parity preserved: two backslashes leave a real
    # opening bracket; one or three escape it. Do not unescape destinations.
    text = re.sub(r'\\([\\\[\]`])', lambda m: ' ' * len(m[0]), '\n'.join(lines))
    # Equal-length backtick runs delimit code spans, including across lines.
    # A longer run is not a closing delimiter for a shorter opener.
    text = re.sub(r'(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)' ,
                  lambda m: '\n' * m[0].count('\n'), text, flags=re.S)
    normalize = lambda label: ' '.join(label.split()).casefold()
    definitions, errors = {}, []
    for match in DEFINITION.finditer(text):
        key = normalize(match[1])
        if key in definitions:
            errors.append(f'duplicate reference definition: {match[1]}')
        else:
            definitions[key] = match[2] or match[3]
    text = DEFINITION.sub('', text)
    targets = LINK.findall(text)
    for match in REFERENCE.finditer(text):
        label = match[2] or match[1]
        key = normalize(label)
        if key not in definitions:
            errors.append(f'undefined reference label: {label}')
        else:
            targets.append(definitions[key])
    # A bare [label] is a link only when this document defines that label.
    remaining = REFERENCE.sub('', LINK.sub('', text))
    for label in re.findall(r'\[([^\]\n]+)\]', remaining):
        key = normalize(label)
        if key in definitions:
            targets.append(definitions[key])
    return targets, errors

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
            targets, reference_errors = markdown_targets(content)
            errors.extend(f'{file.relative_to(root)}: {error}' for error in reference_errors)
            for link in targets:
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
