#!/usr/bin/env python3
"""Build deterministic, allowlisted skill-only archives; never install or publish."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import zipfile

SKILLS = {'game-engineering', 'game-ui-design', 'game-build-delivery', 'game-resource-selection', 'game-prototype-planning', 'game-visual-iteration', 'game-playloop-validation'}
FILES = ['plugin.json', '.claude-plugin/plugin.json', '.claude-plugin/marketplace.json', '.agents/plugins/marketplace.json', 'LICENSE', 'PLUGIN-README.md', 'PLUGIN-README.en.md', 'scripts/validate_package.py']

def payload(root):
    return sorted([root/p for p in FILES] + [p for p in (root/'skills').rglob('*') if p.is_file() and p.suffix in {'.md', '.yaml', '.json'}])

def validate(root):
    errors=[]
    for path in FILES:
        if not (root/path).is_file(): errors.append(f'missing {path}')
    for path in (root/'skills').rglob('*'):
        if path.is_symlink(): errors.append(f'symlink not allowed: {path.relative_to(root)}')
    for path in FILES:
        if (root/path).is_symlink(): errors.append(f'symlink not allowed: {path}')
    names={p.name for p in (root/'skills').iterdir() if p.is_dir()} if (root/'skills').is_dir() else set()
    if names != SKILLS: errors.append('skill inventory mismatch')
    if errors: return errors
    try:
        portable=json.loads((root/'plugin.json').read_text(encoding='utf-8'))
        claude=json.loads((root/'.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        for key in ('name','version','description','license'):
            if portable.get(key) != claude.get(key): errors.append(f'manifest mismatch: {key}')
        if portable.get('name') != 'game-development-plugins': errors.append('unexpected plugin name')
        if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?',portable.get('version','')): errors.append('invalid version')
        for manifest in (portable,claude):
            if set(manifest)-{'$schema','name','version','description','author','homepage','repository','license'}: errors.append('unexpected manifest field/component')
        for path in ('.claude-plugin/marketplace.json','.agents/plugins/marketplace.json'):
            market=json.loads((root/path).read_text(encoding='utf-8')); entries=market.get('plugins',[])
            if market.get('name')!=portable['name'] or len(entries)!=1 or entries[0].get('name')!=portable['name']: errors.append('marketplace identity mismatch')
            elif entries[0].get('source') != ('./' if path.startswith('.claude-plugin/') else {'source':'local','path':'./'}): errors.append('marketplace must target local root using host-specific source shape')
    except (ValueError,KeyError,TypeError) as exc: errors.append(f'invalid JSON manifest: {exc}')
    spec=importlib.util.spec_from_file_location('skill_validator',root/'scripts/validate_package.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    errors.extend(mod.validate(root))
    return errors

def build(root, output):
    errors=validate(root)
    if errors: raise ValueError('\n'.join(errors))
    # No overwrite: callers must deliberately choose a fresh artifact filename.
    with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_DEFLATED) as archive:
        for path in payload(root):
            info=zipfile.ZipInfo(path.relative_to(root).as_posix(),(1980,1,1,0,0,0))
            info.external_attr=0o100644 << 16
            info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,path.read_bytes())
    return hashlib.sha256(output.read_bytes()).hexdigest()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true');parser.add_argument('--output',type=Path)
    args=parser.parse_args();root=Path(__file__).resolve().parents[1]
    errors=validate(root)
    if errors: parser.exit(1,'\n'.join(errors)+'\n')
    if args.output: print(build(root,args.output),args.output)
    else: print('PASS: dual-host distribution structure (not host runtime verification)')
