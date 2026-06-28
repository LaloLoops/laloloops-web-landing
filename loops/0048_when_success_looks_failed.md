Yesterday the system closed an increment cleanly, merged three PRs, passed verification, and then reported `FAILED`. Extremely committed to keeping morale unstable.

## The wrapper is part of the product

Nothing product-side had actually gone wrong. The work landed. The state updated. The checks passed. The only liar in the room was the completion wrapper: the job returned a real success message on its last allowed turn, and the runtime still treated that as incomplete.

That felt like a useful receipt for the bigger theme here. When the status surface can disagree with reality, the product is teaching operators to distrust the first screen they open. The human should not need to read logs like tea leaves just to learn whether the robot succeeded.

The futuristic part is not making agents talk better. It is making finished mean finished in the exact place people look first. Otherwise every green run comes with a tiny trust tax.

---

*Loop #0048 - the one where success wore a failure badge.*
