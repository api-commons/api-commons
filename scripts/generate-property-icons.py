#!/usr/bin/env python3
"""
Generate solid-black silhouette icons for _common and _community properties
that don't yet have one in /images/{slug}.png. Style targets the existing
Font Awesome / Material Design glyph aesthetic used across the catalog.

Usage:
  python3 scripts/generate-property-icons.py          # all missing icons
  python3 scripts/generate-property-icons.py api-index  # one slug substring
"""

import os
import sys
import time
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(SITE_DIR)
IMAGES_DIR = os.path.join(SITE_DIR, 'images')


def load_api_key():
    env_path = os.path.join(ROOT_DIR, '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith('GEMINI_KEY='):
                    return line.strip().split('=', 1)[1]
    return os.environ.get('GEMINI_KEY')


# Curated single-object metaphor per slug. One concrete object only — Imagen
# composites multiple metaphors into busy grids when given a list.
METAPHORS = {
    # _common
    'api-index': 'a stack of books with a magnifying glass',
    'chargeback-policy': 'a curved arrow pointing back into a wallet',
    'console': 'a chevron-right prompt inside a rectangle (terminal cursor)',
    'deprecation-policy': 'a calendar with a single diagonal slash across it',
    'error-codes': 'a triangle exclamation warning sign',
    'faq': 'a speech bubble containing a question mark',
    'portal': 'a rectangular doorway with an arrow pointing through it',
    'release-notes': 'a clipboard with a star on it',
    'sandbox': 'a bucket and shovel',
    'signup': 'a person silhouette with a plus sign next to it',
    'tagging-policy': 'a price tag with a hole at the corner',
    'tutorials': 'a graduation cap',
    'unit-economics': 'a bar chart with a dollar coin in front',
    'website': 'a globe with latitude and longitude lines',
    # _community
    'finops-framework': 'a balance scale with coins on each side',
    'focus-billing-export': 'an arrow pointing out of a folder',
    'focus-conformance-report': 'a clipboard with a checkmark',
    'focus-contract-commitments': 'a handshake silhouette',
    'ghg-protocol-report': 'a leaf with a small ascending bar chart beside it',
    'graphql-schema': 'three connected circular nodes forming a triangle (graph)',
    'invoice-reconciliation': 'two overlapping receipts with a check between them',
    'json-structure': 'two curly braces facing each other',
    'naftiko-capability': 'an interlocking puzzle piece',
    'openapi-plugin-manifest': 'a plug being inserted into a socket',
    'opencost-allocation-api': 'a pie chart split into segments',
    'opencost-specification': 'a rolled scroll',
    'postman-collection': 'a stack of letters/envelopes bundled together',
    'postman-workspace': 'a folder with smaller folders inside it',
    'sci-report': 'a leaf with a small upward arrow',
    'software-carbon-intensity': 'a leaf inside a microchip outline',
}


def parse_fm(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith('---'):
        return {}
    end = text.find('\n---\n', 4)
    if end == -1:
        return {}
    fm = text[3:end]
    out = {}
    for key in ('name', 'description'):
        m = re.search(rf"^{key}\s*:\s*(.+?)(?=\n[a-zA-Z_]+\s*:|\n---|\Z)",
                      fm, re.MULTILINE | re.DOTALL)
        if m:
            v = m.group(1).strip()
            v = re.sub(r'\s+', ' ', v)
            if (v.startswith("'") and v.endswith("'")) or (v.startswith('"') and v.endswith('"')):
                v = v[1:-1]
            out[key] = v
    return out


def find_missing():
    missing = []
    for collection in ('_common', '_community'):
        for path in sorted(glob.glob(os.path.join(SITE_DIR, collection, '*.md'))):
            slug = os.path.splitext(os.path.basename(path))[0]
            if os.path.exists(os.path.join(IMAGES_DIR, f"{slug}.png")):
                continue
            fm = parse_fm(path)
            missing.append({
                'slug': slug,
                'name': fm.get('name', slug.replace('-', ' ').title()),
                'description': fm.get('description', '')[:300],
            })
    return missing


def generate_icon(slug, name, description, api_key):
    from google import genai
    from google.genai import types

    metaphor = METAPHORS.get(slug, f"a clean abstract glyph representing '{name}'")
    prompt = (
        f"A solid-black SVG pictogram of {metaphor}. "
        f"Style: Noun Project icon, simple flat silhouette, single centered subject. "
        f"The icon shape is drawn directly onto a pure white empty background — "
        f"there is no surrounding container, no app-icon plate, no rounded-square "
        f"backdrop, no border outline, no enclosing rectangle, no badge frame. "
        f"Just the bare icon glyph and white space around it. "
        f"Flat vector look, no gradients, no shading, no 3D, no perspective. "
        f"NO text, no letters, no words, no labels, no numbers, no writing of any kind. "
        f"Square 1:1 composition."
    )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=prompt,
        config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio='1:1'),
    )

    if not response.generated_images:
        print(f"  No image generated for: {name}")
        return False

    os.makedirs(IMAGES_DIR, exist_ok=True)
    img_path = os.path.join(IMAGES_DIR, f"{slug}.png")
    with open(img_path, 'wb') as f:
        f.write(response.generated_images[0].image.image_bytes)
    print(f"  Generated: {slug}.png")
    return True


def main():
    api_key = load_api_key()
    if not api_key:
        print("ERROR: GEMINI_KEY not found", file=sys.stderr)
        sys.exit(1)

    missing = find_missing()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if only:
        missing = [m for m in missing if only in m['slug']]
    print(f"Generating {len(missing)} icon(s)")

    for i, item in enumerate(missing, 1):
        print(f"[{i}/{len(missing)}] {item['name']} ({item['slug']})")
        try:
            generate_icon(item['slug'], item['name'], item['description'], api_key)
        except Exception as e:
            print(f"  ERROR: {e}")
        if i < len(missing):
            time.sleep(6)

    print("\nDone")


if __name__ == '__main__':
    main()
