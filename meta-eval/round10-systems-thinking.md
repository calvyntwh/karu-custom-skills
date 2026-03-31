# Meta-Evaluation: systems-thinking

## 1. chestertons-fence

**What it reveals:** The Loop Protocol's "nodes" and "edges" are themselves fences against oversimplification. The skill explicitly guards against linear thinking (Problem -> Solution) by mandating loop tracing. However, the nodes are assumed to be obvious/given—Step 1 says "What variable are you changing?" without a protocol for *discovering* nodes. The skill doesn't explain how to identify what constitutes a node in the first place.

**Weaknesses:**
- No guidance on node granularity: How do you know if you've picked the right abstraction level for a node?
- No "fence archaeology"—if you trace the wrong edges, there's no mechanism to question whether the node itself is the problem
- The "Pre-Mortem" validation step is mentioned but underspecified

**Enhancement:** Add a node validation step: "Is this node a simplification that hides sub-nodes? Could the 'atom' you're tracing actually be a composite?" This would be Chesterton's Fence applied to the loop protocol itself.

---

## 2. decision-matrix

**What it reveals:** Decision-matrix struggles when everything affects everything. The skill has no explicit mechanism for weighting interconnected variables. If you try to apply the 4-step weighted scoring (List Options -> Define Criteria -> Assign Weights -> Score), you hit a wall: in systems thinking, changing one thing changes all the options and criteria simultaneously.

**Weaknesses:**
- The decision-matrix assumes independent variables; systems have entanglement
- No guidance on how to handle circular criteria (e.g., "Performance affects Cost, but Cost affects Performance")
- The skill doesn't teach what to do when the decision space itself is a moving target

**Enhancement:** Add a "Circular Criteria Detection" step: "Before scoring, verify that Criteria A does not influence Criteria B. If circularity exists, collapse them into a single meta-criterion or pick the most upstream."

---

## 3. first-principles-thinking

**What it reveals:** The basic truth of systems thinking—that everything is connected—collides with first-principles' need for atomic decomposition. First principles says "break it down to physics"; systems thinking says "you can't isolate physics." The tension is productive but unresolved.

**Weaknesses:**
- No guidance on where to stop decomposing—a node could decompose infinitely
- First principles asks "what are the assumptions?" but systems thinking says "the assumption is that you can identify inputs/outputs"
- The skill doesn't address emergent properties (where the whole > sum of parts)

**Enhancement:** Add an "Emergence Check": "At what level does your decomposition stop revealing causes and start hiding effects? If the nodes interact to produce behavior none of them have alone, you've hit an emergence boundary—stop decomposing, start mapping."

---

## 4. inversion-thinking

**What it reveals:** Systems thinking helps identify sabotage vulnerabilities by making loops visible—but only if you trace them. Inversion thinking (anti-goal -> pathways -> safeguards) maps well onto reinforcing loop analysis: "How do I make the retry storm explode?" is the inverse of "How do I prevent the retry storm?"

**Weaknesses:**
- The skill doesn't explicitly connect to sabotage analysis; it focuses on architectural side effects
- No guidance on what makes a loop "sabotageable" vs. naturally stable
- The "Pre-Mortem" is reactive; inversion thinking is proactive but underutilized

**Enhancement:** Add a "Saboteur Mode" to Step 3 (Find the Loops): "For each loop identified, ask: 'If I wanted this to fail catastrophically, what would I amplify?' This converts balancing loops into attack surfaces and reinforcing loops into blast radii."

---

## 5. map-vs-territory

**What it reveals:** System maps (nodes + edges) are always simplifications. The skill acknowledges this via the Pre-Mortem ("Do not guess. Look for evidence") but doesn't provide a protocol for validating the map against reality. The gap between "system map" and "actual system" is where failures hide.

**Weaknesses:**
- No mechanism to discover hidden edges (dependencies not on the map)
- The "Drift Test" ("If we do this 1000 times a second...") is mental simulation, not territory validation
- No guidance on when a map is "good enough" vs. dangerously incomplete

**Enhancement:** Add a "Hidden Edge Hunt" step: "What edges are NOT on your map? Interview the system. Check the failure logs. Ask: 'What has broken in production that nobody predicted?' Force confrontation with unmapped territory."

---

## 6. occams-razor

**What it reveals:** Systems thinking is inherently over-engineered for simple problems. The Loop Protocol (4 steps, 2 loop types, Pre-Mortem, Self-Improvement logging) is heavyweight for a single-variable change in a known system. Occam's razor would say: if the system is well-understood and the change is small, skip the full protocol.

**Weaknesses:**
- No "system complexity threshold" guide—when to apply full protocol vs. abbreviated
- The Self-Improvement Protocol adds more overhead than the core analysis
- Pattern Categories and logging feel like meta-engineering for a skill that warns about over-engineering

