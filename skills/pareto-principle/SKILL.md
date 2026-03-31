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

## The Protocol: The Scope Hammer
Do not ask "Can we do this?". Ask "Should we do this?".
Follow these 3 steps.

### 1. List & Rate
List every proposed feature or task.
**Ask the User** (or use Proxy Metrics):
*   **Customer Value (V):** Ask user to rate 1-10 or rank items.
*   **Effort Cost (E):** Proxy: "Number of files touched" or "Complexity of dependencies".

### 2. Calculate ROI
Score = $V / E$ (Value divided by Effort).

### 3. The Cut (80/20)
*   **Top 20% (High ROI):** DO IT NOW. This is the "Vital Few".
*   **Middle 60%:** DEFER. Do not touch until the Top 20% are perfect.
*   **Bottom 20% (Negative ROI):** DELETE. This is the "Trivial Many".

## Example
| Task | Value | Effort | Score | Action |
| :--- | :--- | :--- | :--- | :--- |
| **Core Payment API** | 10 | 5 | **2.0** | **BUILD** |
| **Dark Mode** | 3 | 2 | 1.5 | DEFER |
| **Animated Logo** | 1 | 8 | 0.1 | **DELETE** |

## Self-Improvement Protocol

This skill learns which prioritization decisions work out.

### Logging Corrections

After applying Pareto Principle:

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Task prioritized:** {what was chosen}
**Task deferred/deleted:** {what was not done}
**Outcome:** {did the prioritization work?}
**Value estimate accuracy:** {was the V rating correct?}
---
```

### Trigger Conditions

| Condition | Example | Log? |
|-----------|---------|------|
| Defer was wrong | "Should have built Dark Mode first" | ✅ |
| Delete was wrong | "The 'trivial' feature was actually important" | ✅ |
| Value estimate off | "Users didn't care about the 'core' feature" | ✅ |
| Effort estimate wrong | "Thought it was 2, turned out to be 10" | ✅ |
| 80/20 was wrong | "The 20% wasn't the vital one" | ✅ |

### Pattern Categories for This Skill

- **Value misprediction**: What users actually want vs what we thought
- **Effort estimation errors**: Complexity surprises
- **Scope creep patterns**: When deferral became permanent
- **ROI calculation errors**: Wrong V/E assumptions
- **Feature dependencies**: Tasks that blocked others

### Review & Promote

**Weekly:** Check CORRECTIONS.md → Promote validated patterns to LEARNINGS.md
