# occams-razor Corrections

This file is a one-time-per-incident log of corrections to occams-razor — instances where the skill's protocol produced a wrong outcome that the author caught or was caught by review. Format adapted from Google SRE blameless post-mortem template (sre.google/sre-book/postmortem-culture) and Etsy Debriefing Facilitation Guide.

**Entry template** (one entry per correction):

```
## [YYYY-MM-DD] {Brief title}

**What happened:** One sentence describing the wrong outcome the protocol produced.
**Why it happened:** The protocol step that was followed or skipped. Cite the section if relevant.
**Damage:** What broke or what got through that shouldn't have. Use blast-radius terms if applicable (HIGH/MEDIUM/LOW).
**Fix to protocol:** Concrete change to SKILL.md that would prevent recurrence.
**Status:** open | in-review | resolved
---
```

**Promote to LEARNINGS.md** after 3+ similar corrections.
