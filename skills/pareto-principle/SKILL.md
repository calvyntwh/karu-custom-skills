---
name: pareto-principle
description: Strategic Prioritization using the 80/20 Rule. Optimization of Scope. Use when planning tasks, managing feature creep, or maximizing ROI.
license: MIT
---

# The Pareto Principle (The Scope Hammer)

> "80% of consequences come from 20% of the causes."

## When to Use
*   **Planning Phase:** When the task list is long (> 5 items).
*   **Feature Creep:** When a project feels "unfocused" or "heavy".
*   **Refactoring:** Identifying which module is causing 80% of the bugs.

## When NOT to Use

- **Single item:** No prioritization needed.
- **Short list (< 5 items):** Simple ranking is faster and sufficient.
- **Early-stage ambiguity:** When Value cannot be estimated because requirements are unclear.
- **Time-critical delivery:** The overhead of scoring is not worth it for one-off decisions.
- **High-stakes irreversible decisions:** 80/20 is a heuristic; use [decision-matrix](../decision-matrix/SKILL.md) for decisions that are hard to reverse.

## The Protocol: The Scope Hammer

Do not ask "Can we do this?". Ask "Should we do this?".

### Step 0: Pre-Check (Should We?)
Before any scoring, verify the mindset shift:
- Is this about **scope optimization** (what to prioritize) or **option selection** (which one to choose)?
- If option selection → use [decision-matrix](../decision-matrix/SKILL.md) instead.

### Step 1: List & Rate
List every proposed feature or task.
**Ask the User** (or use Proxy Metrics):
*   **Value (V):** User rating 1-10 or ranked.
*   **Effort (E):** Proxy: file count, complexity, dependencies.

> [!IMPORTANT]
> The V/E formula is a tiebreaker, not the core insight. If you can identify the vital few without it, skip the formula.

### Step 2: Add Confidence Modifiers
Rate confidence in each estimate (1-3):

| Confidence | Meaning |
|------------|---------|
| 1 | Speculative (no evidence) |
| 2 | Based on partial data |
| 3 | Based on benchmarks or user research |

Apply discount: `Adjusted Score = (V/E) × (V_conf × E_conf) / 4`

Low-confidence items get penalized automatically.

### Step 3: The Cut (Iterative, Not One-Time)

**Top 20% (High ROI):** DO IT NOW. This is the "Vital Few".
**Middle 60%:** DEFER. Do not touch until Top 20% is complete.
**Bottom 20% (Negative ROI):** DELETE or archive.

> [!WARNING]
> **DEFER is not PERMANENT.** Items in the middle 60% should be re-evaluated after each Top 20% item is completed. The backlog changes; so should the prioritization.

### Step 4: Re-Cut Trigger
After completing each Top 20% item:
1. Recalculate ROI for remaining items (dependencies may have changed)
2. Ask: "Has context shifted? Any deferred items now have higher Value?"
3. Re-cut if necessary

## Timeboxing

- **Maximum list size before simplification:** 20 items. Beyond this, use grouping.
- **Scoring time budget:** 5 minutes per item. If V or E cannot be estimated in that time, default to V=5, E=5 (score=1) and mark as uncertain.
- **Re-cut frequency:** After each Top 20% completion, or bi-weekly for long-running projects.

## Defer/DELETE Safeguard

Before labeling an item DELETE, ask:
- "Will deleting this increase effort on remaining items?" (dependency)
- "Will this become more expensive to build later?" (technical debt)
- "Is this a 'trivially deferred' item that will become critical?" (scope creep pattern)

If yes to any → Move to DEFER instead.

Before labeling an item DEFER, ask:
- "Can this be completed in < 2 hours?" If yes, just do it now.
- "Is this a dependency blocker for Top 20% items?" If yes, elevate it.

## Validation Steps

Before the final cut:
1. **Confirm distribution:** Does 80/20 actually hold in your domain? Validate with historical data if possible.
2. **Check non-negotiables:** Does any item violate a hard constraint (security, compliance)? Elevate regardless of ROI.
3. **Saboteur check:** [inversion-thinking](../inversion-thinking/SKILL.md) - How could this prioritization backfire?

## Skill Integration

| Situation | Use Instead/Also |
|-----------|------------------|
| Choosing between options | [decision-matrix](../decision-matrix/SKILL.md) |
| Need to verify value estimates | [map-vs-territory](../map-vs-territory/SKILL.md) |
| Criteria might be wrong | [chestertons-fence](../chestertons-fence/SKILL.md) |
| Risk of over-analysis | [occams-razor](../occams-razor/SKILL.md) |
| Preventing deferral from becoming permanent | [inversion-thinking](../inversion-thinking/SKILL.md) |
| Understanding cascading effects | [second-order-thinking](../second-order-thinking/SKILL.md) |

## Self-Improvement Protocol

**Log only if prediction was wrong.**

```markdown
## [YYYY-MM-DD] {Brief Description}
**Action:** {what was prioritized / deferred / deleted}
**Outcome:** {did it work?}
**Lesson:** {one sentence}
```

**Review Trigger:** Monthly → check CORRECTIONS.md → promote validated patterns to LEARNINGS.md.

**Defer Watch:** If an item has been "DEFER" for > 3 months, explicitly ask user: "Is this still DEFER or should it be DELETE?"

## Resources
*   [Detailed Research Notes](references/research.md)
*   [Impact Matrix Reference](references/impact_matrix.md)

---

## Evaluations

### Eval 1: Option Selection vs Scope Optimization
**Scenario:** User asks "React vs Vue for our startup."
**Expected:** Identifies as option selection, redirects to decision-matrix (not pareto).
**Pass criteria:** Correctly distinguishes "what to prioritize" from "which to choose", applies right skill.

### Eval 2: Low-Effort Quick Win Detection
**Scenario:** List has 10 items. One item is "Update README" with V=5, E=1.
**Expected:** Identifies as Top 20%, flags as "do in < 2 hours" for immediate execution.
**Pass criteria:** Catches quick win that would be lost in formal scoring, recommends doing now.

### Eval 3: Defer Permanence Prevention
**Scenario:** Feature has been "DEFER" for 3+ months.
**Expected:** Flags for explicit user decision (DELETE or keep deferred), prevents permanent deferral.
**Pass criteria:** Asks user explicitly after 3 months, does NOT allow indefinite deferral.
