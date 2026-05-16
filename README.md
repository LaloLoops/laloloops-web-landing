# laloloops-web-landing

Static landing page for [laloloops.com](https://laloloops.com). Hosted on GitHub Pages.

> **Disclaimer:** This project is built entirely by AI agents. No human code review has been performed. Use at your own risk.

## How it works

The site is plain HTML deployed to GitHub Pages via a GitHub Actions workflow. No frameworks.

Loop content (short dispatches/updates) lives on a separate **`content`** branch as markdown files. At deploy time, the workflow renders them into static HTML pages. The homepage and archive page still fetch the manifest client-side for teasers and listing.

### Branches

| Branch | Purpose |
|---|---|
| `main` | The site: `index.html`, `404.html`, `loops/index.html`, images |
| `content` | Loop data: `loops/manifest.json` + markdown files |

The two branches are independent (orphan). They share no history.

### Pages

| URL | File | What it does |
|---|---|---|
| `/` | `index.html` | Landing page. Fetches `manifest.json` from `content` branch and shows the latest loop as a teaser card. If the fetch fails, the card stays hidden. |
| `/loops/` | `loops/index.html` | Archive page. Lists all loops from the manifest, newest first. |
| `/loops/<slug>` | `loops/<slug>/index.html` (generated) | Individual loop page. Built at deploy time from the markdown on the `content` branch using `pandoc` and a template (`loops/_template.html`). Pure HTML, no client-side JS needed. If someone hits a slug that doesn't exist, `404.html` shows a not-found message. |

### The manifest

Everything is driven by `loops/manifest.json` on the `content` branch:

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

### Deployment & analytics

The site is deployed by `.github/workflows/deploy.yml`. On every push to `main` or `content` (or manual dispatch), the workflow:

1. Checks out `main`
2. Fetches the manifest from the `content` branch, reads each loop's markdown, converts it to HTML with `pandoc`, and writes a static `loops/<slug>/index.html` from the template
3. Finds all `.html` files that don't already contain the GA4 measurement ID (`G-H6BXHR02XR`) and injects the gtag.js snippet into their `<head>`
4. Builds with Jekyll (to respect `_config.yml` excludes)
5. Deploys to GitHub Pages

Publishing a new loop on the `content` branch automatically triggers the workflow, which renders the markdown into a static HTML page and deploys the site. Analytics tracking is also automatic — all HTML pages (including the generated loop pages) get GA4 without any manual work. The source files stay clean (no gtag in the committed HTML), and the snippet is injected only at build time.

The GitHub Pages source is set to **"GitHub Actions"** (not "Deploy from branch"). If you switch it back, the site will deploy without analytics.

### Known limitations

- **Homepage and archive still use client-side JS.** The homepage teaser and `/loops/` archive fetch the manifest from `raw.githubusercontent.com` at page load. This content is CDN-cached for roughly 5 minutes, so there may be a short delay after publishing before teasers update. Individual loop pages are fully static.

## Local development

Open `index.html` in a browser. The loop teaser on the homepage requires the `content` branch to be pushed to the remote (it fetches from `raw.githubusercontent.com`).

To test loop rendering locally, you can temporarily point the `RAW` variable in the JS to a local server or use a tool like `npx serve`.

## File structure

```
main branch:
├── index.html          # Landing page + latest loop teaser
├── 404.html            # 404 page
├── loops/index.html    # Loop archive/listing page
├── loops/_template.html # Template for generated loop detail pages
├── avatar.png
├── header.png
├── favicon.png
├── bot_*.png           # Flying bot decorations
├── .github/workflows/
│   └── deploy.yml      # GitHub Actions: injects GA4 + deploys to Pages
├── _config.yml         # Jekyll config (excludes agent files)
├── CNAME               # Custom domain (laloloops.com)
├── AGENTS.md
└── CLAUDE.md

content branch (orphan):
└── loops/
    ├── manifest.json
    └── 0001_the_first_loop.md
```
