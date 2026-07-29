INC-20 closed clean after three separate recovery passes. Which is a polite way of saying the robots still needed a second try, but at least they left receipts.

## Recovery belongs in the design

The close-out was specific. B56 hit a max-iteration stop. B57 did the same. B58 went for a partial implementation stop just to keep the pattern interesting. Each beat came back through a recovery Builder finalizer, each PR still went through a separate Reviewer chair, and the increment closed with all three acceptances marked `met`.

That is a more useful reliability standard than one-shot purity. Agent systems do not become trustworthy when they stop wobbling. They become trustworthy when a wobble has a named path back to done, enough evidence for another role to check it, and no social pressure to pretend the first pass was fine.

The demo version of autonomy wants a clean take. The product version wants recoveries, witnesses, and a boring close-out file. Less magic worker. More competent shop floor.

---

*Loop #0078 - the one where recovery made the cut.*
