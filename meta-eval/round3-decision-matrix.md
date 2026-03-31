# Meta-Evaluation: decision-matrix

## 1. chestertons-fence

**What it reveals:** The skill has built-in "fences" that protect against misuse. The pre-check gate (step 0) preventing matrix use for 2-option decisions is a fence—it guards against over-engineering a simple choice. The requirement that "You MUST ask the user for criteria" is a load-bearing fence preventing the agent from imposing external biases.

**Weaknesses:** The fence at step 0 (Occam's Razor pre-check) is incomplete—it only gates 2 options but doesn't address when options are fundamentally incommensurable (e.g., "adopt React" vs "build custom framework"). The user-weighted criteria fence is strong, but the agent-scoring step has no equivalent guard ensuring scores reflect objective reality vs agent assumptions.

**Enhancement:** Add a Chesterton's Fence checkpoint before scoring: "Before scoring, verify each score against documented reality (docs, benchmarks), not assumption. Can you cite evidence for each 1-5 rating?"

---

## 2. decision-matrix (Self-Referential)

**What it reveals:** Applying the skill to itself is revealing. Using a decision-matrix to evaluate a decision-matrix:

| Criterion | Weight | Score (1-5) |
|-----------|--------|-------------|
| Clarity of instructions | 4 | 4 |
| Bias elimination | 4 | 3 |
| Ease of use | 3 | 4 |
| Self-improvement mechanism | 3 | 3 |
| Handles edge cases | 2 | 2 |

**Total: 64/70 potential.** The skill scores well on clarity but loses points on bias elimination (agent still influences scores) and edge cases (no guidance on incommensurable options, false precision from 1-5 scale).

**Weaknesses:** The skill cannot score itself on "objectivity" because the scoring itself is subjective. The self-improvement protocol exists but has zero corrections logged—indicating either no feedback loop or inactive usage.

**Enhancement:** Add a self-referential step: "After 3 uses, audit whether the matrix recommendations matched outcomes. If >30% mismatch, re-calibrate your scoring patterns."

---

## 3. first-principles-thinking

**What it reveals:** Weighted decision-making rests on a basic truth: **"Preferences are knowable and comparable."** This assumption—that a user can meaningfully rate criteria importance (1-4) and that these ratings are commensurable with other users' ratings—is the foundation. If this assumption fails (user unsure, preferences are contextual), the entire framework collapses.

**Weaknesses:** The skill assumes preferences are stable and articulated. It doesn't handle:
- Users who discover preferences through the act of evaluation
- Criteria that are negatively correlated (high X means low Y)
- The possibility that "weight" itself is multidimensional (urgency vs importance vs risk tolerance)

**Enhancement:** Add a Socratic questioning phase: "Before weighting, ask: Do these criteria conflict? Are you comparing apples to oranges? Can you rank these criteria against each other directly (A vs B: which matters more)?"

---

## 4. inversion-thinking

**How this skill leads to bad decisions:**

| Anti-Goal | Sabotage Pathway |
|-----------|------------------|
| Choose the wrong option | Agent inflates scores for preferred option |
| Paralysis by analysis | Too many criteria (10+) make calculation meaningless |
| Commitment to bad choice | Finality bias after matrix produces a "winner" |
| Ignore the matrix | User overrides based on gut feel, negating the process |

**Concrete pathways:**
- "I'll score my preferred option 5 on every criterion even if evidence says 3"
- "Add 15 criteria so the weights become statistically meaningless"
- "After Vue 'wins', sunk cost prevents reconsidering when Vue 4 is released"

**Enhancement:** Add inversion checkpoint: "Before presenting results, ask: How could someone game this matrix to get their desired answer? What if I already prefer one option—have I scored honestly?"

---

## 5. map-vs-territory

**Does the 1-5 scoring match real-world option quality?**

**The Map says:**
- 1 = Poor, 3 = Adequate, 5 = Excellent

**The Territory reality:**
- "Poor" and "Excellent" are context-dependent. React's performance (score 4) might be "Poor" for a 60fps mobile game but "Excellent" for an internal dashboard.
- The 1-5 scale assumes interval properties (distance from 1 to 2 equals 2 to 3) that don't hold in practice.
- Score 3 "Adequate" is a vague anchor that absorbs extreme variation.

**Weaknesses:** No guidance on anchoring the scale to specific, measurable criteria. "You (the agent) can score based on research" without requiring benchmarks means scores are impressionistic.

**Enhancement:** Mandate evidence anchors: "For each score of 1 or 5, cite a specific data point. 'Performance: 4' must mean 'benchmark X shows 95th percentile on metric Y.' If you cannot cite evidence, default to 3 and note uncertainty."

---

## 6. occams-razor

**Can the scoring methodology be simplified?**

**Yes.** The 1-5 scale with weights 1-4 creates 20 distinct score combinations per criterion, but most of this granularity is noise:
- Weight 2 vs Weight 3 is a subjective distinction that rarely maps to measurable difference
- Score 2 vs Score 3 is similarly fuzzy

**The simplification opportunity:** Reduce to binary weights (Important / Critical) and binary scores (Meets / Doesn't meet requirements). This eliminates false precision while preserving the core logic: "Does this option satisfy my non-negotiables?"

**When to keep the full matrix:** Only when comparing 4+ options with 5+ criteria where marginal differences matter.

**Enhancement:** Add a complexity gate: "If criteria are truly independent and user can clearly rank them, use the full 1-5/1-4 matrix. If criteria are vague or interdependent, collapse to binary and use decision-matrix only to confirm, not to choose."

---

## 7. pareto-principle

**What criteria should always be weighted highest?**

**The Pareto insight:** In technology decisions, 20% of criteria typically cause 80% of the regret.

**Based on the skill's own correction patterns, these should default to high weight:**
1. **Team familiarity** (Weight 4 default)—learning curve dominates long-term productivity
2. **Maintenance burden** (Weight 4 default)—code outlives initial development
3. **Exit cost** (Weight 3 default)—how hard is it to reverse this decision?

**Weaknesses:** The skill explicitly forbids defaulting criteria ("Do not invent criteria based on general knowledge"). This prevents helpful defaults but leaves users unguided on universal high-impact factors.

**Enhancement:** Add a Pareto-prescribed minimum: "Regardless of user preference, always surface these as considerations: Maintenance (long-term cost), Reversibility (can we undo this?), and Team Buy-in (will they actually use it?). Do not weight these for the user, but ensure they appear in the criteria list."

---

## 8. rubber-ducking

**Walk through an example. Where does the logic break down?**

**Scenario:** User wants to choose between three job offers.

**User's stated criteria and weights:**
| Criterion | Weight |
|-----------|--------|
| Salary | 4 |
| Location | 3 |
| Growth | 2 |

**Agent scoring:**
| Option | Salary (×4) | Location (×3) | Growth (×2) | Total |
|--------|------------|--------------|-------------|-------|
| A | 5 (20) | 3 (9) | 2 (4) | 33 |
| B | 4 (16) | 4 (12) | 4 (8) | 36 |
| C | 3 (12) | 5 (15) | 5 (10) | 37 |

**Ducking the logic:**
1. "We sum weighted scores to find the winner" → What if the user's *real* priority is "don't regret choosing"? The matrix optimizes for weighted sum, not regret minimization.
2. "Higher total = better choice" → This assumes preferences are transitive (if A>B and B>C, then A>C). Behavioral economics shows this is false.
3. "Score of 5 means excellent" → What does "excellent salary" mean? $150k? $200k? The map (score) doesn't match territory (actual numbers).

**The breakdown:** The matrix assumes revealed preferences are true preferences. But users often have:
- Unstated constraints ("I can't relocate to Seattle")
- Non-compensatory rules ("No matter the salary, I won't work for Company X")
- Preference reversals when seeing actual numbers

**Enhancement:** Add duck-check: "Before finalizing, ask: Are any of your criteria actually non-compensatory? (e.g., 'I would never take a job in Seattle no matter the salary'). If yes, filter those options first before running the matrix."

---

## 9. systems-thinking

**How do criteria weights interact over time?**

**The interactions are non-linear and often forgotten:**

1. **Weight interaction:** High weight on "Learning Curve" (4) combined with high weight on "Ecosystem" (3) creates a hidden interaction—React's large ecosystem makes its learning curve *easier* to overcome. But the matrix treats these as independent.

2. **Feedback loops over time:**
   - Choosing high-weight "Performance" option → team optimizes for performance → other criteria (maintainability) degrade → next decision cycle, maintainability becomes crisis
   - Low weight on "Security" initially → breach occurs → security becomes Weight 5 forever (hysteresis)

3. **Delayed consequences:**
   - Weight "Hiring Pool" at 2 today → 18 months later, can't find React developers → decision-matrix failed to model future state

**Weakness:** The matrix is synchronous—it captures a single moment's preferences against current options. It has no mechanism for tracking how today's weights create tomorrow's constraints.

**Enhancement:** Add temporal loop check: "Ask the user: How might these weights change in 12 months? Which criteria today might become non-negotiable tomorrow? Flag any criteria with high future uncertainty for explicit discussion."

---

## 10. second-order-thinking

**What cascading effects might a decision made by this skill cause?**

**First-order:** "Vue scores highest (40), so we recommend Vue."

**Second-order effects:**

| Cascade | Description |
|---------|-------------|
| **Commitment escalation** | Team invests in Vue → Vue 4 released with breaking changes → matrix said "Vue wins" so team resists migration |
| **Anchoring on weights** | Initial weights become permanent reference → market shifts but weights don't update → decision-matrix recommends suboptimal choice for 2 years |
| **Agent authority amplification** | "The matrix chose it" becomes political cover → agent's scoring biases get embedded in organizational decisions |
| **Skill atrophy** | Users outsource judgment to matrix → team loses ability to make intuitive decisions when matrix is inappropriate |
| **Precedent lock-in** | "We used decision-matrix for React vs Vue, now we must use it for every architectural decision" |

**The dangerous cascade:** A single decision-matrix recommendation, treated as authoritative, creates path dependency that makes subsequent matrix use less valuable (team stops questioning the process) but more confident (data feels objective).

**Enhancement:** Add second-order disclaimer: "This matrix reflects current preferences and current options. The winner is not 'correct'—it is the best match to your stated weights today. Revisit this decision when options or weights change. Document this decision so future-you can understand the context, not just the result."

---

## Summary

### Strengths
- **Clear protocol:** Step-by-step structure is implementable and trainable
- **User-weighted criteria:** Correctly delegates values to the user, not the agent
- **Pre-check gate:** The 2-option skip prevents over-engineering simple decisions
- **Self-improvement mechanism:** Logging framework exists for corrections and learnings
- **Honest about limitations:** "Eliminate popularity bias" is a realistic goal, not overselling

### Weaknesses
- **False precision:** 1-5 scale with 1-4 weights implies accuracy that doesn't exist
- **No evidence requirement:** Scoring without citations divorces the map from territory
- **Incomplete edge case handling:** No guidance for incommensurable options, non-compensatory criteria, or non-transitive preferences
- **Static weights:** No mechanism for weight evolution as context changes
- **Inactive feedback loop:** CORRECTIONS.md has zero entries—either unused or unmaintained
- **No conflict detection:** Doesn't surface when criteria conflict or when options are incomparable
- **Binary outcome:** Produces a "winner" when the honest answer is often "insufficient data to distinguish"

### Enhancement Recommendations

1. **Evidence anchoring:** Require citation for scores of 1 or 5; default uncertain scores to 3 with uncertainty notation
2. **Non-compensatory filter:** Before matrix, filter out options that violate non-negotiable constraints (e.g., "must support IE11")
3. **Conflict detection:** Add step to identify negatively correlated criteria and warn about interaction effects
4. **Uncertainty output:** Instead of single-point recommendation, output "Vue: 38-42, React: 36-40" with confidence ranges
5. **Temporal review trigger:** Set a 6-month review checkpoint in the output, not just the self-improvement log
6. **Activation metric:** Track decision-matrix usage; if unused for 60+ days, prompt user to review LEARNINGS.md before next use
7. **Simplification path:** Explicitly branch to Pros/Cons or binary filter when matrix complexity isn't warranted
