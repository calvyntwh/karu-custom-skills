# Meta-Evaluation: occams-razor

## 1. chestertons-fence

**What it reveals:** The skill explicitly invokes `chestertons-fence` as a safety check ("Chesterton Check") in Step 2. This is a deliberate integration point—the "Why" Test includes: "If uncertain about purpose, invoke chestertons-fence protocol first." This acknowledges that not all complexity is unnecessary.

**Weaknesses:**
- The integration is **advisory** ("If uncertain"), not mandatory. An agent eager to simplify may skip the Chesterton check.
- The Decision Matrix in Step 2 conflates "Keep" criteria: "Referenced or Tests Fail → KEEP" ignores *why* something is referenced or whether tests are testing the right thing.
- The "Prune" step (Step 3) includes examples like collapsing "Passthrough" classes, but chestertons-fence would require proving those passthrough classes are actually load-bearing before removal.

**Enhancement:** Make the Chesterton check **mandatory** for any component that isn't trivially dead code. Add: "If grep finds references but you don't understand *why*, invoke chestertons-fence before pruning."

---

## 2. decision-matrix

**What it reveals:** The skill implicitly assumes simplicity is always the correct answer. The decision-matrix would challenge this—there are cases where complexity is warranted.

**Weaknesses:**
- No guidance on *when* complexity is justified. The "When to Use" section lists triggers (boilerplate-y, heavy) but these are subjective.
- No weighted criteria for deciding "too complex vs appropriately complex."
- The Decision Matrix skill has a Pre-Check that says "2 Options Only? Skip the matrix." Occam's razor could be seen as skipping the matrix entirely—jumping to "delete" without evaluation.

**Enhancement:** Add a brief "When NOT to use Occam's Razor" section: performance-critical paths, security boundaries, multi-team APIs where simplicity of one side causes complexity on another.

---

## 3. first-principles-thinking

**What it reveals:** The skill's "Subtraction Method" is the inverse of first-principles-thinking. First-princicies asks "What is this built from?" Occam asks "What can be removed?" Both are valid but opposite directions.

**Weaknesses:**
- The "bare metal" test (Step 4: "Does the bare metal system still solve the user's Core Problem?") assumes the Core Problem is well-defined. If the user's stated problem is wrong, simplifying to it may be wrong.
- No mechanism to challenge the *problem definition* itself. First-principles would ask "Is this even the right problem?"
- The Hypothesis ("This solution is too complex") is assumed true before investigation—this is reasoning backwards from a conclusion.

**Enhancement:** Add a Step 0: "Verify the problem statement" — ask "What problem does this solve for the user?" before assuming complexity is the problem.

---

## 4. inversion-thinking

**What it reveals:** Inversion-thinking asks "How do I break this?" The Prune step could remove safeguards that prevent failures.

**Weaknesses:**
- The skill doesn't address what happens when over-simplification removes a safeguard. Example: collapsing validation layers might remove the "security fence" that stops malformed input.
- The "Chesterton Check" partially addresses this, but there's no explicit "Saboteur Simulation" asking "If I remove this, how does the system fail?"
- No mention of security, race conditions, or edge-case guards in the pruning examples.

**Enhancement:** Add to the "Why" Test: "Does this component prevent a specific failure mode? Could removing it enable a Saboteur pathway?"

---

## 5. map-vs-territory

**What it reveals:** The skill assumes the **code** is the territory. But "simple" code may not match what developers consider simple. A one-liner that uses obscure language features may be "simple" syntactically but cognitively complex.

**Weaknesses:**
- The skill measures simplicity by what can be removed, not by comprehension. A 50-line obvious function may be "simpler" than a 5-line clever one.
- No mention of readability, cognitive load, or bus factor.
- The "bare metal" test checks if the core problem is solved, not if humans can maintain the solution.

**Enhancement:** Add a "Developer Cognitive Load" check: "Can a new developer understand this in 5 minutes?" Simplification that creates clever-but-opaque code should be flagged as a potential mistake.

---

## 6. occams-razor

**What it reveals:** Self-referentially, the skill could simplify itself. At 85 lines with detailed logging protocols, it may itself be over-engineered.

**Weaknesses:**
- The Self-Improvement Protocol adds complexity (CORRECTIONS.md, LEARNINGS.md, REVIEW.md, PATTERNS.md) that may exceed the complexity it removes.
- The logging template has 4 fields + date + markdown formatting. For small simplifications, this overhead may exceed the value.
- "Weekly Review" suggests ongoing maintenance of the skill itself.

