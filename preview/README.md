# Local preview (throwaway)

This folder is a **local-only** preview harness. It lets the site be browsed with
real-looking content without running the GitHub Actions deploy pipeline. None of
it is production, and none of it touches the `content` branch.

Everything here, plus the generated detail pages (`loops/<slug>/`,
`articles/<slug>/`), is gitignored — see the repo-root `.gitignore`.

## Why this is needed

The site looks static, but two things hide content from a plain local file open:

1. **Detail pages are built only in CI.** `.github/workflows/deploy.yml` fetches
   the `content` branch, reads `loops/manifest.json` + markdown, and renders
   `loops/<slug>/index.html` from `loops/_template.html` (python `markdown`,
   `fenced_code` + `tables`). That never runs locally.
2. **Listing/teaser pages fetch their manifest at runtime** from a hardcoded
   `raw.githubusercontent.com/.../content/...manifest.json` URL — which only
   works over http(s), not `file://`.

## How it works

- `preview/build.py` reuses the **same templating logic as `deploy.yml`**:
  - **Loops** come from `origin/content` exactly like the workflow
    (`git show origin/content:loops/...`), rendered to `loops/<slug>/index.html`.
    The manifest is copied to `preview/content/loops/manifest.json`.
  - **Articles** (and any future collection) are read from committed fixtures
    under `preview/fixtures/<name>/` and rendered to `<name>/<slug>/index.html`.
    The manifest is copied to the served `preview/content/<name>/`. This no-ops
    until an `articles/_template.html` and `preview/fixtures/articles/manifest.json`
    exist.
- The listing/teaser pages detect localhost (`location.hostname` is
  `localhost` / `127.0.0.1` / `::1`) and fetch their manifests from
  `/preview/content/...`. On the real domain they fetch the remote `content`
  branch as before — **production behavior is unchanged**.

## Run it

```bash
./preview.sh           # builds, then serves on http://localhost:8000/
./preview.sh 8003      # custom port
# or, manually:
python3 preview/build.py && python3 -m http.server 8000
```

## Adding article fixtures

Once the site has an Articles section, commit sample fixtures here:

```
preview/fixtures/articles/
├── manifest.json        # {"articles": [{"id","title","summary","date","file"}, ...]}
└── 000N_<slug>.md       # sample long-form articles, Lalo Loops voice
```

These are tracked in git (so the preview is reproducible after a fresh
checkout) but excluded from the published site via `_config.yml`. `build.py`
then renders `articles/<slug>/index.html` and the articles archive lists them on
localhost. See `preview/fixtures/README.md` for the manifest schema.

## Undo / reverse

```bash
rm -rf preview/content loops/[0-9]*/ articles/*/
```

The localhost-aware fetch tweak in `index.html` / `loops/index.html` is
production-safe (only changes behavior on localhost), so it can stay.
