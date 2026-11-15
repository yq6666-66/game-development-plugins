#!/usr/bin/env python3
"""Restricted GitHub publisher. Called only by the approval-gated workflow."""
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.request import Request, urlopen

REPO = 'yq6666-66/game-development-plugins'

def request(path, method='GET', data=None, content_type='application/json', missing=False):
    url = path if path.startswith('https://uploads.github.com/') else 'https://api.github.com/repos/' + REPO + path
    headers = {'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json',
               'Content-Type': content_type, 'X-GitHub-Api-Version': '2022-11-28'}
    body = json.dumps(data).encode() if isinstance(data, dict) else data
    try:
        with urlopen(Request(url, data=body, headers=headers, method=method), timeout=60) as response:
            return json.load(response)
    except HTTPError as exc:
        if missing and exc.code == 404:
            return None
        raise

def publish(folder, version, source, expected_digest, api=request):
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version) or version == '0.1.0':
        raise ValueError('invalid/reused release version')
    if not re.fullmatch('[0-9a-f]{40}', source):
        raise ValueError('full source SHA required')
    archive = folder / f'game-development-plugins-{version}.zip'
    if hashlib.sha256(archive.read_bytes()).hexdigest() != expected_digest:
        raise ValueError('artifact does not match approval')
    tag = 'v' + version
    if api('/git/ref/tags/' + tag, missing=True) is not None:
        raise ValueError('existing tag: never overwrite or move')
    page = 1
    while True:
        releases = api(f'/releases?per_page=100&page={page}')
        if any(r['tag_name'] == tag for r in releases):
            raise ValueError('existing release/draft: manual recovery required')
        for previous in releases:
            match = re.fullmatch(r'v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', previous['tag_name'])
            if match and not previous.get('prerelease', False) and tuple(map(int, match.groups())) >= tuple(map(int, version.split('.'))):
                raise ValueError('version must advance all existing stable releases/drafts')
        if len(releases) < 100:
            break
        page += 1
    # Atomic ref creation rejects races. Never update/delete existing refs.
    api('/git/refs', method='POST', data={'ref': 'refs/tags/' + tag, 'sha': source})
    release = api('/releases', method='POST', data={'tag_name': tag, 'target_commitish': source,
        'name': tag, 'body': (folder/'RELEASE-NOTES.md').read_text(encoding='utf-8'), 'draft': True, 'prerelease': False})
    for file in [archive, folder/'SHA256SUMS', folder/'RELEASE-NOTES.md']:
        data = file.read_bytes()
        asset = api(release['upload_url'].split('{')[0] + '?name=' + file.name,
                    method='POST', data=data, content_type='application/octet-stream')
        if asset.get('digest') != 'sha256:' + hashlib.sha256(data).hexdigest() or asset.get('size') != len(data):
            raise ValueError('server asset digest/size mismatch; draft retained')
    ref = api('/git/ref/tags/' + tag)
    if ref['object']['type'] != 'commit' or ref['object']['sha'] != source:
        raise ValueError('tag changed; refuse publication')
    result = api('/releases/' + str(release['id']), method='PATCH', data={'draft': False, 'make_latest': 'true'})
    if result['draft'] or result['tag_name'] != tag:
        raise ValueError('publication not confirmed')
    print(result['html_url'])

if __name__ == '__main__':
    if os.environ.get('GITHUB_REPOSITORY') != REPO or os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ValueError('wrong repository/ref')
    publish(Path('release-assets'), os.environ['VERSION'], os.environ['SOURCE_SHA'], os.environ['EXPECTED_DIGEST'])
