# Meta-Evaluation Summary

## Per-Skill Results

### humanizer-karu-custom
**Strengths:**
- Comprehensive 24-pattern taxonomy with concrete Before/After examples
- Self-improvement protocol demonstrates thoughtful long-term maintenance
- "Add soul" section addresses the limitation that pattern removal alone doesn't equal naturalness
- Evidence-based foundation (Wikipedia's AI writing research)
- Clear process steps that are actionable

**Weaknesses:**
- No severity tiers - all patterns treated equally
- Self-improvement may drift - LLM assessing own performance is circular
- "Human voice" is stereotyped - assumes Western casual opinionated prose
- Pattern overlap - unclear handling when one phrase triggers multiple patterns
- Context blindness - same rules applied to academic, marketing, technical writing
- Some patterns obsolete - curly quotes, cutoff disclaimers, emojis are either trivial or dated
- Complexity overhead - self-improvement protocol adds significant maintenance

**Recommendations:**
1. Reorganize by severity: High-impact patterns first (AI vocabulary, em dashes, filler phrases, inflated significance), low-yield patterns moved to appendix
2. Add context modes: Academic, casual, technical, marketing - each with different pattern weights
3. Simplify self-improvement: Either make it optional or shift logging to explicit user feedback
4. Clarify "Add soul": Provide procedural steps, not just philosophical guidance
5. Distinguish pattern types: AI-exclusive vs. AI-overused vs. AI-similar
6. Add uncertainty preservation: For formal writing, some hedging is correct
7. Add conflict detection: With grammar/tone skills that might contradict
8. Deprecate obsolete patterns: Curly quotes, knowledge-cutoff disclaimers

---

### chestertons-fence
**Strengths:**
- Clear, actionable protocol with 4 distinct steps
- Excellent integration with git tools (practical for developers)
- Good decision table with clear outcomes
- Self-improvement mechanism with pattern categories
- Strong literary foundation (Chesterton quote)

**Weaknesses:**
- Unclear when to use this skill vs. alternatives (rubber-ducking, occams-razor)
- Self-improvement protocol requires manual effort that may not happen
- No fallback when git archaeology fails
- Over-conservative "DO NOT DELETE" when reason not found (could use feature flags)
- No guidance on when code is legitimately obsolete AND can be safely deleted
- Missing second-order consequences (fence accumulation as technical debt)

**Recommendations:**
1. Add "When NOT to use" section - greenfield code, personal recent code, well-tested code
2. Add risk prioritization matrix - not all fences are equal priority
3. Add fence retirement protocol - periodically re-evaluate kept code
4. Add 4th decision outcome - REFACTOR for legitimate-but-complex cases
5. Add fallback when git unavailable - human review, code context analysis
6. Integrate rubber-ducking step - require plain-English explanation before decision
7. Acknowledge second-order risk - that "never delete" culture can cause technical debt accumulation

---

### decision-matrix
**Strengths:**
- Clear protocol: Step-by-step structure is implementable and trainable
- User-weighted criteria: Correctly delegates values to the user, not the agent
- Pre-check gate: The 2-option skip prevents over-engineering simple decisions
- Self-improvement mechanism: Logging framework exists for corrections and learnings
- Honest about limitations: "Eliminate popularity bias" is a realistic goal, not overselling

**Weaknesses:**
- False precision: 1-5 scale with 1-4 weights implies accuracy that doesn't exist
- No evidence requirement: Scoring without citations divorces the map from territory
- Incomplete edge case handling: No guidance for incommensurable options, non-compensatory criteria, or non-transitive preferences
- Static weights: No mechanism for weight evolution as context changes
- Inactive feedback loop: CORRECTIONS.md has zero entries—either unused or unmaintained
- No conflict detection: Doesn't surface when criteria conflict or when options are incomparable
- Binary outcome: Produces a "winner" when honest answer is often "insufficient data to distinguish"

**Recommendations:**
1. Evidence anchoring: Require citation for scores of 1 or 5; default uncertain scores to 3 with uncertainty notation
2. Non-compensatory filter: Before matrix, filter out options that violate non-negotiable constraints
3. Conflict detection: Add step to identify negatively correlated criteria and warn about interaction effects
4. Uncertainty output: Instead of single-point recommendation, output confidence ranges
5. Temporal review trigger: Set 6-month review checkpoint in the output, not just the self-improvement log
6. Activation metric: Track decision-matrix usage; if unused for 60+ days, prompt user to review LEARNINGS.md
7. Simplification path: Explicitly branch to Pros/Cons or binary filter when matrix complexity isn't warranted

---

### first-principles-thinking
**Strengths:**
- Clear 3-step methodology (Identify → Deconstruct → Reconstruct)
- Strong examples (SpaceX, Chef vs Cook) that make abstract concrete
- Self-improvement protocol with logging and pattern recognition
- Good stopping criteria (physical laws, mathematical truths)
- Emphasizes verification over memory ("Search/Read to verify")

**Weaknesses:**
- No explicit boundary conditions (which domains/market segments?)
- Over-reliance on physics/economics as "atomic" when they're actually models
- No prioritization of which assumptions to question (Pareto gap)
- Socratic questioning underspecified—no answer classification
- Missing timeboxing—risk of infinite analysis
- No integration with other reasoning skills (doesn't reference inversion, second-order)
- No guidance on when FPT fails (quantum, biological, social systems)

**Recommendations:**
1. Add domain boundary checklist: "FPT works best for mechanical/supply-chain problems; use with caution for quantum/biological/social systems"
2. Add answer-type classification to Socratic questioning
3. Add Pareto filter for assumption prioritization
4. Add timeboxing: "Maximum N whys or hours before proceeding"
5. Add second-order checkpoint: "What feedback loops does the new solution create?"
6. Add map-vs-territory verification step for atomic units
7. Add explicit cross-references to complementary skills (inversion-thinking, decision-matrix, systems-thinking)

---

### inversion-thinking
**Strengths:**
- Structured 4-step protocol forces systematic failure thinking rather than ad-hoc review
- Self-improvement loop with CORRECTIONS.md and pattern promotion is excellent meta-cognition
- Failure Modes Reference provides concrete starting points for practitioners who lack attacker mindset
- Strong name/mnemonic (Saboteur Method, Charlie Munger quote) aids recall
- Applicable pre/post-development (before writing code, during debugging, after incidents)

**Weaknesses:**
1. Catalog dependency risk - failure_modes.md may replace genuine attacker thinking
2. No safeguard interaction analysis - safeguards treated as independent, not systemic
3. No prioritization - equal weight to all failure categories despite Pareto distribution of real risk
4. Lacks "when not to use" guidance - applied blindly to non-adversarial domains
5. No validation step - no check that identified failures are real exploitables
6. Saboteur persona is hand-wavy - no structured attacker framework (ATT&CK, STRIDE, etc.)
7. No second-order effects analysis - safeguards may backfire or shift risk

**Recommendations:**
1. Add a Threat Actor framework reference (MITRE ATT&CK, STRIDE, or similar) to ground the Saboteur Simulation
2. Add a Safeguard Interaction Matrix to prevent cascading failures and identify gaps
3. Add severity-weighted pattern categories prioritizing injection, broken auth, and data exposure
4. Add a "Map vs Territory" verification step comparing failure modes against live threat intelligence
5. Add a Second-Order Effects Checklist to prevent safeguard backfire
6. Add a condensed 3-step version for rapid use under time pressure
7. Add "When NOT to use" guidance distinguishing adversarial from non-adversarial contexts
8. Add a "Meta-Inversion" section addressing the skill's own failure modes

---

### map-vs-territory
**Strengths:**
- Clarity: The 3-step protocol (Doubt → Probe → Update) is memorable and actionable
- Strong framing: "DO NOT READ CODE. RUN CODE." is a powerful anti-dogma
- Practical examples: Concrete actions guide implementation
- Self-improvement loop: The logging protocol enables pattern learning
- Addresses real problem: Documentation-code drift is a universal pain point

**Weaknesses:**
- No safety guards: Running code without context can cause production issues
- No prioritization: All discrepancy types treated equally despite vastly different severities
- Ambiguous terminology: "Map" and "Territory" are overloaded and context-dependent
- Self-referential gap: No mechanism to verify the skill itself is applied correctly
- No "when NOT to use" guidance: Over-application wastes time on correct Maps
- Feedback loop blindness: No acknowledgment that Map ≠ Territory is often systemic

**Recommendations:**
1. Add pre-flight checks: "Is running code safe in this context?" "Is this a one-off or recurring issue?" "Rate Map credibility (1-5) before probing"
2. Prioritize by impact: Type annotation errors → Critical; API drift → High; Naming lies → Medium; Comment/doc drift → Low
3. Disambiguate "Territory": Local runtime state, logs, network responses - each requires different verification tactics
4. Add skill self-verification: Include a smoke test case with known outcome
5. Address systemic issues: If Map ≠ Territory is frequent, recommend documentation process fixes
6. Add warning: Map can be correct - sometimes Territory was wrong due to code bug, not Map error

---

### occams-razor
**Strengths:**
- Well-integrated with chestertons-fence for safety checks
- Clear 4-step protocol that is easy to follow
- Self-improvement protocol with pattern tracking
- Good examples of what to prune (lodash → native, passthrough classes)
- Addresses over-engineering with explicit hypothesis framing

**Weaknesses:**
- Makes simplification a default assumption rather than one option in a decision framework
- No guidance on when complexity is warranted
- Missing second-order and systems-level impact analysis
- Cognitive complexity not addressed—only code complexity
- Self-referential overhead may exceed value for small projects

**Recommendations:**
1. Add mandatory Chesterton check for non-trivial components before pruning
2. Add "When NOT to use" section addressing performance-critical, security-sensitive, and multi-team contexts
3. Add Step 0: Problem Verification to challenge the stated problem before assuming over-engineering
4. Add Second-Order Check to anticipate workarounds that may spawn worse complexity
5. Add System Map check to trace downstream effects before removal
6. Add Developer Cognitive Load metric—simplicity should be measured by human comprehension
7. Simplify the self-improvement protocol to reduce logging overhead
8. Add prioritization using Pareto's 80/20 to focus pruning effort on high-impact areas

---

### pareto-principle
**Strengths:**
- Concrete and actionable: The 3-step protocol is immediately usable without training
- Correct core insight: The mindset shift from "can we?" to "should we?" is the most valuable part
- Self-improvement infrastructure: Corrections logging and pattern categories are well-designed
- Applies universally: The 80/20 framing is domain-agnostic and memorable

**Weaknesses:**
- Over-reliance on V/E formula: Treated as precise when it's a rough heuristic with known failure modes
- No loop structure: Designed as a one-time cut, not an iterative re-evaluation
- Temporal blindness: No time horizon analysis; 80/20 applied today assumes conditions are static
- Defer is permanent: No mechanism to prevent "DEFER" from becoming "never"
- Self-improvement is too heavy: 40% of the file's content is after the core protocol

**Recommendations:**
1. Split into two files: a lean SKILL.md (core protocol under 40 lines) and a detailed LEARN.md
2. Add a "Re-cut" loop trigger after completing each Top 20% item
3. Add confidence modifiers to V and E estimates before calculating ROI
4. Elevate the "Should we?" mindset as Step 0
5. Add saboteur/inversion check before labeling items DEFER, to prevent permanent deferral
6. Add time horizon analysis to the DEFER/DELETE decision
7. Add worked examples showing V and E estimation failures (not just successes)

---

### rubber-ducking
**Strengths:**
1. Well-grounded mechanism: Code→English translation leverages LLM strengths to validate logic weaknesses
2. Minimal, actionable protocol: 4 steps that fit in working memory
3. Goal Alignment Check: Table format is clear and prevents "close enough" reasoning
4. Self-improvement loop: Logging with pattern categories creates a learning system
5. Good examples: The off-by-one example is concrete and demonstrates real value
6. Clear trigger conditions: When to use is explicitly stated

**Weaknesses:**
1. No guidance on what to skip: No "obviousness heuristic" — everything looks like it needs ducking
2. Bugs that escape verbalization unaddressed: Concurrency, memory, Heisenbugs, library mismatches
3. User goal assumed correct: No goal-refinement step
4. Local-only validation: No systems-thinking about side effects or downstream impacts
5. Self-improvement adds friction: The logging breaks the 4-step flow
6. Second/third-order benefits unstated: The skill undersells its compounding value

**Recommendations:**
1. Add "when to skip" criteria: Trivial code, already-tested utilities, one-liners
2. Add "bugs that escape" section: Explicitly warn about concurrency, memory, and Heisenbugs
3. Add goal-refinement step: "Verify the goal is complete before checking alignment"
4. Add systems-thinking check: "What does this return? What does the caller expect?"
5. Separate core protocol from learning protocol: Core: 2 questions. Learning: optional logging
6. Add "Benefits Cascade": Explain second and third-order effects to justify adoption
7. Add decision-matrix cross-reference: When to use ducking vs. other skills
8. Add "why it works" section: Self-referential explanation of the mechanism

---

### systems-thinking
**Strengths:**
- Excellent core concept: stop thinking in lines, start thinking in loops
- Good examples (retry storms, auto-scaling) that make abstract loops concrete
- Pre-Mortem validation instinct is correct: don't guess, look for evidence
- Self-Improvement Protocol shows commitment to learning from mistakes
- Pattern categories (reinforcing loops, balancing loops, delays, trade-off errors) are useful taxonomies

**Weaknesses:**
- No guidance on node discovery (how to find the right nodes to trace)
- Loop definitions are mentally intuitive but operationally vague
- Pre-Mortem validation is underspecified—how exactly do you "look for evidence"?
- Heavyweight for simple problems; no complexity-based triage
- Missing integration with the other 9 reasoning skills
- Self-referential: no meta-view of where systems-thinking fits in the skill ecosystem

**Recommendations:**
1. Add Node Discovery Protocol: How to identify nodes at the right granularity
2. Specify Pre-Mortem Validation: Explicit steps (log analysis, trade-off mapping, drift simulation)
3. Add Protocol Triage: Match Loop Protocol intensity to system complexity and change risk
4. Add Skill Integration Matrix: Explicit guidance on when to use systems-thinking with other skills
5. Add Emergence Check: At what level does decomposition stop revealing causes?
6. Add Duck Translation Step: Plain-English loop explanation to verify understanding
7. Add Loop Priority Ranking: Which loops to analyze first (reinforcing > balancing, short delay > long delay)

---

### second-order-thinking
**Strengths:**
- Clean distinction from inversion-thinking with a comparison table
- Concrete examples (Cobra Effect, Tolerance Paradox, Knowledge Curse) that are memorable
- Self-improvement protocol with logging and pattern recognition
- Core question ("And then what?") is simple and repeatable
- Time horizon framing adds temporal rigor

**Weaknesses:**
- No guidance on *when to stop* tracing chains
- Feedback loop detection underdeveloped (systems-thinking gap)
- Time horizon predictions not calibrated or validated
- No Pareto heuristic for which chains matter most
- Self-referential costs of second-order thinking absent
- No integration points with other reasoning skills (decision-matrix, inversion)
- Example chains contain logic gaps (correlation ≠ causation assumptions)

**Recommendations:**
1. Add "When to Stop" heuristics — not every chain needs tracing to infinity
2. Expand feedback loop detection — connect explicitly to systems-thinking skill
3. Add calibration guidance for time horizons — warn against optimistic forecasting
4. Include Pareto heuristic — teach which second-order effects dominate
5. Add self-referential warning — acknowledge cost of over-analysis; when to use first-order thinking
6. Integrate with decision-matrix and inversion — provide combined protocols
7. Fix logic gaps in examples — trace mechanisms, not just directions

---

## Cross-Skill Weakness Analysis

| Weakness | Skills Identifying |
|----------|-------------------|
| Self-improvement protocol requires manual effort that may not happen / is inactive / overhead | chestertons-fence, decision-matrix, humanizer-karu-custom, inversion-thinking, occams-razor, pareto-principle, rubber-ducking, systems-thinking, second-order-thinking |
| No "when NOT to use" guidance / lacks guidance on appropriate contexts | chestertons-fence, decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, map-vs-territory, occams-razor, rubber-ducking |
| No integration with other skills / missing cross-references | chestertons-fence, decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, map-vs-territory, occams-razor, pareto-principle, systems-thinking, second-order-thinking |
| No second-order / long-term consequences analysis | chestertons-fence, decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, map-vs-territory, occams-razor, pareto-principle, systems-thinking |
| No timeboxing / deadline guidance / risk of infinite analysis | decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, map-vs-territory, pareto-principle, second-order-thinking |
| Self-improvement may drift / circular self-assessment | chestertons-fence, decision-matrix, humanizer-karu-custom, inversion-thinking, map-vs-territory, systems-thinking |
| Over-complexity / self-improvement overhead exceeds value | chestertons-fence, humanizer-karu-custom, inversion-thinking, map-vs-territory, occams-razor, pareto-principle, rubber-ducking, systems-thinking |
| No prioritization / equal weight to all factors despite varying importance | chestertons-fence, decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, map-vs-territory, occams-razor, pareto-principle, systems-thinking |
| No feedback loop analysis / systemic effects ignored | chestertons-fence, first-principles-thinking, inversion-thinking, map-vs-territory, occams-razor, pareto-principle, rubber-ducking, second-order-thinking |
| Terminology / definitions vague or overloaded | chestertons-fence, first-principles-thinking, humanizer-karu-custom, map-vs-territory, systems-thinking |
| No explicit stop condition / when to conclude analysis | first-principles-thinking, inversion-thinking, pareto-principle, rubber-ducking, second-order-thinking |
| False precision / implied accuracy doesn't match reality | decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, pareto-principle |
| Missing fallback when primary method fails | chestertons-fence, decision-matrix, humanizer-karu-custom, map-vs-territory, rubber-ducking |
| No validation step / no check that conclusions are correct | chestertons-fence, decision-matrix, first-principles-thinking, humanizer-karu-custom, inversion-thinking, map-vs-territory, second-order-thinking |
| Over-reliance on catalog / reference docs instead of genuine reasoning | humanizer-karu-custom, inversion-thinking, map-vs-territory |
| No worked examples / examples don't show failure modes | decision-matrix, pareto-principle, second-order-thinking |
| Cognitive complexity not addressed / assumes expert level | chestertons-fence, first-principles-thinking, inversion-thinking, occams-razor, rubber-ducking |
| No safety guards against misapplication | inversion-thinking, map-vs-territory, second-order-thinking |
| Self-referential blind spots / can't evaluate itself | chestertons-fence, decision-matrix, first-principles-thinking, inversion-thinking, map-vs-territory, systems-thinking |
| Missing "when to stop" heuristics | first-principles-thinking, inversion-thinking, pareto-principle, second-order-thinking |

---

## Top Recommendations (by frequency)

1. **Add "When NOT to Use" guidance** (8 skills) — Explicitly defining scope boundaries and contraindications was the most commonly identified gap. Skills acknowledge being applied inappropriately to contexts where they don't fit.

2. **Add skill integration matrix / cross-references** (10 skills) — Nearly all skills recognize they don't reference or combine well with other skills. Users don't know when to chain skills or resolve conflicts between them.

3. **Simplify or optionalize self-improvement protocol** (8 skills) — The self-improvement/logging overhead was frequently cited as exceeding value, especially for one-off uses. Most recommend splitting into core (minimal) and advanced (optional) modules.

4. **Add prioritization / severity tiers** (9 skills) — All patterns, criteria, failure modes, and assumptions are treated equally despite vastly different importance. Skills need Pareto-style filtering to focus effort.

5. **Add timeboxing / deadline guidance** (7 skills) — Several skills risk infinite loops (analysis paralysis) or permanent deferral without temporal constraints.

6. **Add second-order / cascading effects analysis** (9 skills) — Skills focus on immediate effects and miss downstream consequences that create new problems.

7. **Add validation / verification step** (7 skills) — No check that the skill's output is actually correct; assumptions go unverified.

8. **Add explicit stop conditions** (5 skills) — When to conclude analysis, pruning, or questioning is underspecified.

9. **Add fallback protocol for when primary method fails** (5 skills) — Git unavailable, code can't be run, catalog doesn't apply—skills lack contingency plans.

10. **Reduce false precision** (5 skills) — 1-5 scales, V/E formulas, and specific percentages imply accuracy that doesn't exist in subjective assessments.