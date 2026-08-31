#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
IGNORE_DIRS = {'.git'}


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs: list[tuple[str, str]] = []
        self.has_title = False
        self.has_description = False
        self.has_viewport = False
        self.has_main = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title':
            self.has_title = True
        if tag == 'meta':
            if attrs.get('name') == 'description' and attrs.get('content'):
                self.has_description = True
            if attrs.get('name') == 'viewport' and attrs.get('content'):
                self.has_viewport = True
        if tag == 'main':
            self.has_main = True
        if tag in {'a', 'link'} and attrs.get('href'):
            self.refs.append((tag, attrs['href']))
        if tag in {'img', 'script', 'source'} and attrs.get('src'):
            self.refs.append((tag, attrs['src']))


def local_target(source: Path, raw: str) -> Path | None:
    value = raw.strip()
    if not value or value.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:')):
        return None
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        return None
    path = parsed.path
    if not path:
        return None
    if path.startswith('/'):
        target = ROOT / path.lstrip('/')
    else:
        target = source.parent / path
    if path.endswith('/'):
        target = target / 'index.html'
    elif not target.suffix and not target.exists():
        candidate = target / 'index.html'
        if candidate.exists():
            target = candidate
    return target.resolve()


def audit_html() -> list[str]:
    errors: list[str] = []
    html_files = sorted(ROOT.rglob('*.html'))
    for page in html_files:
        if any(part in IGNORE_DIRS for part in page.parts):
            continue
        parser = Collector()
        try:
            parser.feed(page.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'{page.relative_to(ROOT)}: could not parse HTML: {exc}')
            continue
        label = page.relative_to(ROOT)
        if not parser.has_title:
            errors.append(f'{label}: missing <title>')
        if page.name != '404.html' and not parser.has_description:
            errors.append(f'{label}: missing meta description')
        if not parser.has_viewport:
            errors.append(f'{label}: missing viewport meta')
        if not parser.has_main:
            errors.append(f'{label}: missing <main> landmark')
        for tag, ref in parser.refs:
            target = local_target(page, ref)
            if target is None:
                continue
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f'{label}: {tag} reference escapes repository: {ref}')
                continue
            if not target.exists():
                errors.append(f'{label}: broken {tag} reference: {ref}')
    return errors


def duplicate_assets() -> list[str]:
    groups: dict[tuple[int, str], list[Path]] = {}
    for folder in ('images',):
        base = ROOT / folder
        if not base.exists():
            continue
        for path in base.rglob('*'):
            if not path.is_file():
                continue
            data = path.read_bytes()
            key = (len(data), hashlib.sha256(data).hexdigest())
            groups.setdefault(key, []).append(path)
    notes = []
    for (size, _), paths in groups.items():
        if len(paths) > 1:
            names = ', '.join(str(p.relative_to(ROOT)) for p in paths)
            notes.append(f'duplicate asset ({size} bytes): {names}')
    return notes


def main() -> int:
    errors = audit_html()
    notes = duplicate_assets()
    print(f'Audited static site at {ROOT}')
    for note in notes:
        print(f'NOTICE: {note}')
    if errors:
        print('\nFAILURES:')
        for error in errors:
            print(f'- {error}')
        return 1
    print('\nPASS: no broken local references or required HTML metadata failures found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
