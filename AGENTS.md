# Lalo Loops Web Landing - Agent Context

This repository contains the static website for `laloloops.com`. It is a small
GitHub Pages site built from plain HTML, inline CSS, image assets, and a content
branch used for loop posts.

Keep this file safe to publish. Personal operating preferences, local account
details, commit-author identity, and private publishing rules belong in global
agent configuration outside the repository.

## Project Shape

- No application framework.
- No required build step for ordinary page edits.
- `main` contains the site source.
- `content` contains loop markdown and `loops/manifest.json`.
- GitHub Actions renders loop markdown to static HTML and deploys to Pages.

## Main Files

| Path | Purpose |
|---|---|
| `index.html` | Landing page and latest-loop teaser |
| `404.html` | Not-found page |
| `loops/index.html` | Loop archive page |
| `loops/_template.html` | Template for generated loop detail pages |
| `loops/AGENT_INSTRUCTIONS.md` | Instructions for authoring loop content |
| `*.png` | Brand and bot image assets |
| `_config.yml` | Jekyll/GitHub Pages config |
| `CNAME` | Custom domain |

## Brand Context

When making copy, design, or visual changes, use the sibling branding repository
as reference if it is available locally:

```text
../laloloops-branding/
```

Relevant files:

- `../laloloops-branding/brand/voice_guide.md`
- `../laloloops-branding/brand/brand_os.md`
- `../laloloops-branding/visuals/`

Do not copy the full branding repository into this project.

## Local Development

Open `index.html` in a browser for simple page edits. The homepage loop teaser
fetches published content from the remote `content` branch, so it may not work
fully from a local file URL.

For loop rendering changes, use the workflow documented in `README.md` and
verify generated pages before publishing.

## Working Rules

- Keep the site simple: HTML, CSS, and static assets unless the task explicitly
  requires more.
- Reuse existing visual assets and styling patterns.
- Check responsive behavior before finishing layout changes.
- Never commit secrets, credentials, private paths, personal identifiers, or
  unpublished private context.
- Keep checked-in agent instructions portable. Use `~/.codex/AGENTS.md` and
  `~/.claude/CLAUDE.md` for private personal preferences.
