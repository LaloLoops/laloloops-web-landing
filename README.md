# laloloops-web-landing

Static landing page for [laloloops.com](https://laloloops.com). Hosted on GitHub Pages.

> **Disclaimer:** This project is built entirely by AI agents. No human code review has been performed. Use at your own risk.

## How it works

The site is plain HTML served from the `main` branch. No build step, no frameworks.

Dynamic content (loops — short dispatches/updates) lives on a separate **`content`** branch and is fetched client-side at page load via `raw.githubusercontent.com`.

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
| `/loops/<slug>` | `404.html` | Individual loop viewer. GitHub Pages serves `404.html` for any path that doesn't match a real file. The page extracts the slug from the URL, looks it up in the manifest, fetches the corresponding `.md` file, and renders it with [marked.js](https://github.com/markedjs/marked). If the slug doesn't match anything, it shows a 404 message. |

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

The site picks it up automatically. No changes to `main` needed.

### Caching

`raw.githubusercontent.com` is CDN-cached for roughly 5 minutes. After pushing new content to the `content` branch, there may be a short delay before it appears on the live site.

### Known limitations

- **HTTP 404 status on individual loops.** URLs like `/loops/0001_the_first_loop` are served by the GitHub Pages 404 handler, so the HTTP response code is 404 even though the page renders correctly. This means social media crawlers (Twitter cards, Open Graph) won't generate link previews. This is an inherent GitHub Pages limitation for client-side routing. A future GitHub Action could generate static HTML files to fix this.
- **No server-side rendering.** The content is fetched and rendered entirely in the browser. If JavaScript is disabled, only the static parts of the page are visible.
- **Markdown is rendered unsanitized.** Since all content comes from this repo (which you control), this is fine. If you ever accept external content, add [DOMPurify](https://github.com/cure53/DOMPurify) or similar.

## Local development

Open `index.html` in a browser. The loop teaser on the homepage requires the `content` branch to be pushed to the remote (it fetches from `raw.githubusercontent.com`).

To test loop rendering locally, you can temporarily point the `RAW` variable in the JS to a local server or use a tool like `npx serve`.

## File structure

```
main branch:
├── index.html          # Landing page + latest loop teaser
├── 404.html            # Individual loop viewer + 404 page
├── loops/index.html    # Loop archive/listing page
├── avatar.png
├── header.png
├── favicon.png
├── bot_*.png           # Flying bot decorations
├── _config.yml         # Jekyll config (excludes agent files)
├── CNAME               # Custom domain (laloloops.com)
├── AGENTS.md
└── CLAUDE.md

content branch (orphan):
└── loops/
    ├── manifest.json
    └── 0001_the_first_loop.md
```
