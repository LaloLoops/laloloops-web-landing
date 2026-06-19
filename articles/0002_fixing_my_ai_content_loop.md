<div style="margin:0 0 2.5rem;">
  <a href="https://x.com/LaloLoops/status/2067935156757750255" target="_blank" rel="noopener" style="display:block;background:#1A1A1A;border:2px solid #E8872B;border-radius:12px;padding:1.4rem 1.6rem;text-decoration:none;">
    <div style="font-family:'Space Mono',monospace;font-size:0.72rem;letter-spacing:0.06em;text-transform:uppercase;color:#E8872B;margin-bottom:0.45rem;">The full essay &middot; on X</div>
    <div style="font-family:'Space Grotesk',sans-serif;font-size:1.15rem;font-weight:600;color:#FDF0DC;line-height:1.35;">How I'm Fixing My AI Content Loop &rarr;</div>
  </a>
</div>

For the past month, an autonomous loop wrote a daily public log from my work with AI agents. *(You can read it at [laloloops.com/loops/](https://laloloops.com/loops/).)*

The setup was simple. Some days I sent a remote agent a short Telegram note about what I had been building, the loop folded that into an ongoing narrative, and an entry went up. Some days I sent nothing and it wrote an entry of its own from the narrative it had already built.

It never missed a day. I was proud of that streak until I read the whole month in one sitting and stopped being proud of the output.

Read one at a time, the entries were fine. Read together, they exposed the thing I had actually built: not a content system that learned from the month, but a content system that could reliably turn thin inputs into clean, similar outputs.

Each individual entry was good enough. That is the problem. Every post was acceptable on its own, and the sameness only showed up across the set.

The problem is accumulation.

## The problem was not one bad post

Most discussions about AI-written content still focus on the single-piece smell test. Does this paragraph sound robotic? Did it use the forbidden phrase? Is there a suspiciously neat contrast in the middle?

That is not where my loop failed.

The individual entries were readable. The facts were mostly right. The tone was close enough. Each entry had a point, a shape, and a tidy ending. If I had only published one of them, I probably would not have noticed much.

The issue appeared only after accumulation.

Across thirty-one entries, "boring" appeared in thirteen, almost always doing the same job, praising unglamorous architecture. "Demo" appeared in fourteen, usually as the thing real workflows are not. The exact phrase "confidently unfinished" showed up twice, eight days apart, presented both times as a fresh observation. Entry ten argued that yesterday's mess was not momentum. Entry thirty argued that continuity was the feature. Those are close cousins, and the loop kept reaching for the same ideas in nearly the same words.

The structure repeated too. Almost every entry followed the same arc: a short observation, a broad interpretation, a general lesson about state or context or review, and a clean closing line. That arc was in my system prompt, so the loop was just following instructions. Read once, it looks like a voice. Read thirty times, it looks like a template.

## The loop rewarded sameness

Once I saw the pattern, the cause was less mysterious than I wanted it to be.

The loop was doing exactly what I had trained it to do. I gave it a small note, a narrative direction, some tone constraints, and permission to produce a publishable entry. It optimized for clean continuity because that is what the system rewarded.

There was no mechanism for freshness. No recent archive in context, no memory of phrases already used, no check for repeated conclusions, and no editor asking whether today's lesson had already appeared three times this month. The model did not independently decide to become repetitive. The workflow made repetition cheap and approval easy.

So if the problem is that the system rewards safe repetition, the fix is operational, not a cleverer prompt: better inputs, better memory, better review, and a higher standard for what counts as publishable.

## Better inputs beat better prompting

The first fix is upstream.

My Telegram notes were often too thin. Sometimes they were two sentences. Sometimes one. A note that short gives the model almost nothing to anchor to, so it fills the empty space with whatever the system already knows: the house style, the recurring beliefs, the safest lesson, the familiar closing beat.

Looking back, the flattest entries came from the thinnest notes. The model did not get worse on those days. It just had nothing to work with except itself.

The next version of the loop needs a minimum input standard. A useful note should carry at least one of these:

- a decision I made;
- a thing that broke;
- a number;
- a tradeoff;
- a specific file, feature, bug, prompt, test, or artifact.

If I miss a note, or my note does not carry one of those, the loop should not write around the absence. It should go looking for a receipt in the day's actual artifacts: commits, session notes, logs, issue updates, drafts, whatever changed.

And if there is still no real detail, the entry should be short. Maybe very short. A quiet day does not need to become another meditation that's mostly made up.

## The loop needs memory

The second fix is recent memory.

Each run saw the current note and the broad narrative, but it did not see the last week of published output. That meant it could not know it had already used the same phrase, made the same contrast, or landed on the same conclusion.

So the next version gets a recent archive in context. The last seven to ten entries should be part of every generation run, with a blunt instruction: do not repeat their phrasing, their conclusions, or their argument shape unless there is a clear reason.

That does not mean forcing novelty for novelty's sake. A content system should have recurring beliefs; that is how a body of work becomes coherent instead of random. But there is a difference between developing a belief over time and restating it because the workflow has no memory of what it said yesterday.

The question for each new entry should be:

> What does today's evidence add that the archive has not already said?

If the answer is nothing, the loop should either find a sharper detail or publish less.

## Review the month, not just the draft

The third fix is changing what review means.

Here is the honest part: I don't approve entries before they go up. The whole point of the loop is to give me leverage, to let the system run while I spend my attention building the next thing. So I read the entries after they publish, not before. If I am going to keep my hands off the publish button, the loop has to be able to review itself well enough that I can trust it to.

That review cannot only happen one draft at a time, because sameness does not show up at the draft level. It shows up across the body of work. So the loop needs a second pass that runs in batches. Once a week, it should read the recent archive and flag what a single-entry review cannot see:

- repeated openings;
- repeated closing beats;
- repeated lessons;
- repeated favorite words;
- repeated emotional posture;
- repeated structure disguised as voice.

A simple text check can catch phrase reuse. A better review pass can catch argument reuse across time. Even a dumb script comparing today's draft against the last ten entries would have caught "confidently unfinished" the second time.

## Smooth is not the standard

The fourth fix is editorial.

AI is very good at producing text that is good enough if your standard is cleanliness. It can make a paragraph flow. It can add a conclusion. It can sound calm, competent, and vaguely useful while saying very little that had to be observed.

The standard I actually want is different: does this piece say something specific, earned, and different enough to deserve a place in the archive? That raises the bar in a useful way. A draft should not survive because it is smooth. It should survive because it has a reason to exist. A concrete detail. A changed belief. A useful mistake. A decision someone else can learn from. A piece of evidence that makes the claim feel paid for.

Sometimes that means cutting the prettiest sentence because it is only pretty. Sometimes it means keeping the awkward sentence because it contains the actual truth.

## The next version of the loop

So the next version is not a better "write in my voice" prompt. It is a stricter operating loop:

1. Capture better raw material from the day.
2. Require at least one receipt before drafting.
3. Include the recent archive in every generation run.
4. Check for repeated phrases and repeated conclusions before publish.
5. Run a weekly batch review of the whole body of work.
6. Judge each entry on earnedness, not polish.

The goal is to make the work worth reading. That requires the system to preserve the thing AI is worst at inventing from nowhere: lived specificity. The actual detail. The decision. The bug. The artifact. The small operator lesson that came from doing the work, not from asking a model to produce a lesson-shaped draft.

## How I will know it worked

The test is simple.

Next month, I should be able to pick an entry at random and roughly tell which week it came from. Not because the date is obvious, but because the writing knows things it did not know before. The archive should show motion.

If every entry could have been published on any day of the month, the loop is still circling.

The uncomfortable part is that the first version did exactly what I built it to do. It showed up every day and produced clean, publishable text from whatever I gave it. That consistency looked like success.

Now consistency is the failure mode.

The next version has a harder job. It needs to remember what it already said, ask for better evidence, catch its own repetition, and hold a higher bar before the archive turns into the same entry with new dates. That is the real lesson from the month: attention only matters if it changes the system.
