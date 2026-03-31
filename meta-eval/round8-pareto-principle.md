# Meta-Evaluation: pareto-principle

## 1. chestertons-fence

**What it reveals:** The 80/20 rule itself functions as a "fence" — a meta-level constraint against scope creep and over-planning. It forces a hard stop at the vital few, preventing unlimited expansion. The fence exists because unbounded task lists are the default failure mode in project planning.

**Weaknesses:** The fence has a blind spot — it assumes the cut was made for the right reasons. If the original categorization (what goes in the Top 20%) is wrong, the fence locks in the wrong priorities. The skill's self-improvement protocol (Section 7) is the attempt to detect when the fence itself is misplaced, but there's no explicit "Chesterton check" on the V/E inputs before the cut is made.

**Enhancement:** Add a pre-cut sanity check: "Before the 80/20 cut, can you explain why the Top 20% items were rated high-value AND low-effort? If you can't explain it, invoke chestertons-fence to investigate before cutting."

---

## 2. decision-matrix

**What it reveals:** The pareto-principle and decision-matrix are complementary but distinct. Decision-matrix is for *choosing between options* (which framework, which vendor) using weighted multi-criteria scoring. Pareto is for *prioritizing a backlog* (which tasks to do first) using a single V/E ratio. They address different phases: matrix before the list is finalized, Pareto after you have a list of things you might do.

**Weaknesses:** The two skills don't cross-reference. A task with high ROI under Pareto might score poorly on a decision-matrix criteria the user cares about (e.g., team morale, security). There's no warning that Pareto's V/E score ignores criteria that are *non-negotiable*.

**Enhancement:** At step 2 (Calculate ROI), add a check: "Does any item have V=10 but violates a hard constraint (security, compliance, team dealbreaker)? If yes, elevate it regardless of ROI." Cross-reference decision-matrix's weighted criteria as a filter before ROI is calculated.

---

## 3. first-principles-thinking

**What it reveals:** The basic truth beneath Pareto is the *power law distribution* — in many systems, outputs are disproportionately driven by inputs. This is a first principle in economics and physics (Pareto originally observed it in land ownership in Italy). The skill correctly grounds itself in this truth rather than treating 80/20 as a magic number.

**Weaknesses:** The skill never states *why* 80/20, just that it *is*. A first-principles decomposition of the ratio itself is absent: Is 80/20 a fixed law or an approximation? Does it vary by domain? What evidence is it based on? The skill treats it as a given.

**Enhancement:** Add a "First Principles Check" in the protocol: "Before applying 80/20, verify the distribution actually holds. In your specific domain, is it 80/20, 90/10, or 70/30? Use historical data or user validation to confirm before the cut."

---

## 4. inversion-thinking

