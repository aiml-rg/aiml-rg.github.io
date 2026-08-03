#!/usr/bin/env python3
"""Checks the site for the things that actually break it.

Run it before opening a pull request:

    python3 .github/scripts/check_site.py

It is the same script the pull-request check runs, so if it passes here it
passes there. No dependencies; Python 3 is enough.
"""

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'source', 'track', 'wbr'}
MAX_IMAGE_KB = 1500

problems = []
notes = []


def fail(where, message):
    problems.append(f"{where}: {message}")


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '.github')]
        for name in filenames:
            if name.endswith('.html'):
                full = os.path.join(dirpath, name)
                yield os.path.relpath(full, ROOT), full


class Balance(HTMLParser):
    """Catches an unclosed or mismatched tag, which is what usually turns a
       small edit into a page that renders as a wall of nothing."""

    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"line {self.getpos()[0]}: stray </{tag}>")
            return
        open_tag, line = self.stack.pop()
        if open_tag != tag:
            self.errors.append(
                f"line {self.getpos()[0]}: </{tag}> closes <{open_tag}> "
                f"opened on line {line}")


def target_for(url):
    """Where a root-relative URL has to exist on disk."""
    path = url.split('#')[0].split('?')[0]
    if path in ('', '/'):
        return os.path.join(ROOT, 'index.html')
    path = path.lstrip('/')
    if path.endswith('/'):
        return os.path.join(ROOT, path, 'index.html')
    return os.path.join(ROOT, path)


LINK = re.compile(r'(?:href|src)="([^"]+)"')

for rel, full in sorted(pages()):
    text = open(full, encoding='utf-8').read()

    checker = Balance()
    checker.feed(text)
    for err in checker.errors:
        fail(rel, err)
    for tag, line in checker.stack:
        fail(rel, f"line {line}: <{tag}> is never closed")

    for url in LINK.findall(text):
        if url.startswith(('http://', 'https://', 'mailto:', 'data:', '#')):
            continue

        # Every path on this site is root-relative. A missing leading slash
        # works on the page you tested and breaks on every other one.
        if not url.startswith('/'):
            fail(rel, f'"{url}" is missing its leading slash')
            continue

        if not os.path.exists(target_for(url)):
            fail(rel, f'"{url}" does not exist')

        # Pages are served from directories, so a .html link is a stale one.
        if url.endswith('.html') and '/assets/' not in url:
            notes.append(f"{rel}: \"{url}\" should be a directory URL")

for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, 'assets')):
    for name in filenames:
        if not name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
            continue
        full = os.path.join(dirpath, name)
        kb = os.path.getsize(full) // 1024
        if kb > MAX_IMAGE_KB:
            fail(os.path.relpath(full, ROOT),
                 f"{kb} KB, over the {MAX_IMAGE_KB} KB limit. Resize it, or "
                 f"export it again at a lower quality.")

for note in notes:
    print(f"note    {note}")

if problems:
    print()
    for problem in problems:
        print(f"PROBLEM {problem}")
    print(f"\n{len(problems)} problem(s). The site would be broken; "
          f"fix these before merging.")
    sys.exit(1)

count = len(list(pages()))
print(f"\nOK: {count} pages, every link and asset resolves.")
