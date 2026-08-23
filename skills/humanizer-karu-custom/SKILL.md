---
name: humanizer-karu-custom
version: 5.0.0
description: |
  Remove signs of AI-generated writing from text. Use when editing text to make it
  sound more natural and human-written. Based on Wikipedia's "Signs of AI writing" guide.
  Addresses: inflated symbolism, promotional language, em dash overuse, AI vocabulary,
  filler phrases, sycophantic tone, vague connection (2025+ LLMs), skipped heading levels,
  notability parade, misattributed source analysis, low punctuation density, hedging verb
  padding, and other patterns. Model-aware: pattern signal strength varies by LLM
  (Claude / ChatGPT / Gemini / Grok). For full pattern reference, see PATTERNS.md.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
---

# Humanizer: Remove AI Writing Patterns

## When NOT to Use This Skill

- **Academic writing with genuine hedging**: "may indicate", "further research needed" are correct in scholarship
- **Legal/compliance documents**: Formulaic phrases are required for precision
- **Technical docs with standard terminology**: Established terms used correctly should not be "simplified"
- **When preserving original voice matters more than pattern removal**: Some authors have styles that overlap with AI patterns
- **Marketing copy where enthusiasm fits the brand**: Do not strip intended promotional tone

---

## Context Modes

| Mode | Use For | Pattern Priority |
|------|---------|------------------|
| **Academic** | Scholarly writing, research papers | Remove filler; preserve appropriate hedging |
| **Casual** | Blog posts, opinion pieces | Remove em dash overuse, promotional language, AI vocabulary |
| **Technical** | Documentation, code comments, API docs | Remove filler phrases, copula avoidance; preserve precision terms |
| **Marketing** | Sales copy, landing pages | Remove sycophantic tone; preserve rule of three if intentional |

---
## Pattern Severity Tiers

### Tier 1: HIGH Impact (Address always)
1. **AI Vocabulary**: Additionally, crucial, pivotal, underscore, landscape, showcase, testament
2. **Em Dash Overuse** (Claude-only HIGH; ChatGPT LOW — see Pattern 13 caveat): Multiple em dashes in close proximity
3. **Filler Phrases**: In order to, due to the fact that, at this point in time
4. **Inflated Significance**: Pivotal moment, testament, underscores the importance
5. **Promotional Language**: Breathtaking, groundbreaking, renowned, nestled
6. **Sycophantic Tone**: Great question!, You're absolutely right!, Excellent point
7. **Vague Connection (NEW)**: "associated with", "in connection with", "particularly/widely associated with" — strong 2025+ signal across all models. [Pattern 25]
8. **Skipped Heading Levels (NEW)**: jumping H2→H4, H1→H3 in rendered Markdown/wikitext. [Pattern 26]
9. **Notability / Media Coverage Parade (NEW)**: listing outlets without specific dates/context to claim significance. [Pattern 27]
10. **Misattributed Source Analysis (NEW)**: claim attached to named source ("X highlighted the lasting influence") that the source did not actually make. [Pattern 28]

### Tier 2: MEDIUM Impact (Address when clearly present)
11. **Superficial -ing Analyses**: Highlighting, underscoring, reflecting
12. **Vague Attributions**: Experts believe, some critics argue
13. **Rule of Three Overuse**: Innovation, inspiration, industry insights
14. **Negative Parallelism**: Not only...but..., It's not just...it's...
15. **Copula Avoidance**: Serves as, stands as, boasts
16. **Generic Positive Conclusions**: Exciting times lie ahead, major step forward
17. **Punctuation Density Too Low (NEW)**: >40 words/sentence average, <1 comma per 25 words. [Pattern 29]
18. **Hedging Verb Padding (NEW)**: ensures, ensuring, highlights (when not adding info), reflects (figurative). [Pattern 30]

### Tier 3: LOW Impact (Address selectively)
19. Elegant Variation (synonym cycling)
20. Boldface Overuse
21. Inline-Header Lists
22. Title Case in Headings
23. False Ranges
24. Excessive Hedging
25. Collaborative Artifacts (I hope this helps...)
26. Emojis (Claude: low signal; ChatGPT/Grok: higher signal — see Pattern 17)
27. Curly Quotation Marks (ChatGPT/DeepSeek-specific; Claude/Gemini usually straight) [Pattern 18]

**Deprecated**: Knowledge-cutoff disclaimers (do not apply)
---

## Pattern Conflict Detection

1. **Single phrase, multiple patterns**: Apply most severe tier only
2. **Context mode conflicts**: Default to context mode
3. **Author voice vs. pattern removal**: Preserve author-introduced terms
4. **Grammar/clarity conflicts**: Humanizer addresses tone, not grammar

**Resolution priority**: Author voice > Context mode > Severity tier > Default fix

---

## Process

1. **Determine context mode**: Academic, Casual, Technical, or Marketing
2. **Identify patterns by tier**: Tier 1 → Tier 2 → Tier 3
3. **Rewrite problematic sections**: Apply context-appropriate fixes
4. **Add soul**: Inject personality (see below)
5. **Resolve conflicts**: Use Conflict Detection above
6. **Verify output**:
   - Sounds natural when read aloud
   - Varies sentence structure
   - Uses specific details over vague claims
7. **Present the humanized version**

---

## Adding Soul

Removing AI patterns is half the job. Sterile writing is just as obvious.

