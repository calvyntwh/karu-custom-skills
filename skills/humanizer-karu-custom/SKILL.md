---
name: humanizer-karu-custom
version: 4.1.0
description: |
  Remove signs of AI-generated writing from text. Use when editing text to make it
  sound more natural and human-written. Based on Wikipedia's "Signs of AI writing" guide.
  Addresses: inflated symbolism, promotional language, em dash overuse, AI vocabulary,
  filler phrases, sycophantic tone, and other patterns. For full pattern reference, see PATTERNS.md.
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
2. **Em Dash Overuse**: Multiple em dashes in close proximity
3. **Filler Phrases**: In order to, due to the fact that, at this point in time
4. **Inflated Significance**: Pivotal moment, testament, underscores the importance
5. **Promotional Language**: Breathtaking, groundbreaking, renowned, nestled
6. **Sycophantic Tone**: Great question!, You're absolutely right!, Excellent point

### Tier 2: MEDIUM Impact (Address when clearly present)
7. **Superficial -ing Analyses**: Highlighting, underscoring, reflecting
8. **Vague Attributions**: Experts believe, some critics argue
9. **Rule of Three Overuse**: Innovation, inspiration, industry insights
10. **Negative Parallelism**: Not only...but..., It's not just...it's...
11. **Copula Avoidance**: Serves as, stands as, boasts
12. **Generic Positive Conclusions**: Exciting times lie ahead, major step forward

### Tier 3: LOW Impact (Address selectively)
13. Elegant Variation (synonym cycling)
14. Boldface Overuse
15. Inline-Header Lists
16. Title Case in Headings
17. False Ranges
18. Excessive Hedging
19. Collaborative Artifacts (I hope this helps...)
20. Emojis

**Deprecated**: Curly quotes, knowledge-cutoff disclaimers (do not apply)

**Full pattern details**: See [PATTERNS.md](PATTERNS.md)

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
3. **Add specifics**: names, dates, numbers
4. **Include contradiction**: "It's impressive, but also unsettling"
5. **Use first-person** where it fits
6. **Allow imperfection**: tangents, unfinished thoughts

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