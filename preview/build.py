#!/usr/bin/env python3
"""Build local preview content from remote loops and local article fixtures."""

from __future__ import annotations

import html
import json
import os
import shutil
import subprocess
from pathlib import Path

import markdown as md_lib


ROOT = Path(__file__).resolve().parents[1]
PREVIEW_CONTENT = ROOT / "preview" / "content"


def git_show(path: str, fallback: str) -> str:
    result = subprocess.run(
        ["git", "show", f"origin/content:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return fallback
    return result.stdout


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def remove_generated_dirs(name: str, manifest: dict) -> None:
    for item in manifest.get(name, []):
        slug = item["id"]
        if slug[:4].isdigit():
            shutil.rmtree(ROOT / name / slug, ignore_errors=True)


def render_collection(
    name: str,
    manifest: dict,
    markdown_loader,
    number_token: str,
    default_summary: str,
) -> None:
    template = (ROOT / name / "_template.html").read_text(encoding="utf-8")
    remove_generated_dirs(name, manifest)

    for item in manifest.get(name, []):
        slug = item["id"]
        title = item["title"]
        summary = item.get("summary", default_summary)
        date = item["date"]
        item_num = "#" + slug.split("_")[0]
        canonical_url = f"https://laloloops.com/{name}/{slug}/"

        md = markdown_loader(item)
        body = md_lib.markdown(md, extensions=["fenced_code", "tables"])

        page = template.replace("{{TITLE}}", html.escape(title))
        page = page.replace("{{DESCRIPTION}}", html.escape(summary))
        page = page.replace("{{CANONICAL_URL}}", html.escape(canonical_url))
        page = page.replace(number_token, html.escape(item_num))
        page = page.replace("{{DATE}}", html.escape(date))
        page = page.replace("{{BODY}}", body)

        dir_path = ROOT / name / slug
        dir_path.mkdir(parents=True, exist_ok=True)
        (dir_path / "index.html").write_text(page, encoding="utf-8")
        print(f"Created {name}/{slug}/index.html")


def build_loops() -> None:
    subprocess.run(
        ["git", "fetch", "origin", "content", "--depth=1"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )

    manifest = json.loads(git_show("loops/manifest.json", '{"loops":[]}'))
    write_json(PREVIEW_CONTENT / "loops" / "manifest.json", manifest)

    render_collection(
        "loops",
        manifest,
        lambda item: git_show(f'loops/{item["file"]}', ""),
        "{{LOOP_NUM}}",
        "Dispatch from the loop.",
    )


def build_articles() -> None:
    manifest_path = PREVIEW_CONTENT / "articles" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    render_collection(
        "articles",
        manifest,
        lambda item: (PREVIEW_CONTENT / "articles" / item["file"]).read_text(encoding="utf-8"),
        "{{ARTICLE_NUM}}",
        "Longer note from the loop.",
    )


def main() -> None:
    os.chdir(ROOT)
    build_loops()
    build_articles()
    print("Local preview build complete.")


if __name__ == "__main__":
    main()
