# Preview fixtures (committed)

Authored sample content for the local preview, kept in git so anyone can run
`./preview.sh` and see populated listings **without regenerating anything**.

These files are the **source of truth** for preview content. They are tracked,
but excluded from the live site via `_config.yml` (`exclude: preview`), so they
never publish to laloloops.com and never reach the `content` branch. `build.py`
copies/renders them into the gitignored `preview/content/` (served) location.

> Loops need no fixtures here — they are rendered from the real `content` branch
> (`origin/content`), exactly like CI. Only collections that have no published
> content yet (i.e. articles) live here.

## Layout

```
preview/fixtures/
└── articles/
    ├── manifest.json     # {"articles": [ {id, title, summary, date, file}, ... ]}
    └── <id>.md           # one markdown file per article, in the Lalo Loops voice
```

### manifest.json shape

```json
{
  "articles": [
    {
      "id": "0001_some_slug",
      "title": "Some Title",
      "summary": "One-line teaser.",
      "date": "2026-06-01",
      "file": "0001_some_slug.md"
    }
  ]
}
```

`id` becomes the URL slug (`/articles/<id>/`) and, if it starts with digits,
the displayed number. Match the field names and template placeholders
(`{{TITLE}}`, `{{DATE}}`, `{{ARTICLE_NUM}}`, `{{BODY}}`, ...) used by your
`articles/_template.html`.

## Where these come from

The Articles section is added by a redesign branch. When that lands, it commits
its sample articles here so the fixtures match its own manifest schema and
template. Until then this folder only documents the convention.
