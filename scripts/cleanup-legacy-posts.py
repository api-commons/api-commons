#!/usr/bin/env python3
"""
Strip legacy right-floated <img> icon tags from the body of pre-2024 HTML
posts. Those icons reference dead-feeling S3 URLs and conflict visually with
the new banner image. Front matter (including the new image: field) is
preserved exactly as-is.

Also removes the floated "api-commons-icon.png" decoration that some posts
tucked at the bottom.
"""

import os
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
POSTS_DIR = os.path.join(SITE_DIR, '_posts')


def parse_front_matter(text):
    if not text.startswith('---'):
        return None, text
    end = text.find('\n---\n', 4)
    if end == -1:
        return None, text
    return text[3:end].strip('\n'), text[end + 5:]


def clean_body(body):
    patterns = [
        r'<p>\s*<a[^>]*>\s*<img[^>]*align="right"[^>]*/?>\s*</a>\s*</p>',
        r'<p>\s*<img[^>]*align="right"[^>]*/?>\s*</p>',
        r'<a[^>]*>\s*<img[^>]*align="right"[^>]*/?>\s*</a>',
        r'<img[^>]*align="right"[^>]*/?>',
    ]
    for pat in patterns:
        body = re.sub(pat, '', body, flags=re.IGNORECASE)
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.lstrip('\n')


def process(path):
    with open(path) as f:
        text = f.read()
    fm, body = parse_front_matter(text)
    if fm is None:
        return False
    new_body = clean_body(body)
    if new_body == body:
        return False
    with open(path, 'w') as f:
        f.write('---\n' + fm.strip('\n') + '\n---\n' + new_body)
    return True


def main():
    changed = 0
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, '*.html'))):
        if process(path):
            print(f"cleaned: {os.path.basename(path)}")
            changed += 1
    print(f"\n{changed} files cleaned")


if __name__ == '__main__':
    main()
