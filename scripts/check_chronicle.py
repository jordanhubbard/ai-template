#!/usr/bin/env python3
"""Check chapter order, actual README headings, and reciprocal navigation."""
import argparse
import base64
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def github_readme(chapter):
    endpoint = f"repos/jordanhubbard/{chapter['name']}/contents/{chapter['readme']}"
    result = subprocess.run(
        ['gh', 'api', endpoint], check=True, capture_output=True, text=True
    )
    return base64.b64decode(json.loads(result.stdout)['content']).decode('utf-8')


def headings(text):
    """Read ATX headings outside fenced code; chapter titles use plain text."""
    fence = None
    result = []
    for line in text.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            match = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*$', line)
            if match:
                result.append(match[1])
    return result


def check(manifest, read):
    chapters = manifest['chapters']
    if not chapters:
        raise ValueError('Chronicle has no chapters')
    names = [chapter['name'] for chapter in chapters]
    if len(set(names)) != len(names):
        raise ValueError('Duplicate repository in chronicle')
    order = [
        (datetime.datetime.fromisoformat(c['first_ai']['date']), c['name'])
        for c in chapters
    ]
    if order != sorted(order):
        raise ValueError('Chapters are not in first-AI-commit order')
    texts = {}
    for i, chapter in enumerate(chapters, 1):
        name = chapter['name']
        if chapter['part'] != i:
            raise ValueError(f'{name}: expected part {i}')
        text = read(chapter)
        texts[name] = text
        titles = headings(text)
        if titles.count(chapter['heading']) != 1:
            raise ValueError(f'{name}: chapter heading missing or duplicated')
        anchor = re.sub(r'[^\w\- ]', '', chapter['heading'].lower()).replace(' ', '-')
        url = f'https://github.com/jordanhubbard/{name}#{anchor}'
        if chapter['anchor'] != anchor or chapter['chapter_url'] != url:
            raise ValueError(f'{name}: heading and chapter URL disagree')
        links = []
        if i > 1:
            prev = chapters[i - 2]
            links.append(f'[← Part {i - 1}: {prev["label"]}]({prev["chapter_url"]})')
        if i < len(chapters):
            nxt = chapters[i]
            links.append(f'[Part {i + 1}: {nxt["label"]} →]({nxt["chapter_url"]})')
        expected = f'> *Part {i} of an ongoing chronicle. ' + ' | '.join(links) + '*'
        actual = re.findall(r'^> \*Part \d+ of an ongoing chronicle\..*$', text, re.M)
        if actual != [expected]:
            raise ValueError(f'{name}: missing, duplicate, or incorrect neighbor links')
    return texts


def verify_preservation(chapter, text, repos_dir):
    repo = repos_dir / chapter['name']
    old_bytes = subprocess.run(
        ['git', 'show', f'{chapter["base_sha"]}:{chapter["readme"]}'],
        cwd=repo, check=True, capture_output=True,
    ).stdout
    if hashlib.sha256(old_bytes).hexdigest() != chapter['original_sha256']:
        raise ValueError(f'{chapter["name"]}: original README hash mismatch')
    if hashlib.sha256(text.encode()).hexdigest() != chapter['updated_sha256']:
        raise ValueError(f'{chapter["name"]}: README differs from audited retrofit')
    old = old_bytes.decode('utf-8')
    if not chapter['existing']:
        stripped, count = re.subn(
            r'<!-- ai-template:narrative:start -->\n.*?'
            r'<!-- ai-template:narrative:end -->\n(?:\n)?', '', text, flags=re.S,
        )
        # A README ending with one newline needs a blank separator before
        # an appended heading; no other original bytes may change.
        appended_separator = (
            old.endswith('\n') and not old.endswith('\n\n')
            and text.startswith(old + '\n<!-- ai-template:narrative:start -->')
            and stripped == old + '\n'
        )
        if count != 1 or (stripped != old and not appended_separator):
            raise ValueError(f'{chapter["name"]}: content outside addition changed')
    else:
        heading = '## ' + chapter['heading']
        def outside(value):
            start = value.index(heading)
            end = value.find('\n## ', start + len(heading))
            return value[:start], value[end:] if end >= 0 else ''
        if outside(old) != outside(text):
            raise ValueError(f'{chapter["name"]}: content outside story changed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path,
                        default=Path(__file__).resolve().parents[1] / 'chronicle.json')
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--repos-dir', type=Path, help='Directory containing named clones')
    source.add_argument('--github', action='store_true', help='Read live default branches via gh')
    parser.add_argument('--verify-retrofit', action='store_true',
                        help='Compare local README files to audited base commits and hashes')
    args = parser.parse_args()
    if args.verify_retrofit and not args.repos_dir:
        parser.error('--verify-retrofit requires --repos-dir')
    manifest = json.loads(args.manifest.read_text())
    read = github_readme if args.github else lambda c: (
        args.repos_dir / c['name'] / c['readme']
    ).read_bytes().decode('utf-8')
    try:
        texts = check(manifest, read)
        if args.verify_retrofit:
            for chapter in manifest['chapters']:
                verify_preservation(chapter, texts[chapter['name']], args.repos_dir)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        return 1
    print(f'PASS: {len(texts)} chapters in chronological order; all headings and neighbor links match.')
    if args.verify_retrofit:
        print('PASS: audited hashes match; original content outside narrative edits is unchanged.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
