# Research: Decision Matrix / Weighted Scoring Model

## Origin
**Also Known As:** Weighted Decision Matrix, Prioritization Matrix, Pugh Matrix.
**Core Concept:** Quantify subjective decisions by scoring options against weighted criteria.

## Why It Works
1.  **Forces Explicit Trade-offs:** You cannot hide behind "it depends." You must assign numbers.
2.  **Reduces Bias:** The agent's preference is overridden by user-defined weights.
3.  **Creates Audit Trail:** The matrix is a document that justifies the decision.

## The Core Formula
```
Total Score = Σ (Option Score for Criterion × Criterion Weight)
```

## Key Principles

### 1. Weights Come From the User (Bias Prevention)
An AI will default to its training biases (popularity, recency).
Forcing the *user* to define weights ensures the decision reflects *their* context.

### 2. Limit Criteria (Pareto Principle)
More than 5 criteria adds noise without improving signal.
Focus on the "Vital Few" that actually differentiate the options.

### 3. Include "Switching Cost" (Systems Thinking)
If the user is already using something, the cost of migration is a hidden criterion.
Add "Migration Effort" or "Lock-in Risk" as a weighted factor.

## Common Pitfalls
*   **Gaming the Weights:** Agent assigns weights to guarantee its preferred option.
    *   *Fix:* User must approve weights before scoring.
*   **False Precision:** Scores like 4.7 vs 4.8 are noise.
    *   *Fix:* Use integer scales (1-5).
*   **Ignoring Qualitative Factors:** Not everything can be scored (e.g., "Team morale").
    *   *Fix:* Note unquantifiable factors separately.

## Resources & Verified References
*   [Airfocus: Weighted Decision Matrix](https://airfocus.com/glossary/what-is-a-weighted-decision-matrix/)
*   [Lucidchart: How to Make a Decision Matrix](https://www.lucidchart.com/blog/decision-matrix)
*   [Wrike: Decision Matrix Analysis](https://www.wrike.com/blog/decision-matrix-analysis/)