**Enhancement:** Add a "Protocol Triage" step: "Is this a known system with < 5 connected components? Use simplified trace. Is this a novel architecture or a post-mortem? Use full Loop Protocol." Match rigor to risk.

---

## 7. pareto-principle

**What it reveals:** In systems thinking, feedback loops ARE the 80/20. A small number of loops (often 1-3) cause the majority of system behaviors. The skill identifies loop types (Reinforcing, Balancing) but doesn't help prioritize which loops to analyze first.

**Weaknesses:**
- No guidance on which loops matter most—reinforcing and balancing loops have equal billing
- In practice, reinforcing loops (explosions) are more dangerous than balancing loops (stability)
- The Pareto question ("What feedback loops cause 80% of system behaviors?") isn't answered—it's assumed you find all loops

**Enhancement:** Add a "Loop Priority" ranking: "1. Reinforcing loops with short delays (explosion risk). 2. Balancing loops protecting critical resources (bottleneck risk). 3. Delay-heavy loops (silent accumulation risk)." Let analysts focus on the 20% of loops that cause 80% of chaos.

---

## 8. rubber-ducking

**What it reveals:** Walking through the Loop Protocol reveals confusion points:
- Step 2 (Trace the Edges): "Downstream" and "Upstream" are intuitive but inconsistently applied—is the thread pool upstream or downstream of the DB?
- Step 3 (Find the Loops): The distinction between Reinforcing (A->B->A) and Balancing (A->B->-A) is clear in abstract but ambiguous in practice. "Load High -> Add Servers -> Load per Server Low -> Remove Servers" is actually TWO loops interacting.
- The Pre-Mortem section is the vaguest: "Do not guess. Look for evidence" is good advice but not a duckable protocol.

**Weaknesses:**
- The loop definitions conflate structure (what connects) with behavior (what happens over time)
- "Does A produce B, which produces more A?" is circular language for a circular concept
- No plain-English translation step to verify understanding

**Enhancement:** Add a "Duck Translation" step: "Explain each loop in one sentence: 'The [NODE] causes [EDGE], which causes [NODE], which [INCREASES/DECREASES] the original.' If you can't say it plainly, you don't understand the loop."

---

## 9. systems-thinking (self-referential)

**What it reveals:** Systems thinking belongs to a meta-system of reasoning skills. It interacts with:
- **Chesterton's Fence**: The nodes are fences that may be load-bearing
- **Decision Matrix**: Criteria become entangled (circular dependencies)
- **First Principles**: Emergence boundaries limit decomposition
- **Inversion Thinking**: Sabotage surfaces = loop blast radii
- **Map vs Territory**: Maps are always incomplete
- **Occam's Razor**: The protocol itself can be over-engineered
- **Pareto**: Loops are the 80/20 of system behavior
- **Rubber Ducking**: Loop explanations need plain-English validation

**Weaknesses:**
- No skill explicitly references systems-thinking back—it's treated as standalone
- No guidance on skill sequencing: When do you use systems-thinking BEFORE vs AFTER another skill?
- The meta-system of skills has no "owner" to resolve conflicts (e.g., when Occam says "simplify" but systems thinking says "trace more")

**Enhancement:** Add a "Skill Integration Matrix" appendix showing when to chain skills. Example: "Before applying Occam's Razor to a system, run systems-thinking to ensure you're not removing a load-bearing loop."

---

## Summary

### Strengths
- Excellent core concept: stop thinking in lines, start thinking in loops
- Good examples (retry storms, auto-scaling) that make abstract loops concrete
- Pre-Mortem validation instinct is correct: don't guess, look for evidence
- Self-Improvement Protocol shows commitment to learning from mistakes
- Pattern categories (reinforcing loops, balancing loops, delays, trade-off errors) are useful taxonomies

### Weaknesses
- No guidance on node discovery (how to find the right nodes to trace)
- Loop definitions are mentally intuitive but operationally vague
- Pre-Mortem validation is underspecified—how exactly do you "look for evidence"?
- Heavyweight for simple problems; no complexity-based triage
- Missing integration with the other 9 reasoning skills
- Self-referential: no meta-view of where systems-thinking fits in the skill ecosystem

### Enhancement Recommendations
1. **Add Node Discovery Protocol**: How to identify nodes at the right granularity (not too fine, not too coarse)
2. **Specify Pre-Mortem Validation**: Explicit steps (log analysis, trade-off mapping, drift simulation)
3. **Add Protocol Triage**: Match Loop Protocol intensity to system complexity and change risk
4. **Add Skill Integration Matrix**: Explicit guidance on when to use systems-thinking with other skills
5. **Add Emergence Check**: At what level does decomposition stop revealing causes?
6. **Add Duck Translation Step**: Plain-English loop explanation to verify understanding
7. **Add Loop Priority Ranking**: Which loops to analyze first (reinforcing > balancing, short delay > long delay)
