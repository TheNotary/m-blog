#!/usr/bin/env python3
"""Create a new blog post (public or unlisted).

Usage:
    python scripts/new_post.py --title "My Post Title"
    python scripts/new_post.py --title "Secret Note" --unlisted
"""

import argparse
import re
import uuid
from datetime import date
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
BLOG_POSTS_DIR = DOCS_DIR / "blog" / "posts"
UNLISTED_DIR = DOCS_DIR / "p"

PUBLIC_TEMPLATE = """\
---
date: {date}
slug: {slug}
draft: true
---

# {title}

Write your post here.

<!-- more -->

Continue the longer article below the fold.
"""

UNLISTED_TEMPLATE = """\
---
date: {date}
search:
  exclude: true
---

# {title}

Write your post here.
"""


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def create_public_post(title: str) -> Path:
    BLOG_POSTS_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    slug = slugify(title)
    filename = f"{today}-{slug}.md"
    filepath = BLOG_POSTS_DIR / filename
    filepath.write_text(PUBLIC_TEMPLATE.format(date=today, slug=slug, title=title))
    return filepath


def create_unlisted_post(title: str) -> Path:
    UNLISTED_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    post_uuid = str(uuid.uuid4())
    filename = f"{post_uuid}.md"
    filepath = UNLISTED_DIR / filename
    filepath.write_text(UNLISTED_TEMPLATE.format(date=today, title=title))
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Create a new blog post.")
    parser.add_argument("--title", required=True, help="Post title")
    parser.add_argument(
        "--unlisted",
        action="store_true",
        help="Create an unlisted post with a UUID slug",
    )
    args = parser.parse_args()

    if args.unlisted:
        path = create_unlisted_post(args.title)
        rel = path.relative_to(DOCS_DIR)
        # The URL path: /p/<uuid>/
        url_path = f"/p/{path.stem}/"
        print(f"Created unlisted post: {path}")
        print(f"URL path:             {url_path}")
    else:
        path = create_public_post(args.title)
        print(f"Created public post:  {path}")
        print(f"NOTE: draft is set to true — flip to false when ready to publish.")


if __name__ == "__main__":
    main()
