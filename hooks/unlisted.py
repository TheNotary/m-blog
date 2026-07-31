"""MkDocs hook: exclude unlisted pages from sitemap and inject noindex meta."""

import logging

log = logging.getLogger("mkdocs.hooks.unlisted")

UNLISTED_PREFIX = "p/"


def _is_unlisted(page) -> bool:
    """Check if a page lives under the unlisted directory."""
    return page.file.src_path.startswith(UNLISTED_PREFIX)


def on_page_context(context, page, config, nav, **kwargs):
    """Inject noindex and search exclusion for unlisted pages."""
    if _is_unlisted(page):
        page.meta["robots"] = "noindex, nofollow"
        page.meta["unlisted"] = True
        # Ensure search exclusion even if not set in frontmatter
        page.meta.setdefault("search", {})
        if isinstance(page.meta["search"], dict):
            page.meta["search"]["exclude"] = True
    return context


def on_post_build(config, **kwargs):
    """Remove unlisted pages from the generated sitemap.xml."""
    import xml.etree.ElementTree as ET
    from pathlib import Path

    site_dir = Path(config["site_dir"])
    sitemap_path = site_dir / "sitemap.xml"
    if not sitemap_path.exists():
        return

    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    site_url = config["site_url"].rstrip("/")
    unlisted_url_prefix = f"{site_url}/{UNLISTED_PREFIX}"

    to_remove = []
    for url_elem in root.findall(f"{{{ns}}}url"):
        loc = url_elem.find(f"{{{ns}}}loc")
        if loc is not None and loc.text and loc.text.startswith(unlisted_url_prefix):
            to_remove.append(url_elem)

    for elem in to_remove:
        root.remove(elem)
        log.info("Removed unlisted page from sitemap: %s", elem.find(f"{{{ns}}}loc").text)

    tree.write(sitemap_path, xml_declaration=True, encoding="UTF-8")
