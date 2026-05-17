# Loop Publishing — Agent Instructions

These instructions are for any AI agent tasked with writing and publishing a new loop.

---

## What is a loop?

A loop is a short public dispatch published at [laloloops.com/loops/](https://laloloops.com/loops/). Think of it as a micro blog post — a build-in-public update about what's being built, shipped, broken, or learned.

**Loops are public.** They are read by strangers on the open internet. Every word you write will be visible to anyone with a browser. Write accordingly.

---

## Privacy rules — read this first

This is a pseudonymous project. The person behind Lalo Loops is anonymous and must stay that way.

**Never include any of the following in a loop:**

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

**When in doubt, leave it out.** If a detail doesn't serve the public reader, it doesn't belong in the loop.

---

## Voice and tone

Loops should sound like Lalo Loops — not like a corporate blog, not like an AI-generated summary.

- **Dry humor, self-aware, technically competent, commercially humbled.** "Serious thesis, unserious delivery."
- Write like a developer talking to developer friends in a group chat. Casual but sharp.
- Never sound like an AI hype bro, a fake guru, or a SaaS press release.
- Never use filler phrases like "In this post we'll explore..." or "Let's dive into..."
- Filter: would a real person actually say this?

If the branding repo is available at `../laloloops-branding/brand/voice_guide.md`, read it before writing.

---

## Workflow

### Step 1 — Sync the content branch

The loop files live on the **`content`** branch of `laloloops-web-landing`. This is an orphan branch — it shares no history with `main`.

```bash
git fetch origin content
git checkout content
git pull origin content
```

You must be on the `content` branch and up to date before doing anything else.

### Step 2 — Determine the next loop number

Read `loops/manifest.json`. Look at the last entry in the `loops` array. The next loop number is one higher, zero-padded to four digits.

Example: if the last entry is `"id": "0003_whatever"`, the next loop number is `0004`.

### Step 3 — Choose a slug

The slug follows the format: `NNNN_short_descriptive_name`

- `NNNN` is the zero-padded loop number from step 2
- The rest is a short, lowercase, underscore-separated description
- Keep it concise — it becomes the URL: `laloloops.com/loops/0004_short_descriptive_name`
- Use only lowercase letters, digits, and underscores

Examples of good slugs:
- `0004_first_real_product`
- `0005_agents_broke_everything`
- `0006_distribution_is_hard`

### Step 4 — Write the markdown file

Create `loops/<slug>.md` on the `content` branch. This is the loop content.

Format:
- Write in standard markdown
- Do not include a top-level `# heading` — the title is rendered from the manifest, not the markdown
- Use the loop house format in this exact order:
  - a short opening intro paragraph before any heading
  - one `##` subtitle immediately after the intro
  - the main body under that subtitle, usually 2-4 short paragraphs
  - a horizontal rule and italic closing footer
- Do not skip the subtitle and do not collapse the whole loop into body copy
- End with a horizontal rule (`---`) and a closing line like `*Loop #NNNN — short tagline.*`
- Keep it short. A loop is a dispatch, not an essay. A few paragraphs is plenty.

Use `loops/0002_launch_meet_silence.md`, `loops/0003_posting_through_the_cringe.md`, and `loops/0004_shadowban_probably.md` on the `content` branch as the clearest references for this shape. `loops/0001_the_first_loop.md` is still a valid tone and length reference. Here is `0001` in full:

```markdown
This is where it begins. One human, a handful of agents, and a landing page that took longer to build than it should have.

## What is a loop?

A loop is a dispatch. A small update. A note from the trenches of building things with AI agents while also being a dad with a day job.

Sometimes it'll be about something we shipped. Sometimes it'll be about something that broke. Occasionally it'll be about the coffee.

## Why write loops?

Because building in public means actually... being public. And because the agents need accountability. If I don't document what they're doing, they'll just keep refactoring the same file forever.

## What's next?

More loops. More agents. More coffee. Probably a product at some point.

---

*Loop #0001 — the one where we start.*
```

Things to notice about this example:
- No `# top-level heading` — the title comes from the manifest, not the markdown
- Opens with a short, punchy paragraph — no preamble
- Published loops should still include one explicit `##` subtitle after the intro, even when the rest is brief
- Each section is 1–3 short paragraphs — not walls of text
- Ends with `---` and an italic closing tagline
- Total length is roughly 150 words — that's the target range. A bit more is fine, an essay is not
- Tone is conversational and self-deprecating, not polished or corporate

### Step 5 — Update the manifest

Edit `loops/manifest.json`:

1. **Append** a new entry to the end of the `loops` array:
   ```json
   {
     "id": "<slug>",
     "title": "<Human-readable title>",
     "summary": "<One sentence, plain text, shown in teasers and the archive>",
     "date": "<YYYY-MM-DD>",
     "file": "<slug>.md"
   }
   ```
2. **Set** the `"latest"` field to the new loop's `id`.

The `id` must exactly match the markdown filename (without `.md`). The `summary` is plain text — no markdown, no HTML. The `date` is the publication date.

### Step 6 — Validate

Before committing, verify:

- [ ] The markdown file exists at `loops/<slug>.md`
- [ ] The `id` in the manifest matches the filename (minus `.md`)
- [ ] The `file` field matches the actual filename
- [ ] The `latest` field points to the new loop's `id`
- [ ] The `loops` array is valid JSON (no trailing commas, proper quoting)
- [ ] The loop number is consecutive — no gaps, no duplicates
- [ ] The content contains **zero** personal, private, or sensitive information
- [ ] The tone sounds like Lalo Loops, not like a corporate blog or raw AI output

### Step 7 — Commit and push

```bash
git add loops/<slug>.md loops/manifest.json
git commit -m "Add loop NNNN"
git push origin content
```

Commit rules:
- The commit author must be `Lalo Loops <laloloops@proton.me>` (set via repo-level git config)
- Never add `Co-Authored-By` trailers for any AI tool
- Never reference AI tools in the commit message
- Keep the commit message short and human: `"Add loop 0004"` is fine

---

## Manifest schema reference

```json
{
  "loops": [
    {
      "id": "string — URL slug, matches filename without .md",
      "title": "string — human-readable title, shown as page heading",
      "summary": "string — one sentence, plain text, shown in cards and teasers",
      "date": "string — YYYY-MM-DD publication date",
      "file": "string — filename inside loops/ on the content branch"
    }
  ],
  "latest": "string — id of the loop to feature on the homepage"
}
```

The `loops` array is ordered chronologically. New entries go at the end. The site displays them in reverse order (newest first).

---

## What not to do

- **Don't touch the `main` branch.** Loops are published entirely via the `content` branch.
- **Don't delete or modify existing loops.** Only append new ones.
- **Don't skip loop numbers.** They must be consecutive.
- **Don't write loops that read like AI-generated slop.** If it sounds like a language model wrote it, rewrite it until it doesn't.
- **Don't include images hosted on external services.** If a loop needs an image, it should be committed to the `loops/` directory on the `content` branch and referenced with a relative path.
- **Don't publish without validating the manifest JSON.** A malformed manifest breaks the entire loops system on the live site.
