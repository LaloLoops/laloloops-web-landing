#!/usr/bin/env python3
"""Build local preview content so the site can be browsed with real-looking
content without running the GitHub Actions deploy pipeline.

It reuses the SAME templating logic as .github/workflows/deploy.yml:
  - Loops are rendered from the remote `content` branch (git show origin/content:...)
  - Articles (and any future collection) are rendered from local fixtures under
    preview/content/<collection>/ — these never touch the content branch.

Generated detail pages (loops/<slug>/, articles/<slug>/) and everything under
preview/ are gitignored, so a preview build leaves the tracked tree clean.

Run:  python3 preview/build.py     (then serve the repo root over HTTP)
"""

from __future__ import annotations

import html
import json
import os
import shutil
import subprocess
from pathlib import Path

import markdown as md_lib

ROOT = Path(__file__).resolve().parents[1]
# Committed source fixtures (tracked, never published to the live site — see
# _config.yml exclude). Authored sample content lives here.
FIXTURES = ROOT / "preview" / "fixtures"
# Served, gitignored build output. Assembled from fetched loops + copied fixtures.
PREVIEW_CONTENT = ROOT / "preview" / "content"


def git_show(path: str, fallback: str) -> str:
    """Return the contents of a file on origin/content, or `fallback`."""
    result = subprocess.run(
        ["git", "show", f"origin/content:{path}"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    return result.stdout if result.returncode == 0 else fallback


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def render_collection(name: str, manifest: dict, markdown_loader,
                      number_token: str, default_summary: str) -> None:
    """Render every item in `manifest[name]` to <name>/<slug>/index.html using
    <name>/_template.html — mirrors the deploy.yml placeholder substitution."""
    template_path = ROOT / name / "_template.html"
    if not template_path.exists():
        print(f"[skip] {name}: no {name}/_template.html yet (nothing to render)")
        return
    template = template_path.read_text(encoding="utf-8")

    # Clean previously generated numbered dirs so removed items don't linger.
    for item in manifest.get(name, []):
        slug = item["id"]
        if slug[:4].isdigit():
            shutil.rmtree(ROOT / name / slug, ignore_errors=True)

    for item in manifest.get(name, []):
        slug = item["id"]
        body = md_lib.markdown(markdown_loader(item), extensions=["fenced_code", "tables"])
        page = template
        page = page.replace("{{TITLE}}", html.escape(item["title"]))
        page = page.replace("{{DESCRIPTION}}", html.escape(item.get("summary", default_summary)))
        page = page.replace("{{CANONICAL_URL}}", html.escape(f"https://laloloops.com/{name}/{slug}/"))
        page = page.replace(number_token, html.escape("#" + slug.split("_")[0]))
        page = page.replace("{{DATE}}", html.escape(item["date"]))
        page = page.replace("{{BODY}}", body)

        out_dir = ROOT / name / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(page, encoding="utf-8")
        print(f"Created {name}/{slug}/index.html")


def build_loops() -> None:
    subprocess.run(
        ["git", "fetch", "origin", "content", "--depth=1"],
        cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
    )
    manifest = json.loads(git_show("loops/manifest.json", '{"loops":[]}'))
    write_json(PREVIEW_CONTENT / "loops" / "manifest.json", manifest)
    render_collection(
        "loops", manifest,
        lambda item: git_show(f'loops/{item["file"]}', ""),
        "{{LOOP_NUM}}", "Dispatch from the loop.",
    )


def build_articles() -> None:
    """Render articles from committed fixtures in preview/fixtures/articles/.
    No-ops until those fixtures and an articles/_template.html both exist."""
    fixtures_dir = FIXTURES / "articles"
    manifest_path = fixtures_dir / "manifest.json"
    if not manifest_path.exists():
        print("[skip] articles: no preview/fixtures/articles/manifest.json yet")
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    # Publish the manifest to the served (gitignored) preview/content path so the
    # articles archive can fetch it on localhost.
    write_json(PREVIEW_CONTENT / "articles" / "manifest.json", manifest)
    render_collection(
        "articles", manifest,
        lambda item: (fixtures_dir / item["file"]).read_text(encoding="utf-8"),
        "{{ARTICLE_NUM}}", "Longer note from the loop.",
    )


def main() -> None:
    os.chdir(ROOT)
    build_loops()
    build_articles()
    print("Local preview build complete.")


if __name__ == "__main__":
    main()
