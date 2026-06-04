# laloloops-web-landing

Static landing page for [laloloops.com](https://laloloops.com). Hosted on GitHub Pages.

> **Disclaimer:** This project is built entirely by AI agents. No human code review has been performed. Use at your own risk.

## How it works

The site is plain HTML deployed to GitHub Pages via a GitHub Actions workflow. No frameworks.

Loop content (short dispatches/updates) and article content (longer written pieces) live on a separate **`content`** branch as markdown files. At deploy time, the workflow renders them into static HTML pages. The homepage and archive pages still fetch the manifests client-side for teasers and listings.

### Branches

| Branch | Purpose |
|---|---|
| `main` | The site: `index.html`, `404.html`, `loops/index.html`, `articles/index.html`, images |
| `content` | Content data: `loops/manifest.json`, `articles/manifest.json`, and markdown files |

The two branches are independent (orphan). They share no history.

### Pages

| URL | File | What it does |
|---|---|---|
| `/` | `index.html` | Landing page. Fetches manifests from `content` branch and shows the latest loop and latest article as teaser cards. If a fetch fails, that card stays hidden. |
| `/loops/` | `loops/index.html` | Archive page. Lists all loops from the manifest, newest first. |
| `/loops/<slug>` | `loops/<slug>/index.html` (generated) | Individual loop page. Built at deploy time from markdown on the `content` branch using Python Markdown and `loops/_template.html`. Pure HTML, no client-side JS needed. |
| `/articles/` | `articles/index.html` | Archive page. Lists all articles from the manifest, newest first. |
| `/articles/<slug>` | `articles/<slug>/index.html` (generated) | Individual article page. Built at deploy time from markdown on the `content` branch using Python Markdown and `articles/_template.html`. Pure HTML, no client-side JS needed. |

### Loop manifest

Loops are driven by `loops/manifest.json` on the `content` branch:

```json
{
  "loops": [
    {
      "id": "0001_the_first_loop",
      "title": "The First Loop",
      "summary": "Short description shown in teasers and the archive list.",
      "date": "2026-05-14",
      "file": "0001_the_first_loop.md"
    }
  ],
  "latest": "0001_the_first_loop"
}
```

- `id` — the URL slug. `laloloops.com/loops/0001_the_first_loop` renders this loop.
- `file` — the markdown filename inside `loops/` on the `content` branch.
- `latest` — which loop `id` to feature on the homepage teaser.
- `summary` — plain text shown on the homepage card and archive list (not rendered as markdown).

### Article manifest

Articles use the same pattern with `articles/manifest.json` on the `content` branch:

```json
{
  "articles": [
    {
      "id": "0001_agents_need_management",
      "title": "Agents Need Management",
      "summary": "A longer note about why agentic workflows need operating rules, not just more prompts.",
      "date": "2026-06-02",
      "file": "0001_agents_need_management.md"
    }
  ],
  "latest": "0001_agents_need_management"
}
```

- `id` — the URL slug. `laloloops.com/articles/0001_agents_need_management` renders this article.
- `file` — the markdown filename inside `articles/` on the `content` branch.
- `latest` — which article `id` to feature on the homepage teaser.
- `summary` — plain text shown on the homepage card and archive list (not rendered as markdown).

### Adding a new loop

Push to the `content` branch:

```bash
git checkout content

# write the markdown file
cat > loops/0002_shipping_things.md << 'EOF'
Content of the loop goes here. Supports full markdown.

## Subheadings work

So do lists, code blocks, links, images, blockquotes, etc.
EOF

# update the manifest — add the new entry and set it as latest
# (edit manifest.json manually or with jq/script)

git add loops/0002_shipping_things.md loops/manifest.json
git commit -m "Add loop 0002"
git push origin content
```

Pushing to the `content` branch triggers the deploy workflow, which generates a static page for the new loop and redeploys the site. No changes to `main` needed.

### Adding a new article

Push to the `content` branch:

```bash
git checkout content

# write the markdown file
cat > articles/0001_agents_need_management.md << 'EOF'
Articles use standard markdown and should not include a top-level # heading.

## The actual heading starts here

Longer article body goes here.

---

*Article #0001 — management was the missing dependency.*
EOF

# update the manifest — add the new entry and set it as latest
# (edit manifest.json manually or with jq/script)

git add articles/0001_agents_need_management.md articles/manifest.json
git commit -m "Add article 0001"
git push origin content
```

Pushing to the `content` branch triggers the deploy workflow, which generates a static page for the new article and redeploys the site. No changes to `main` needed.

### Deployment & analytics

The site is deployed by `.github/workflows/deploy.yml`. On every push to `main` or `content` (or manual dispatch), the workflow:

1. Checks out `main`
2. Fetches the loop and article manifests from the `content` branch, reads each markdown file, converts it to HTML with Python Markdown, and writes static `loops/<slug>/index.html` and `articles/<slug>/index.html` pages from their templates
3. Finds all `.html` files that don't already contain the GA4 measurement ID (`G-H6BXHR02XR`) and injects the gtag.js snippet into their `<head>`
4. Builds with Jekyll (to respect `_config.yml` excludes)
5. Deploys to GitHub Pages

Publishing a new loop or article on the `content` branch automatically triggers the workflow, which renders the markdown into a static HTML page and deploys the site. Analytics tracking is also automatic — all HTML pages, including generated content pages, get GA4 without any manual work. The source files stay clean (no gtag in the committed HTML), and the snippet is injected only at build time.

The GitHub Pages source is set to **"GitHub Actions"** (not "Deploy from branch"). If you switch it back, the site will deploy without analytics.

### Known limitations

- **Homepage and archives still use client-side JS.** The homepage teasers and `/loops/` and `/articles/` archives fetch manifests from `raw.githubusercontent.com` at page load. This content is CDN-cached for roughly 5 minutes, so there may be a short delay after publishing before teasers update. Individual generated content pages are fully static.

## Local development

Open `index.html` in a browser. The homepage content teasers require the `content` branch to be pushed to the remote because they fetch from `raw.githubusercontent.com`.

For a full local preview — rendered loop/article detail pages plus populated listings, which otherwise only exist after a CI deploy — run:

```bash
./preview.sh          # builds preview content, serves on http://localhost:8000
./preview.sh 8003     # optional custom port
```

`preview/build.py` reuses the same templating as the deploy workflow. Loops are rendered from the remote `content` branch; articles render from committed sample fixtures under `preview/fixtures/articles/`. The served output lands in `preview/content/` (gitignored), and the whole `preview/` directory is excluded from the published site via `_config.yml` — nothing in it ever reaches the live site or the `content` branch. See `preview/README.md`.

## File structure

```
main branch:
├── index.html           # Landing page + latest loop/article teasers
├── 404.html             # 404 page
├── loops/index.html     # Loop archive/listing page
├── loops/_template.html # Template for generated loop detail pages
├── articles/index.html  # Article archive/listing page
├── articles/_template.html # Template for generated article detail pages
├── avatar.png
├── header.png
├── favicon.png
├── bot_*.png            # Flying bot decorations
├── .github/workflows/
│   └── deploy.yml       # GitHub Actions: render content, inject GA4, deploy to Pages
├── _config.yml          # Jekyll config (excludes agent files + preview/)
├── CNAME                # Custom domain (laloloops.com)
├── preview/             # Local preview harness (build.py + fixtures); excluded from the live site
├── preview.sh           # Build + serve the site locally
├── AGENTS.md
└── CLAUDE.md

content branch (orphan):
├── loops/
│   ├── manifest.json
│   └── 0001_the_first_loop.md
└── articles/
    ├── manifest.json
    └── 0001_agents_need_management.md
```
