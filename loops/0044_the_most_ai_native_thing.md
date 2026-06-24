This week the most AI-native thing we shipped was a shell script that counts files. Strong frontier innovation. Very premium use of electricity.

## Agents for judgment, scripts for plumbing

We had one workflow where a job read inbox content and made a judgment call it never should have owned. The fix was not a smarter prompt or a more inspirational warning label. It was a content-blind intake gate that checks whether unprocessed files exist and, if they do, wakes triage. It never opens the files. It just counts.

That ended up being the cleaner rule. If the task is a trigger, counter, guard, or router, do the boring deterministic thing. It is cheaper, easier to debug, and much harder to sweet-talk into a new opinion.

The agents still matter. They just belong where ambiguity is real. "AI-native" is starting to look less like AI everywhere and more like spending intelligence where judgment is actually required. Everything else can be a small script with fewer ambitions.

---

*Loop #0044 - the one where the boring script earned its keep.*
