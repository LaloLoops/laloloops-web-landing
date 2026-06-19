<div style="margin:0 0 2.5rem;">
  <a href="https://x.com/LaloLoops/status/2067935156757750255" target="_blank" rel="noopener" style="display:block;background:#1A1A1A;border:2px solid #E8872B;border-radius:12px;padding:1.4rem 1.6rem;text-decoration:none;">
    <div style="font-family:'Space Mono',monospace;font-size:0.72rem;letter-spacing:0.06em;text-transform:uppercase;color:#E8872B;margin-bottom:0.45rem;">The full essay &middot; on X</div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:1.15rem;font-weight:600;color:#FDF0DC;line-height:1.35;">How I'm Fixing My AI Content Loop &rarr;</div>
  </a>
</div>

I ran a month-long content loop that published daily notes from my work with AI agents. It did the thing I asked for: it showed up every day, stayed on topic, kept the voice mostly intact, and produced clean posts from whatever raw material I gave it.

Then I read the whole month together and found the real problem. One entry at a time, the loop looked fine. Across the archive, it was too safe, too similar, and too good at turning thin inputs into familiar lessons. The failure mode was not one bad post. It was accumulation.

## The archive exposed the pattern

Single-piece review misses what a body of work reveals. The entries repeated favorite words, familiar contrasts, similar endings, and the same argument shape: observation, broad lesson, tidy close. That can look like voice when you read one post. Read thirty in a row and it starts looking like a template wearing a hoodie.

The loop was not being lazy. It was following the incentives I gave it. I rewarded continuity, polish, and publishability. I did not give it enough memory, enough evidence, or enough friction against repeating itself.

## Better inputs, less meditation

The weakest entries came from the thinnest notes. When I gave the system one or two vague sentences, it filled the space with house style and recurring beliefs. That is useful if you need something passable. It is less useful if you want the archive to feel like it came from actual work.

The next version needs a higher input bar. A note should include a decision, a thing that broke, a number, a tradeoff, or a specific artifact from the day. If none of that exists, the loop should look for receipts in commits, logs, issues, drafts, or session notes. If it still finds nothing, the output should be shorter instead of pretending a quiet day is a thesis.

## The loop needs recent memory

The system also needs to know what it just said. Each run had the current note and the broad narrative, but not the recent archive. That meant it could reuse the same phrase, conclusion, or structure without noticing.

So the next loop gets the last seven to ten entries in context, plus checks for repeated phrasing and repeated conclusions. The point is not forced novelty. A content system should have recurring beliefs. But there is a difference between developing an idea over time and unknowingly restating it because the workflow has no short-term memory.

## Review has to happen in batches

I still want the loop to publish without me approving every post. That is the leverage. But if I am not reviewing every draft before it goes live, the system has to review itself better than it did.

That means weekly batch review, not just draft review. The loop should read the recent archive and flag repeated openings, closing beats, lessons, favorite words, emotional posture, and structure. Smoothness is not enough. A piece should earn its place with a concrete detail, a changed belief, a useful mistake, or a real decision.

The next version is less about a better "write in my voice" prompt and more about a stricter operating loop: better raw material, recent memory, repetition checks, batch review, and a higher editorial bar.

---

*Consistency looked like success until the archive proved it was the failure mode.*
