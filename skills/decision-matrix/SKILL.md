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

### 3. Assign Weights (WITH USER)
Ask the user to rate the importance of each criterion.

| Weight | Meaning |
| :--- | :--- |
| 1 | Nice to have |
| 2 | Moderately important |
| 3 | Very important |
| 4 | Critical / Non-negotiable |

### 4. Score Options
Rate each option against each criterion (1-5 scale).
*   1 = Poor
*   3 = Adequate
*   5 = Excellent

*You (the agent) can score based on research, but weights come from the user.*

### 5. Calculate Weighted Scores
For each option: `Total = Σ (Score × Weight)`

### 6. Recommend & Verbalize
Present the matrix and state the winner with reasoning.

*   "Based on your priorities (Performance=Critical, Learning Curve=Important), **Vue** scores highest because..."

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

## Self-Improvement Protocol

This skill learns from decisions to improve future trade-off analysis.

### Logging Corrections

After a decision made using this matrix:

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Decision:** {what was chosen}
**Outcome:** {how did it turn out? Correct or wrong?}
**Criteria accuracy:** {were the weights right?}
**Pattern:** {lessons learned}
---
```

### Trigger Conditions

| Condition | Example | Log? |
|-----------|---------|------|
| Chose option that failed | "The winner turned out to be wrong" | ✅ |
| Weights were wrong | "Should have weighted learning curve higher" | ✅ |
| Missing criteria discovered | "Security should have been a criteria" | ✅ |
| Outcome matched prediction | "Framework held up well under load" | ✅ |
| False positive | "Matrix said X but Y was clearly better" | ✅ |

### Pattern Categories for This Skill

- **Weight calibration errors**: Over/under weighting criteria
- **Missing criteria**: Security, team familiarity, maintenance
- **Score accuracy**: Model predictions vs reality
- **Bias patterns**: Popularity bias, anchoring bias
- **Context failures**: Criteria that worked in one context but not another

### Review & Promote

**Monthly:** Check CORRECTIONS.md → Promote validated patterns to LEARNINGS.md

## Resources
*   [Detailed Research Notes](references/research.md)