### Signs of Soulless Writing (Even If "Clean")
- Every sentence the same length
- No opinions, just neutral reporting
- No first-person when appropriate
- Reads like a Wikipedia article

### Procedural Steps
1. **Add one opinion** the writer might have
2. **Vary rhythm**: long sentence → short sentence
3. **Check sentence length uniformity** (2026 signal): AI text averages 18-30 word sentences with low variance; humans write some 5-word sentences and some 50-word ones. Break uniformity.
4. **Add specifics**: names, dates, numbers
5. **Include contradiction**: "It's impressive, but also unsettling"
6. **Use first-person** where it fits
7. **Allow imperfection**: tangents, unfinished thoughts

### Example
**Clean but soulless:**
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical.

**Has a pulse:**
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. But I keep thinking about those agents working through the night.

---

## Cross-Skill Integration

| Skill | When to Chain |
|-------|---------------|
| **rubber-ducking** | Before humanizing: verbalize what text is trying to say |
| **decision-matrix** | When deciding between multiple rewrite options |
| **chestertons-fence** | Before removing patterns the author introduced |
| **map-vs-territory** | Verify humanized output sounds natural to target audience |
| **systems-thinking** | Consider tone change downstream effects |

---

## Self-Improvement Protocol

**Log only novel discoveries** — something genuinely new, not already in patterns.

```markdown
## [YYYY-MM-DD] {Brief Description}
**Pattern**: {what was new}
**Fix applied**: {what worked}
---
```

**Promote after 3+ occurrences.**

---

## Output Format

1. The rewritten text
2. Summary of changes made (optional)
3. "Logged N correction(s) to .learnings/" if applicable

---

## Full Example

**Before (AI-sounding):**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently. It's not just an update, it's a revolution in how we think about productivity. Industry experts believe this will have a lasting impact on the entire sector, highlighting the company's pivotal role in the evolving technological landscape.

**After (Humanized):**
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

**Changes**: Removed "serves as a testament" (inflated significance), "Moreover" (AI vocabulary), "seamless, intuitive, and powerful" (rule of three), em dash (overuse), "It's not just...it's..." (negative parallelism), "Industry experts believe" (vague attribution), "pivotal role" and "evolving landscape" (AI vocabulary).

---

## Reference

Based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing).

Key insight: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

---

## Evaluations

### Eval 1: Tier 1 Pattern Removal
**Scenario:** Text contains "Additionally, this pivotal solution underscores our commitment" and multiple em dashes.
**Expected:** Identifies AI vocabulary (Additionally, pivotal, underscores) and em dash overuse as Tier 1, removes all.
**Pass criteria:** MUST remove all Tier 1 patterns, produces natural-sounding output.

### Eval 2: Tier 2 Pattern Removal + Context Mode
**Scenario:** Academic paper has "Furthermore, experts believe this research serves as a cornerstone" with excessive hedging.
**Expected:** Recognizes "experts believe" as vague attribution (Tier 2) and "serves as" as copula avoidance (Tier 2), but preserves legitimate academic hedging.
**Pass criteria:** Removes Tier 2 patterns without removing legitimate academic voice.

### Eval 3: Adding Soul
**Scenario:** Text is clean but soulless: "The experiment produced results. Data was collected. Conclusions were drawn."
**Expected:** Applies "Add Soul" steps — varies rhythm, adds opinion, includes specifics.
**Pass criteria:** Transforms sterile text into something with personality while preserving accuracy.

### Eval 4: Model-Specific Pattern Detection (NEW)
**Scenario:** Text contains one em dash in otherwise unremarkable prose. Source LLM unknown.
**Expected:** Notes em dash alone is weak 2026 signal. Checks sentence length (Pattern 29). Looks for vague connection (Pattern 25). If none present, states: "no model-specific confidence; cannot attribute to AI from this text alone."
**Pass criteria:** Does NOT over-claim based on em dash alone. Correctly applies model-specific weighting. Refuses attribution when signal is insufficient.

### 5.0.0
- **Model-aware detection** (major). Added 4 new Tier 1 patterns: vague connection (P25), skipped heading levels (P26), notability/media coverage parade (P27), misattributed source analysis (P28). Added 2 new Tier 2 patterns: punctuation density (P29), hedging verb padding (P30).
- Revised em dash pattern (P13) with July 2026 model caveat: only Claude overuses; ChatGPT 5.1+ suppressed them.
- Revised emoji pattern (P17) with model caveat: Claude rare, ChatGPT/Grok higher.
- Re-promoted curly quotes (P18) as Tier 3 model-specific (ChatGPT/DeepSeek default; Claude/Gemini straight).
- Added "Model Era Note" at top of PATTERNS.md with per-model signal weighting table.
- Added Eval 4: model-specific detection (refuse attribution when signal insufficient).
- Added sentence-length uniformity check to Add Soul procedural steps.
- Pattern reference renumbered; v4.1.0 had 24 patterns with a gap at #2 (inherited from Wikipedia source numbering), v5.0 adds P25-P30 bringing total to 29. The #2 gap is intentional and unchanged.

### 4.1.0
- Reduced from 694 to under 500 lines using progressive disclosure
- Split detailed patterns to PATTERNS.md
- Simplified self-improvement: log only novel discoveries
- Promoted to main SKILL.md: Add Soul section

### 4.0.0
- Added severity tiers and context modes
- Added "When NOT to Use"
- Improved Add Soul with procedural steps
- Simplified self-improvement (made optional)