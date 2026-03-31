# Meta-Evaluation: first-principles-thinking

## 1. chestertons-fence

**What it reveals:** The skill's instruction to "stop when you hit a physical law, a mathematical truth, or a verified hard constraint" functions as a fence—but the skill never asks *why* that fence exists. The stopping criterion is presented as self-evident rather than interrogated.

**Weaknesses:**
- No guidance on what makes a constraint "verified" vs. assumed
- The "stop rule" itself could be wrong (e.g., what if the "physical law" is based on incomplete understanding?)
- Missing protocol for when to challenge the fence itself vs. accept it

**Enhancement:** Add a "fence about fences" step: "Before accepting a constraint as terminal, ask: Why is this constraint considered inviolable? Who verified it? Under what conditions does it hold?"

---

## 2. decision-matrix

**What it reveals:** First-principles thinking and decision-matrix address fundamentally different problem types. The skill correctly identifies when to use FPT (innovation, novel problems), but doesn't explicitly address when NOT to use it.

**Weaknesses:**
- FPT is computationally expensive but the skill doesn't provide heuristics for when the ROI isn't worth it
- No guidance on when analogical reasoning is actually sufficient (low-stakes, well-trodden problems)
- The 10x improvement threshold is arbitrary

**Enhancement:** Add a decision criterion: "Before engaging FPT, ask: What is the cost of being wrong? If low, analogical reasoning is probably sufficient. If high (safety-critical, highly innovative), FPT is warranted."

---

## 3. first-principles-thinking (Self-Referential)

**What it reveals:** The skill is vulnerable to its own methodology. "Question all assumptions" is itself an assumption. If applied recursively, this leads to infinite regress.

**Weaknesses:**
- No explicit stop condition that isn't self-referential
- The Socratic questioning itself isn't questioned
- The "Search/Read to verify" instruction is good but doesn't address what to do when sources conflict

**Enhancement:** Add meta-level guidance: "Acknowledge that the framework itself rests on unquestioned assumptions (e.g., that breaking problems down is useful, that atomic units exist). Document these as explicit boundary conditions."

---

## 4. inversion-thinking

**What it reveals:** FPT can lead to unconventional answers that are factually wrong. "Deconstruct to physics/logic/economics" assumes these domains fully capture reality.

**Weaknesses:**
- Physics, logic, and economics are themselves models with known limitations
- Quantum effects, emergent behavior, and human irrationality violate naive physical/economic assumptions
- Example (SpaceX) works because rockets are (mostly) classical systems—FPT fails for quantum, biological, or social systems

**Enhancement:** Add domain boundaries: "FPT works best for mechanical, supply-chain, and computational problems. For quantum, biological, or social systems, consult domain experts before assuming 'physics' provides the atomic units."

---

## 5. map-vs-territory

**What it reveals:** The "atomic units" (mass, energy, axioms, raw material costs) are presented as territory, but they are actually maps—models that have been validated but not verified for every case.

**Weaknesses:**
- The skill doesn't distinguish between verified atomic units and assumed ones
- "Material properties" depend on conditions (temperature, pressure, purity)—not truly atomic
- Economic "truths" like spot prices are volatile and context-dependent

**Enhancement:** Add reality-check protocol: "After identifying atomic units, verify at least one empirically. If your 'atomic truth' is actually a model, label it as such and note its confidence interval."

---

## 6. occams-razor

**What it reveals:** The 5-whys approach is potentially over-engineered. The skill instructs to ask "Why?" 5 times without guidance on whether fewer questions would suffice.

**Weaknesses:**
- No threshold for when questioning can stop before 5 whys
- Some assumptions are trivially falsifiable (1-2 whys), others require deeper probing
- No guidance on efficiency—time-boxing, or when rapid falsification is possible

**Enhancement:** Replace fixed 5-whys with: "Ask 'Why?' until you encounter either (a) a verified physical law, or (b) a statement you cannot verify with Search/Read. Stop at whichever comes first. Cap at 5 to prevent infinite regress."

---

## 7. pareto-principle

