---
name: decision-matrix
description: Objective trade-off analysis using weighted criteria. Eliminates popularity bias by requiring user-defined priorities. Use when choosing between technologies, architectures, or vendors.
license: MIT
---

# Decision Matrix (The Bias Eliminator)

> "When you can measure what you are speaking about... you know something about it." - Lord Kelvin

## When to Use
*   **Technology Choices:** "Should we use React or Vue?"
*   **Architecture Decisions:** "Monolith vs Microservices?"
*   **Vendor Selection:** "AWS vs GCP vs Azure?"
*   **Any Multi-Option Decision:** When there are 3+ options and no obvious winner.

## When NOT to Use

- **2 options or fewer:** Use Pros/Cons instead. Matrix adds overhead without benefit.
- **Incommensurable options:** Cannot compare "adopt React" vs "build custom framework" if the evaluation criteria cannot be objectively measured.
- **Non-compensatory criteria:** If any criterion is an absolute blocker (e.g., "must support IE11"), filter those options first.
- **High uncertainty / no data:** When you cannot evidence any scores, the matrix produces false precision.
- **Already decided:** If the user has already chosen, the matrix will confirm rather than inform.

## The Protocol: Weighted Scoring

### 0. Pre-Check (Occam's Razor)
*   **2 Options Only?** Skip the matrix. Use a simple Pros/Cons list.
*   **3+ Options?** Proceed with the full matrix.

### 1. List Options
Enumerate all viable choices.
*   *Example:* React, Vue, Svelte, Angular

### 2. Define Criteria (WITH USER)
Ask the user for their **Top 3-5** evaluation criteria.

> [!IMPORTANT]
> **You MUST ask the user for criteria.**
> Do not invent criteria based on general knowledge. The user's context defines what matters.

*   *Example Criteria:* Performance, Learning Curve, Ecosystem Size, Bundle Size, Hiring Pool

### 3. Check for Conflicts
Before proceeding, ask the user:
- "Do any of these criteria conflict with each other?" (e.g., "max performance" vs "min bundle size")
- "Is any criterion non-negotiable — meaning if any option fails it, it's automatically disqualified?"

If yes, filter out disqualified options before scoring.

### 4. Assign Weights (WITH USER)
Ask the user to rate the importance of each criterion.

| Weight | Meaning |
| :--- | :--- |
| 1 | Nice to have |
| 2 | Moderately important |
| 3 | Very important |
| 4 | Critical / Non-negotiable |

### 5. Score Options (with Evidence)
Rate each option against each criterion (1-5 scale).

| Score | Meaning | Evidence Required |
|-------|---------|-------------------|
| 1 | Poor | Must cite specific data point |
| 3 | Adequate | Default if uncertain |
| 5 | Excellent | Must cite specific data point |

> [!WARNING]
> **No evidence = Score 3.** If you cannot cite benchmarks, docs, or user research, default to "Adequate" (3). Do not guess.

*You (the agent) can score based on research, but weights come from the user.*

### 6. Calculate Weighted Scores
For each option: `Total = Σ (Score × Weight)`

Present results as a range: "Vue: 38-42, React: 36-40" to acknowledge uncertainty.

### 7. Recommend & Verbalize
Present the matrix and state the winner with reasoning.

*   "Based on your priorities (Performance=Critical, Learning Curve=Important), **Vue** scores highest because..."

### 8. Set Review Trigger
Set a 6-month review checkpoint. Log this decision to `.learnings/REVIEW.md`.

## Validation Steps

Before presenting results, verify:
1. **Non-compensatory filter applied:** Were hard constraints checked first?
2. **Conflict detection done:** Were negatively correlated criteria surfaced?
3. **Evidence anchoring:** Did you cite evidence for scores of 1 or 5?
4. **Uncertainty notation:** Did you use ranges for high-uncertainty outputs?

## Timeboxing

- **Maximum criteria:** 7 (beyond this, weights become statistically meaningless)
- **Maximum options:** 10 (beyond this, scoring becomes inconsistent)
- **Time budget:** If analysis exceeds 30 minutes, simplify to binary (Meets/Doesn't meet) or Pros/Cons

## Example

**User Goal:** Choose a frontend framework for a small team with tight deadlines.

**User Criteria & Weights:**
| Criterion | Weight |
| :--- | :--- |
| Learning Curve | 4 |
| Performance | 2 |
| Ecosystem | 3 |

**Agent Scoring:**
| Option | Learning (×4) | Perf (×2) | Ecosystem (×3) | **Total** |
| :--- | :--- | :--- | :--- | :--- |
| React | 3 (12) | 4 (8) | 5 (15) | **35** |
| Vue | 5 (20) | 4 (8) | 4 (12) | **40** ✅ |
| Angular | 2 (8) | 4 (8) | 5 (15) | **31** |

**Recommendation:** "Vue scores highest (40) primarily due to its excellent Learning Curve score, which you rated as Critical."

## Skill Integration

| Situation | Use Instead/Also |
|-----------|------------------|
| 2 options | [Pros/Cons](../rubber-ducking/SKILL.md) or [rubber-ducking](../rubber-ducking/SKILL.md) |
| Need to validate scores | [map-vs-territory](../map-vs-territory/SKILL.md) |
| Criteria might be wrong | [chestertons-fence](../chestertons-fence/SKILL.md) |
| Risk of over-analysis | [occams-razor](../occams-razor/SKILL.md) |
| Need to understand second-order effects | [second-order-thinking](../second-order-thinking/SKILL.md) |
| Prioritizing a backlog | [pareto-principle](../pareto-principle/SKILL.md) |

## Self-Improvement Protocol

After a decision is made, log to `.learnings/CORRECTIONS.md` **only if** the outcome differed from prediction. Keep entries brief:

```markdown
## [YYYY-MM-DD] {Brief Description}
**Decision:** {what was chosen}
**Outcome:** {Correct or wrong?}
**Lesson:** {one sentence}
```

**Review Trigger:** If no entries in 60+ days, the self-improvement loop is inactive. Resume by reviewing `.learnings/LEARNINGS.md` before next use.

**Promote:** Monthly, check CORRECTIONS.md → move validated lessons to LEARNINGS.md.

## Resources
*   [Detailed Research Notes](references/research.md)
