---
name: first-principles-thinking
description: A mental model for breaking down basic truths to generate original solutions. Use for innovation, novel problems, or when stuck in conventional thinking.
license: MIT
metadata:
  type: mental-model
  version: "1.1"
---

# First Principles Thinking

## Overview
First Principles Thinking is a mode of inquiry that relentlessly questions assumptions to get to the fundamental truth of a problem, then builds a solution from scratch. It is the tool of the innovator, used to bypass "reasoning by analogy" (copying what others do).

## When to Use This Skill
*   **Innovation:** When the user wants to invent a new way of doing things.
*   **Stuck Points:** When standard solutions are too expensive, too slow, or impossible.
*   **Debugging:** When "it should work" but doesn't—strip away assumptions about why it *should* work.
*   **Cost Analysis:** When you need to understand the absolute floor of a cost structure.

## When NOT to Use This Skill
*   **Well-trodden problems:** When analogical reasoning is sufficient and the cost of being wrong is low.
*   **Quantum/Biological systems:** FPT assumes independence of atomic units; quantum entanglement and biological emergence violate this.
*   **Social/Human systems:** Human behavior is not decomposable into physics axioms—consult domain experts instead.
*   **Time-critical decisions:** FPT is computationally expensive; under deadline pressure, use decision-matrix or analogical reasoning.
*   **When expertise is available:** If a domain expert can be consulted and the problem is within their validated expertise, rely on their map.

## Domain Boundary Checklist
Before applying FPT, confirm:
- [ ] Problem is mechanical, supply-chain, or computational (not quantum/biological/social)
- [ ] Atomic units are empirically verifiable (not model-dependent)
- [ ] Cost of being wrong is high enough to warrant full deconstruction
- [ ] Time available exceeds 2x estimated analysis duration

## Skill Integration Cross-References
*   **Before FPT:** Use [decision-matrix](../decision-matrix/SKILL.md) to confirm FPT is warranted (high-stakes, innovative)
*   **After FPT:** Use [systems-thinking](../systems-thinking/SKILL.md) to check feedback loops and emergent behavior
*   **Combined Protocol:** When facing adversarial contexts, chain inversion-thinking → FPT
*   **Complementary:** Use [rubber-ducking](../rubber-ducking/SKILL.md) to verify plain-English explanation of atomic units
*   **Avoid over-use:** If FPT hits deadline frequently, the problem may be too ill-defined—consider escalating

## Methodology

### 1. Identify & Question Assumptions (Socratic Method)
**Goal:** Expose the hidden beliefs limiting the current view.

#### Answer Classification
When "Why?" yields an answer, classify it before proceeding:
| Type | Action |
|------|--------|
| **Empirical** | Search/Read to verify—do not accept on memory |
| **Social norm** | Note as context-dependent; may shift |
| **Value judgment** | Acknowledge; not falsifiable—move on |
| **Circular** | Re-ask with different framing |

#### Timeboxing
*   **Maximum:** 5 "Why?" iterations OR 30 minutes, whichever comes first.
*   **Stop at:** (a) verified physical law, (b) unverified claim you cannot verify with Search/Read.
*   **Deadline fallback:** Accept current best assumption with confidence label (verified/assumed/unknown) and proceed. Log deadline hits.

#### Pareto Prioritization
Before questioning an assumption, estimate:
*   **Centrality:** How core is this to the problem? (1-5)
*   **Likelihood of being wrong:** (1-5)
*   **Priority Score:** Centrality × (5 - Likelihood)

Question assumptions with Priority Score ≥ 15 first. Low-likelihood assumptions are often correct—skip them.

*   **Prompt:** "What are we assuming to be true here? Why do we think that?"
*   **Technique:** Ask "Why?" up to 5 times.
    *   **CRITICAL:** Do not answer from memory. **Search/Read** to verify the answer to each "Why?".
    *   *Stop:* When you hit a physical law, a mathematical truth, or a verified hard constraint.

### 2. Deconstruct to Constituent Parts
**Goal:** Find the atomic units that cannot be reduced further.
*   **Action:** Break the system down into:
    *   **Physics:** Mass, energy, material properties.
    *   **Logic:** Axioms and necessary truths.
    *   **Economics:** Raw material costs, time units.

#### Validation Step
Label each atomic unit as:
*   **Verified** — empirically confirmed under relevant conditions
*   **Model** — theoretical construct (e.g., economic "spot price") with known limitations
*   **Assumed** — no verification attempted

For Model/Assumed units, note confidence interval and conditions where they may not hold.

### 3. Reconstruct from Scratch
**Goal:** Build a 10x better solution using only the essential parts.
*   **Action:** Ignore "how it's usually done." Combine the atomic units in the most efficient way possible to achieve the goal.

#### Second-Order Checkpoint
Before implementing, ask:
1. What new interactions does this solution create?
2. What feedback loops might emerge when it scales 10x?
3. What breaks if this solution becomes widely adopted?

Use [systems-thinking](../systems-thinking/SKILL.md) if feedback loop analysis is complex.

## Boundary Conditions
This framework rests on unquestioned assumptions:
*   Breaking problems down is useful (may fail for emergent systems)
*   Atomic units exist (may fail for quantum entanglement)
*   Deconstruction reveals truth (may fail for social/human systems)

Document these as explicit limits. Re-evaluate if problem domain shifts.

## Examples

### The SpaceX Example (Cost Reduction)
> **User:** "Rockets are too expensive."
> **Analogy Reasoning:** "Rockets define the market price. We can maybe save 10% by negotiating."
> **First Principles Reasoning:** "A rocket is just aluminum, titanium, and fuel. The spot price of these materials is 2% of a rocket's cost. The cost is inefficient manufacturing. We will buy raw metal and build it ourselves."

### The "Chef vs. Cook"
> **Analogy (Cook):** Follows a recipe. If an ingredient is missing, they stop.
> **First Principles (Chef):** Understands *why* the acid balances the fat. If a lemon is missing, they use vinegar, because the *principle* is acidity.

## Self-Improvement Protocol

This skill learns to identify assumptions more accurately and find better atomic truths.

### Logging Corrections

After applying First Principles Thinking:

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Problem:** {the original problem}
**Assumption challenged:** {what was assumed}
**Breakthrough:** {the actual truth found}
**Outcome:** {did it work?}
---
```

### Trigger Conditions

| Condition | Example | Log? |
|-----------|---------|------|
| Found a false assumption | "Turns out X was actually Y" | ✅ |
| Missed obvious assumption | "Should have questioned Z earlier" | ✅ |
| Wrong atomic unit | "The 'atomic' unit had substructure" | ✅ |
| Analogical reasoning was right | "Standard approach actually worked" | ✅ |
| Novel solution found | "Never seen this approach before" | ✅ |

### Pattern Categories for This Skill

- **Assumption patterns**: Common beliefs that are usually wrong
- **Atomic unit types**: Physics, Logic, Economics breakdowns
- **Questioning depth**: How many "whys" needed
- **Analogy failures**: When analogies mislead vs help
- **Constraint types**: Physical vs logical vs economic

### Review & Promote

**Weekly:** Check for recurring assumption patterns → Add to LEARNINGS.md

## Resources
*   [Detailed Research Notes](references/research.md)