**What it reveals:** The skill identifies "atomic truths" as stop conditions but doesn't distinguish which assumptions are high-value vs. low-value to challenge.

**Weaknesses:**
- Challenging the wrong assumption wastes effort; the skill provides no prioritization
- "Physical laws" (mentioned as stop conditions) are rarely the bottleneck—assumptions about human behavior, market dynamics, or implementation are usually more fruitful
- No guidance on which assumptions are likely to be wrong vs. likely to be correct

**Enhancement:** Add Pareto filter: "Before questioning an assumption, estimate: (a) how central is this to the problem? (b) how likely is it to be wrong? Focus on assumptions that are both central AND likely wrong. Low-likelihood assumptions are often correct—skip them."

---

## 8. rubber-ducking

**What it reveals:** The Socratic questioning sequence is underspecified. "Ask 'Why?' 5 times" lacks clarity on what constitutes a valid answer vs. a deflection.

**Weaknesses:**
- No guidance on recognizing bad answers: "Because that's how it's always done" is presented as an assumption to challenge, but the skill doesn't teach how to detect it in answers
- The questioning can become circular—answering one "Why?" with another assumption that itself needs questioning
- No distinction between empirical claims (verifiable) and value judgments (not falsifiable)

**Enhancement:** Add answer-type classification: "When you ask 'Why?' and get an answer, classify it as: (1) Empirical—Search/Read to verify. (2) Social norm—note as context-dependent. (3) Value judgment—acknowledge and move on. (4) Circular—re-ask with different framing."

---

## 9. systems-thinking

**What it reveals:** FPT isolates problems to find atomic truths, but this deconstruction ignores how the parts interact. The "reconstruct from scratch" step assumes no emergent properties arise from combination.

**Weaknesses:**
- The skill treats atomic units as independent, but systems have emergent behavior
- "Build a 10x better solution" ignores second-order effects of the new solution
- No feedback loop analysis—what if the "better" solution creates new problems?

**Enhancement:** Add a systems-thinking checkpoint after reconstruction: "Before implementing, ask: (1) What new interactions does this solution create? (2) What feedback loops might emerge? (3) What breaks if this scales 10x?"

---

## 10. second-order-thinking

**What it reveals:** The skill focuses on questioning current assumptions but ignores the second-order effect of always questioning: analysis paralysis and missed opportunities.

**Weaknesses:**
- No timeboxing or decision deadline
- FPT without a time constraint can infinite-loop on questioning
- The self-improvement protocol logs corrections but doesn't measure opportunity cost

**Enhancement:** Add time-horizon guidance: "Set a maximum questioning duration before reconstruction. If you hit the deadline, either (a) accept current best atomic units and proceed, or (b) escalate to human review. Log how often you hit the deadline—frequent hits suggest the problem is too ill-defined for FPT alone."

---

## Summary

### Strengths
- Clear 3-step methodology (Identify → Deconstruct → Reconstruct)
- Strong examples (SpaceX, Chef vs Cook) that make abstract concrete
- Self-improvement protocol with logging and pattern recognition
- Good stopping criteria (physical laws, mathematical truths)
- Emphasizes verification over memory ("Search/Read to verify")

### Weaknesses
- No explicit boundary conditions (which domains/market segments?)
- Over-reliance on physics/economics as "atomic" when they're actually models
- No prioritization of which assumptions to question (Pareto gap)
- Socratic questioning underspecified—no answer classification
- Missing timeboxing—risk of infinite analysis
- No integration with other reasoning skills (e.g., doesn't reference inversion, second-order)
- No guidance on when FPT fails (quantum, biological, social systems)

### Enhancement Recommendations
1. Add domain boundary checklist: "FPT works best for mechanical/supply-chain problems; use with caution for quantum/biological/social systems"
2. Add answer-type classification to Socratic questioning
3. Add Pareto filter for assumption prioritization
4. Add timeboxing: "Maximum N whys or hours before proceeding"
5. Add second-order checkpoint: "What feedback loops does the new solution create?"
6. Add map-vs-territory verification step for atomic units
7. Add explicit cross-references to complementary skills (inversion-thinking, decision-matrix, systems-thinking)
