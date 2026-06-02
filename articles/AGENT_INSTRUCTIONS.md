# Article Publishing — Agent Instructions

These instructions are for any AI agent tasked with writing and publishing a new long-form article.

---

## What is an article?

An article is a longer public piece published at [laloloops.com/articles/](https://laloloops.com/articles/). It is the essay-shaped sibling of a loop: deeper thinking about agent workflows, product building, distribution from zero, and the awkward operator reality underneath the shiny demos.

**Articles are public.** They are read by strangers on the open internet. Every word you write will be visible to anyone with a browser. Write accordingly.

---

## Privacy rules — read this first

This is a pseudonymous project. The person behind Lalo Loops is anonymous and must stay that way.

**Never include any of the following in an article:**

- Real names, usernames, or handles of anyone (except `@LaloLoops` / Lalo Loops)
- Employer names, company names, or client names
- Location, city, country, timezone, or anything geographically identifying
- Family details, ages, relationships, or personal anecdotes that could identify someone
- Email addresses, phone numbers, IP addresses, or account identifiers
- API keys, tokens, passwords, secrets, or credentials of any kind
- Internal project names, codenames, or references to private repositories
- Names or identifiers of other people, collaborators, or contacts
- Financial details — revenue figures, salary, costs, or account numbers
- Anything that could de-anonymize the person behind Lalo Loops

**When in doubt, leave it out.** If a detail doesn't serve the public reader, it doesn't belong in the article.

---

## Voice and tone

Articles should sound like Lalo Loops — not like a corporate blog, not like an AI-generated essay.

- **Dry humor, self-aware, technically competent, commercially humbled.** "Serious thesis, unserious delivery."
- Write like a developer explaining a hard-won operating lesson to developer friends.
- Keep the thesis serious and the delivery human. The article can be thoughtful without dressing up as thought leadership.
- Never sound like an AI hype bro, a fake guru, or a SaaS press release.
- Never use filler phrases like "In this post we'll explore..." or "Let's dive into..."
- Filter: would a real person actually say this?

If the branding repo is available at `../laloloops-branding/brand/voice_guide.md`, read it before writing.

---

## Workflow

### Step 1 — Sync the content branch

The article files live on the **`content`** branch of `laloloops-web-landing`. This is an orphan branch — it shares no history with `main`.

```bash
git fetch origin content
git checkout content
git pull origin content
```

You must be on the `content` branch and up to date before doing anything else.

### Step 2 — Determine the next article number

Read `articles/manifest.json`. Look at the last entry in the `articles` array. The next article number is one higher, zero-padded to four digits.

Example: if the last entry is `"id": "0003_whatever"`, the next article number is `0004`.

### Step 3 — Choose a slug

The slug follows the format: `NNNN_short_descriptive_name`

- `NNNN` is the zero-padded article number from step 2
- The rest is a short, lowercase, underscore-separated description
- Keep it concise — it becomes the URL: `laloloops.com/articles/0004_short_descriptive_name`
- Use only lowercase letters, digits, and underscores

Examples of good slugs:

- `0001_agents_need_management`
- `0002_distribution_for_builders`
- `0003_the_tiny_team_problem`

### Step 4 — Write the markdown file

Create `articles/<slug>.md` on the `content` branch. This is the article content.

Format:

- Write in standard markdown
- Do not include a top-level `# heading` — the title is rendered from the manifest, not the markdown
- Open with a short, direct intro paragraph before any heading
- Use clear `##` sections that move the argument forward
- Prefer concrete operator detail: tradeoffs, mistakes, system decisions, receipts, and what changed
- Keep paragraphs short enough to scan
- End with a horizontal rule (`---`) and an italic closing footer like `*Article #NNNN — short tagline.*`
- Target roughly 800-1,500 words. Shorter is fine when the idea is finished. Longer is allowed only when the structure earns it.

Good article structure:

```markdown
The problem was not that the agents were bad. The problem was that I had accidentally become middle management for autocomplete.

## The thing I expected

Set up the expectation, belief, or system design.

## The thing that actually happened

Show the failure mode, tradeoff, or unexpected behavior with enough detail to be useful.

## The operating rule

Explain what changed and why it matters.

## What this means for builders

Bring it back to a practical takeaway without pretending to have solved capitalism before lunch.

---

*Article #0001 — management was the missing dependency.*
```

Things to notice:

- No `# top-level heading` — the title comes from the manifest
- The opening paragraph starts with signal, not preamble
- Each section has a job
- The humor sits under the point instead of replacing it
- The ending gives the piece a clean exit

### Step 5 — Update the manifest

Edit `articles/manifest.json`:

1. **Append** a new entry to the end of the `articles` array:
   ```json
   {
     "id": "<slug>",
     "title": "<Human-readable title>",
     "summary": "<One sentence, plain text, shown in teasers and the archive>",
     "date": "<YYYY-MM-DD>",
     "file": "<slug>.md"
   }
   ```
2. **Set** the `"latest"` field to the new article's `id`.

The `id` must exactly match the markdown filename (without `.md`). The `summary` is plain text — no markdown, no HTML. The `date` is the publication date.

### Step 6 — Validate

Before committing, verify:

- [ ] The markdown file exists at `articles/<slug>.md`
- [ ] The `id` in the manifest matches the filename (minus `.md`)
- [ ] The `file` field matches the actual filename
- [ ] The `latest` field points to the new article's `id`
- [ ] The `articles` array is valid JSON (no trailing commas, proper quoting)
- [ ] The article number is consecutive — no gaps, no duplicates
- [ ] The content contains **zero** personal, private, or sensitive information
- [ ] The tone sounds like Lalo Loops, not like a corporate blog or raw AI output
- [ ] The piece has a real thesis, not just a longer loop with bigger shoes

### Step 7 — Commit and push

```bash
git add articles/<slug>.md articles/manifest.json
git commit -m "Add article NNNN"
git push origin content
```

Commit rules:

- Use the repository's configured commit author
- Never add `Co-Authored-By` trailers for any AI tool
- Never reference AI tools in the commit message
- Keep the commit message short and human: `"Add article 0001"` is fine

---

## Manifest schema reference

```json
{
  "articles": [
    {
      "id": "string — URL slug, matches filename without .md",
      "title": "string — human-readable title, shown as page heading",
      "summary": "string — one sentence, plain text, shown in cards and teasers",
      "date": "string — YYYY-MM-DD publication date",
      "file": "string — filename inside articles/ on the content branch"
    }
  ],
  "latest": "string — id of the article to feature on the homepage"
}
```

The `articles` array is ordered chronologically. New entries go at the end. The site displays them in reverse order (newest first).

---

## What not to do

- **Don't touch the `main` branch when publishing articles.** Articles are published entirely via the `content` branch.
- **Don't delete or modify existing articles.** Only append new ones.
- **Don't skip article numbers.** They must be consecutive.
- **Don't write articles that read like AI-generated slop.** If it sounds like a language model wrote it, rewrite it until it doesn't.
- **Don't include images hosted on external services.** If an article needs an image, it should be committed to the `articles/` directory on the `content` branch and referenced with a relative path.
- **Don't publish without validating the manifest JSON.** A malformed manifest breaks the entire articles system on the live site.
