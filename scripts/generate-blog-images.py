#!/usr/bin/env python3
"""
Generate black and white blog post banners for the api-commons blog using
Google Gemini Imagen. Matches the visual style used on apis.io.

Always regenerates — meant to be run when you want a consistent style across
every post. Drop the --skip-existing flag in if you want incremental behavior.
"""

import os
import sys
import time
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(SITE_DIR)
POSTS_DIR = os.path.join(SITE_DIR, '_posts')
IMAGES_DIR = os.path.join(SITE_DIR, 'assets', 'images', 'blog')


def load_api_key():
    # Walk up from the site dir looking for a .env with GEMINI_KEY; the commons
    # repos live one level below the GitHub root that holds the shared .env.
    for d in (ROOT_DIR, os.path.dirname(ROOT_DIR)):
        env_path = os.path.join(d, '.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.startswith('GEMINI_KEY='):
                        return line.strip().split('=', 1)[1]
    return os.environ.get('GEMINI_KEY')


def parse_front_matter(text):
    if not text.startswith('---'):
        return None, text
    end = text.find('\n---\n', 4)
    if end == -1:
        end = text.find('\r\n---\r\n', 4)
        if end == -1:
            return None, text
        body = text[end + 7:]
    else:
        body = text[end + 5:]
    fm = text[3:end].strip('\n')
    return fm, body


def get_field(fm_text, key):
    """Pull a single top-level field from front-matter text without YAML.
    Posts use a mix of quoted/unquoted scalars; YAML would also choke on some
    of the legacy entries. Simple regex is enough here."""
    m = re.search(rf"^{re.escape(key)}\s*:\s*(.+)$", fm_text, re.MULTILINE)
    if not m:
        return ''
    v = m.group(1).strip()
    if (v.startswith("'") and v.endswith("'")) or (v.startswith('"') and v.endswith('"')):
        v = v[1:-1]
    return v


def get_tags(fm_text):
    m = re.search(r"^tags\s*:\s*\[(.+)\]", fm_text, re.MULTILINE)
    if m:
        return [t.strip().strip("'\"") for t in m.group(1).split(',') if t.strip()]
    m = re.search(r"^tags\s*:\s*\n((?:\s*-\s*.+\n?)+)", fm_text, re.MULTILINE)
    if m:
        return [line.strip().lstrip('-').strip().strip("'\"")
                for line in m.group(1).splitlines() if line.strip()]
    return []


def get_posts():
    posts = []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, '*'))):
        if not (path.endswith('.md') or path.endswith('.html')):
            continue
        with open(path) as f:
            content = f.read()
        fm, body = parse_front_matter(content)
        if fm is None:
            continue
        slug = os.path.splitext(os.path.basename(path))[0]
        image_slug = slug[11:] if re.match(r'\d{4}-\d{2}-\d{2}-', slug) else slug
        posts.append({
            'file': path,
            'slug': slug,
            'image_slug': image_slug,
            'title': get_field(fm, 'title'),
            'tags': get_tags(fm),
            'fm_text': fm,
            'body': body,
        })
    return posts


def generate_image(title, tags, image_slug, api_key):
    from google import genai
    from google.genai import types

    tag_str = ', '.join(tags[:4]) if tags else 'API Commons, open source, API specifications'

    prompt = (
        f"A striking black and white editorial illustration for a blog post titled '{title}'. "
        f"Themes: {tag_str}. "
        f"Abstract, minimalist composition with clean geometric shapes and high contrast. "
        f"Think ink illustration style - bold blacks, crisp whites, no gray midtones. "
        f"Conceptual and evocative, suitable as a wide banner image. "
        f"No text, no words, no letters, no logos."
    )

    client = genai.Client(api_key=api_key)
    response = client.models.generate_images(
        model='imagen-4.0-generate-001',
        prompt=prompt,
        config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio='16:9'),
    )

    if not response.generated_images:
        print(f"  No image generated for: {title}")
        return False

    os.makedirs(IMAGES_DIR, exist_ok=True)
    img_path = os.path.join(IMAGES_DIR, f"{image_slug}.png")
    with open(img_path, 'wb') as f:
        f.write(response.generated_images[0].image.image_bytes)
    print(f"  Generated: {image_slug}.png")
    return True


def update_post_image(filepath, fm_text, body, new_image_path):
    """Set image: field in front matter, preserving everything else verbatim."""
    if re.search(r"^image\s*:.*$", fm_text, re.MULTILINE):
        new_fm = re.sub(r"^image\s*:.*$",
                        f"image: {new_image_path}",
                        fm_text, count=1, flags=re.MULTILINE)
    else:
        new_fm = fm_text.rstrip() + f"\nimage: {new_image_path}"

    with open(filepath, 'w') as f:
        f.write('---\n')
        f.write(new_fm.strip('\n') + '\n')
        f.write('---\n')
        f.write(body)


def main():
    api_key = load_api_key()
    if not api_key:
        print("ERROR: GEMINI_KEY not found in .env or environment", file=sys.stderr)
        sys.exit(1)

    only = sys.argv[1] if len(sys.argv) > 1 else None
    skip_existing = '--skip-existing' in sys.argv

    posts = get_posts()
    if only:
        posts = [p for p in posts if only in p['slug']]
    print(f"Found {len(posts)} post(s) to process")

    for i, post in enumerate(posts, 1):
        image_path = os.path.join(IMAGES_DIR, f"{post['image_slug']}.png")
        new_image = f"/assets/images/blog/{post['image_slug']}.png"

        if skip_existing and os.path.exists(image_path):
            print(f"[{i}/{len(posts)}] Skipping (exists): {post['image_slug']}")
            continue

        print(f"[{i}/{len(posts)}] {post['title']}")
        try:
            ok = generate_image(post['title'], post['tags'], post['image_slug'], api_key)
        except Exception as e:
            print(f"  ERROR: {e}")
            ok = False

        if ok:
            update_post_image(post['file'], post['fm_text'], post['body'], new_image)
            print(f"  Updated front matter")

        if i < len(posts):
            time.sleep(6)

    print("\nDone")


if __name__ == '__main__':
    main()