**What it reveals:** Prioritization can backfire. The Saboteur question: "How could prioritizing the Top 20% create new problems?" If you always chase the vital few, you defer indefinitely items that might be *enablers* — prerequisites that unlock the next tier of work. The deferral itself becomes permanent (a known failure pattern in the skill's own logs).

**Weaknesses:** The skill has no explicit failure mode analysis. "DEFER" is the default for the middle 60%, but there's no protocol to prevent "defer forever." The only feedback is a post-hoc correction log — no proactive sabotage check exists.

**Enhancement:** Add a "Saboteur Check" before labeling items DEFER: "Can this deferred item become more expensive or impossible to do later due to dependency lock-in, market changes, or team turnover? If yes, it may need to move up regardless of current ROI."

---

## 5. map-vs-territory

**What it reveals:** The ROI formula `Score = V / E` is a map. Value and Effort are *estimates*, not territory. The skill acknowledges in the self-improvement protocol that "Value estimate accuracy" and "Effort estimation errors" are known failure patterns, but the main protocol doesn't include a reality check before the calculation runs.

**Weaknesses:** The skill assumes V and E are knowable at the time of rating. In practice, Value is often speculative (user said they'd use it), and Effort is estimation (it was wrong in 40% of the logged corrections). The map-territory gap is the primary source of Pareto failures.

**Enhancement:** Add a confidence modifier: "Rate your confidence in the V estimate (1-3) and E estimate (1-3). Multiply the final score by (V_confidence × E_confidence) / 4. Low-confidence items get a discount. This makes the 'map' explicitly uncertain before you trust it."

---

## 6. occams-razor

**What it reveals:** The pareto-principle *is* an Occam's Razor for project planning — it cuts the fat from a bloated task list. The "Scope Hammer" framing is literally a pruning metaphor. The three-step protocol (List → Score → Cut) is the simplest possible prioritization method, which is a strength.

**Weaknesses:** The skill has a structural complexity problem — the self-improvement protocol is 40% of the file but is not referenced in the main protocol flow. The corrections log, trigger conditions, and pattern categories are all valuable but add cognitive overhead that could undermine the simplicity goal.

**Enhancement:** The self-improvement protocol is valuable but optional for initial use. Split into two files: SKILL.md (core 3-step protocol, under 40 lines) and LEARN.md (self-improvement details). This preserves the Occam simplicity for first-time use while keeping depth accessible.

---

## 7. pareto-principle (self-referential)

**What it reveals:** The 20% of this skill that provides 80% of the value is: Step 1 (List & Rate) + Step 3 (The Cut). The ROI calculation in Step 2 is actually the least important part — it just sorts the list. If you can identify the vital few without the formula, the skill still works. The formula is a tiebreaker and a rationalization layer, not the core insight.

**Weaknesses:** The skill over-emphasizes the V/E formula as the mechanism when it's really just window dressing on "do the important things first." The most valuable part (the mindset shift from "can we do this?" to "should we?") is buried in the protocol intro.

**Enhancement:** Elevate the mindset framing ("Do not ask Can we do this? Ask Should we do this?") to be Step 0 at the top of the protocol. The ROI formula should be labeled as optional or a tiebreaker, not the central mechanism.

---

## 8. rubber-ducking

**What it reveals:** Walking through the ROI calculation step by step reveals multiple failure points:

1. **Value is not Value** — "Customer Value" conflates user-reported desire (stated preference) with actual utility (revealed preference). A user rating Dark Mode as V=3 may actually *use it every day* once built.

2. **Effort is not Effort** — "Number of files touched" is a complexity proxy, not time. A 1-file change might require a major refactor; a 5-file change might be a copy-paste pattern.

3. **V/E is not ROI** — The formula implies diminishing returns and linear separability. In reality, V and E are often correlated (high-value features are often high-effort) and interactions between features matter (building A makes B trivial, or B necessary).

4. **The Cut is arbitrary** — 80/20 is applied to the *output* of the formula, not the input. The formula doesn't guarantee the top 20% by score actually represents 80% of value. It's a coincidence of numbers.

**Enhancement:** Add a worked example that walks through each failure mode explicitly, so users understand the formula is a heuristic, not a measurement. The example table in the skill (Section 5) doesn't show where V or E was wrong.

---

## 9. systems-thinking

**What it reveals:** Priorities are not static. The Pareto cut assumes a snapshot at a point in time, but completing top-20% items changes the system: new dependencies emerge, the backlog's composition changes, team capabilities evolve, and user needs shift. The "Vital Few" at project start may not be the Vital Few at project end.

**Weaknesses:** The skill is single-shot — it's designed for a one-time cut, not iterative re-evaluation. There's no loop. The self-improvement protocol is post-hoc, not real-time. No reinforcing or balancing loop is identified within the protocol itself.

**Enhancement:** Add a "Re-cut" trigger: "After completing each Top 20% item, re-run the ROI calculation on the remaining items. The completed item may have changed the Value of remaining items (dependencies satisfied, context gained) and the Effort of remaining items (shared infrastructure built)." Make it a loop, not a one-time cut.

---

## 10. second-order-thinking

**What it reveals:** Chasing the Top 20% has cascading second-order effects:

- **First-order:** You ship high-ROI items fast.  
- **Second-order:** The deferred middle 60% accrues technical debt and becomes more expensive over time (the "scope creep" the skill tries to prevent becomes the output of the strategy itself).  
- **Third-order:** The team optimizes for measurable ROI, which trains users/ stakeholders to only ask for *measurable* value — intangible value (security, documentation, refactoring) gets systematically deleted because its V≈0 in the formula.  
- **Cobra Effect:** Deleted "trivial" features become critical when downstream work reveals they were dependencies. The formula predicted their deletion was safe.

**Weaknesses:** The skill has no time horizon analysis. 80/20 applied in month 1 of a project produces different outcomes than 80/20 applied in month 12. The temporal dimension is completely absent.

**Enhancement:** Add a time horizon dimension to the cut: "For items in the Bottom 20%, what is the cost of deleting them *now* vs deleting them *after* the top 20% is complete? If the cost is significantly higher later (dependency growth, market shift, team churn), move them to DEFER instead of DELETE."

---

## Summary

### Strengths
- **Concrete and actionable:** The 3-step protocol is immediately usable without training.
- **Correct core insight:** The mindset shift from "can we?" to "should we?" is the most valuable part.
- **Self-improvement infrastructure:** Corrections logging and pattern categories are well-designed for skill growth.
- **Applies universally:** The 80/20 framing is domain-agnostic and memorable.

### Weaknesses
- **Over-reliance on V/E formula:** Treated as precise when it's a rough heuristic with known failure modes.
- **No loop structure:** Designed as a one-time cut, not an iterative re-evaluation.
- **Temporal blindness:** No time horizon analysis; 80/20 applied today assumes conditions are static.
- **Defer is permanent:** No mechanism to prevent "DEFER" from becoming "never."
- **Self-improvement is too heavy:** 40% of the file's content is after the core protocol, creating friction for first-time use.

### Enhancement Recommendations
1. Split into two files: a lean SKILL.md (core protocol under 40 lines) and a detailed LEARN.md (self-improvement, patterns, references).
2. Add a "Re-cut" loop trigger after completing each Top 20% item.
3. Add confidence modifiers to V and E estimates before calculating ROI.
4. Elevate the "Should we?" mindset as Step 0 — it's the most valuable part of the skill.
5. Add a saboteur/inversion check before labeling items DEFER, to prevent permanent deferral.
6. Add time horizon analysis to the DEFER/DELETE decision.
7. Add worked examples showing V and E estimation failures (not just successes).