**Enhancement:** Consider a leaner self-improvement approach: a single `.learnings/simplifications.md` with one-line entries. The current overhead may discourage use.

---

## 7. pareto-principle

**What it reveals:** If 80% of maintenance burden comes from 20% of complexity, the skill should target that 20%. But the skill doesn't help identify which complexity is the 20%.

**Weaknesses:**
- No guidance on where to prune first. "Iterate through every component" (Step 2) treats all complexity as equal.
- The Pattern Categories (abstraction layers, passthrough classes, boilerplate indicators) are broad. Which causes 80% of the pain?
- No ROI calculation: pruning a rarely-used abstraction vs pruning a widely-used one have different payoffs.

**Enhancement:** Add prioritization: "Start with the complexity that touches the most critical paths or causes the most frequent bugs." Reference Pareto's 80/20—prune high-traffic, high-bug areas first.

---

## 8. rubber-ducking

**What it reveals:** The "Why" Test mentions explaining to verify safety, but not in the rubber-ducking sense. The rubber-ducking protocol would ask: "Can I explain *why this component exists* in plain English?"

**Weaknesses:**
- The "Why" Test is about safety (grep, tests), not about understanding. If you can't explain why something exists, you shouldn't prune it—but the skill doesn't say this explicitly.
- The Decision Matrix criteria ("Referenced or Tests Fail → KEEP") might miss the case where code is referenced but nobody knows *why*.
- Ambiguity: "Nice to have" is deleted, but who decides what's "nice to have"? A feature flag that one team calls "nice to have" might be a contract with another team.

**Enhancement:** Add a "Rubber Duck Explanation" requirement: "Before pruning, you must be able to explain in one sentence why this component exists. If you cannot, invoke chestertons-fence."

---

## 9. systems-thinking

**What it reveals:** Removing complexity from one part of a system can cause complexity in another. The skill doesn't address interconnectedness.

**Weaknesses:**
- Collapsing "Passthrough" classes may break abstractions that other parts of the system depend on, even if the passthrough itself adds no logic.
- No mention of downstream effects. Example: removing a validation layer might work for direct callers but break middleware, proxies, or testing harnesses that depend on that layer.
- The "bare metal" test only checks the Core Problem, not the connected systems.

**Enhancement:** Add a "System Map" check before pruning: "What is connected to this component? Will removing it break any downstream system or contract?" Use the system's thinking "trace the edges" approach.

---

## 10. second-order-thinking

**What it reveals:** First-order: "Remove this abstraction layer." Second-order: "Then developers add similar logic inline in each caller, multiplying duplication."

**Weaknesses:**
- The skill's Verification step (Step 4) only checks immediate results ("still solves the core problem"). It doesn't check what happens in the next sprint.
- Over-pruning creates second-order complexity: developers work around the missing abstraction, often in worse ways.
- The "Self-Improvement Protocol" logs corrections but doesn't anticipate them. "Over-pruning → had to add back" is documented but not prevented.

**Enhancement:** Add a "Second-Order Check": "If we prune this, what will developers likely do instead? Will that create more complexity than we removed?" This anticipates the common pattern where removed abstractions resurface as inline code scattered across the codebase.

---

## Summary

### Strengths
- Well-integrated with chestertons-fence for safety checks
- Clear 4-step protocol that is easy to follow
- Self-improvement protocol with pattern tracking
- Good examples of what to prune (lodash → native, passthrough classes)
- Addresses over-engineering with explicit hypothesis framing

### Weaknesses
- Makes simplification a default assumption rather than one option in a decision framework
- No guidance on when complexity is warranted
- Missing second-order and systems-level impact analysis
- Cognitive complexity not addressed—only code complexity
- Self-referential overhead may exceed value for small projects

### Enhancement Recommendations
1. **Add mandatory Chesterton check** for non-trivial components before pruning
2. **Add "When NOT to use"** section addressing performance-critical, security-sensitive, and multi-team contexts
3. **Add Step 0: Problem Verification** to challenge the stated problem before assuming over-engineering
4. **Add Second-Order Check** to anticipate workarounds that may spawn worse complexity
5. **Add System Map check** to trace downstream effects before removal
6. **Add Developer Cognitive Load** metric—simplicity should be measured by human comprehension, not just removal count
7. **Simplify the self-improvement protocol** to reduce logging overhead
8. **Add prioritization** using Pareto's 80/20 to focus pruning effort on high-impact areas
