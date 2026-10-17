# M Blog

A static blog built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).  
Supports **public posts** (blog index + RSS feed) and **unlisted posts** (UUID URLs, no listing, direct link only).

## Quick Start

```bash
pip install -r requirements.txt
mkdocs serve        # local preview at http://127.0.0.1:8000
```

## Creating Posts

```bash
# Public blog post (appears on index + RSS feed)
make new-post

# Unlisted post (UUID slug, accessible only by direct link)
make new-unlisted
```

Or use the script directly:

```bash
python scripts/new_post.py --title "My Post"
python scripts/new_post.py --title "Secret Note" --unlisted
```

## Build & Deploy

```bash
mkdocs build                                       # outputs to site/
```

Pushes to `main` build the site and deploy it to GitHub Pages:

<https://thenotary.github.io/m-blog>
