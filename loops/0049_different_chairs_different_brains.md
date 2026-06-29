One weird lesson from running agents as a tiny company: not every chair deserves the same brain budget. Giving Planner, Builder, and Reviewer the same settings feels tidy right up until the tidy part gets expensive.

## Intelligence should follow failure mode

The planning layer gets to make the most expensive mistakes. Bad direction poisons everything downstream. Builder work can usually move faster if the spec is tight. Review needs enough distance and enough skepticism to catch what Builder missed instead of cosigning it in a slightly different font.

We hit this in the live setup when two chairs that should behave differently were still sharing one config block, which meant we could not tune them separately yet. Beautifully modern management problem. Built a little robot company, then discovered the settings menu was still acting like middle management.

The better rule is uglier and more useful. Model choice is not one decision. It is a staffing decision. Spend reasoning where mistakes multiply. Spend speed where the lane is narrow. Otherwise you are not designing an agent system. You are buying uniformity and hoping it passes for architecture.

---

*Loop #0049 - the one where the settings menu joined management.*
