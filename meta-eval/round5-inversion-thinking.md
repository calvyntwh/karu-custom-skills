# Meta-Evaluation: inversion-thinking

## 1. chestertons-fence

**What it reveals:** The Anti-Goal functions as a conceptual fence against naive optimism. It forces the practitioner to pause and articulate what *shouldn't* happen before designing safeguards. The fence exists because without it, humans default to confirmation bias—asking "will this work?" rather than "how will this fail?"

**Weaknesses:**
- The skill doesn't explicitly advise *against* removing or simplifying the Anti-Goal step. A Chesterton's Fence check should be added: "Before skipping the Anti-Goal, prove the worst case is impossible."
- No guidance on when the fence is "over-engineered" (i.e., the Anti-Goal is too catastrophically unlikely to warrant protection).

**Enhancement:** Add a "Fence Verification" step: "Is this Anti-Goal actually plausible, or are we protecting against cosmic rays? If the Anti-Goal requires simultaneity of 47 impossible events, simplify."

---

## 2. decision-matrix

**What it reveals:** Inversion-thinking is superior to decision-matrix when the problem domain is adversarial. Decision-matrix works for technology/vendor choices where success is objective and static. Inversion-thinking wins when the "opponent" is intelligent and adapting (attackers, Murphy's Law, entropy).

**Weaknesses:**
- The skill never acknowledges its complementary relationship with decision-matrix.
- No guidance on *when not to use* inversion-thinking (e.g., when the "enemy" is nature, not malice—then probabilistic risk analysis may be better).

**Enhancement:** Add a "When NOT to use" section contrasting with decision-matrix. Inversion-thinking is for adversarial or entropy-dominated domains; decision-matrix is for static multi-criteria optimization.

---

## 3. first-principles-thinking

**What it reveals:** Sabotage reasoning rests on a basic truth: **every system has exploitable assumptions**. The skill assumes that code written to achieve Goal X makes implicit assumptions about inputs, environment, and user behavior—and these assumptions can be violated. First-principles decomposition of a system reveals its "atomic vulnerabilities."

**Weaknesses:**
- The skill doesn't explicitly teach *how to find* those base assumptions. It says "become the saboteur" but doesn't provide a systematic way to enumerate assumptions.
- The failure_modes.md catalog is a crutch that may prevent genuine first-principles reasoning (catalog-driven vs. system-derived failure modes).

**Enhancement:** Add Step 1.5: "Identify Assumptions" before Define Anti-Goal. List the implicit assumptions the system makes (about trust boundaries, input validity, timing, etc.). The Anti-Goal should directly violate these assumptions.

---

## 4. inversion-thinking (Self-Referential)

**What it reveals:** Yes, you can invert the inversion skill itself. Applied rigorously:

- **Anti-Goal of inversion-thinking:** "Never anticipate failure; assume everything works on first try."
- **Saboteur Simulation:** "How do I ensure this skill gets skipped?" → Make it too complex to follow, too vague to apply, too time-consuming to use.
- **Proof of Fragility:** The skill fails when: (1) practitioners are under time pressure, (2) the skill is too long to read, (3) it produces false confidence, (4) safeguards become the attack surface.

**Weaknesses:**
- The skill doesn't address its own failure modes (meta-inversion).
- If inversion-thinking becomes security theater, practitioners may believe they've anticipated failures when they've only checked obvious cases.

**Enhancement:** Add a self-referential "Anti-Use Case" section: "When does inversion-thinking create false security?" List its failure modes (checklist mentality, inventor blind spots, over-engineered safeguards).

---

## 5. map-vs-territory

**What it reveals:** The failure_modes.md catalog is a "map" that may diverge from actual attacker behavior in the wild. Real attackers use: zero-days (not in catalog), chained exploits (interactions between low-severity issues), economic analysis (why bother attacking X when Y is easier), and novel attack classes that emerge from system interactions.

**Weaknesses:**
- The catalog could create a false sense of completeness. Practitioners may think "I checked failure_modes.md, I'm covered."
- The catalog is static; attacker techniques evolve. No mechanism to update the map against live threat intelligence.

**Enhancement:** Add a "Map Verification" step: "Compare your failure modes against recent CVEs in your dependency stack or industry incident reports. Does your map match the territory?" Suggest subscribing to CISA advisories, GitHub Security Advisories, or industry-specific threat feeds.

---

## 6. occams-razor

**What it reveals:** The 4-step protocol (Anti-Goal → Saboteur Simulation → Proof of Fragility → Inversion) is likely necessary but could be condensed. Steps 3 and 4 are mirror images (list failures, then block them) and could be combined into a single "Identify & Mitigate" step.

**Weaknesses:**
- The skill is verbose for what is essentially: "Ask 'how can this fail?' then fix it." The protocol overhead may discourage use in quick coding tasks.
- Step 3 (Proof of Fragility) and Step 4 (The Fix) are sequential but could be iterative—"for each failure, design safeguard, then check if safeguard introduces new failures."

**Enhancement:** Condense to a 3-step protocol: (1) Define Anti-Goal, (2) Saboteur Simulation with immediate counter-design (Failure→Fix pairs), (3) Verify safeguards don't introduce new Anti-Goals. This is functionally equivalent but lower ceremony.

---

## 7. pareto-principle

**What it reveals:** Approximately 20% of failure modes cause 80% of security incidents. Based on industry data, the critical 20% are:
- **Injection attacks** (SQL, XSS, command—unchecked input validation)
- **Broken authentication** (session hijacking, credential stuffing, privilege escalation)
- **Sensitive data exposure** (unencrypted data at rest/transit, improper key management)

The skill's pattern categories correctly weight toward these, but don't prioritize them.

**Weaknesses:**
- The skill treats all failure categories equally (Memory attacks, Race conditions, Auth bypasses, Data corruption, DoS, Social engineering). This gives equal mental bandwidth to buffer overflow (rare in managed languages) and injection (ubiquitous and severe).

**Enhancement:** Add a severity/likelihood weighting to the Pattern Categories. Suggest prioritizing: Injection > Broken Auth > Data Exposure > the rest. Provide guidance like: "If you only have 10 minutes, audit for injection first."

---

## 8. rubber-ducking

**What it reveals:** The Saboteur Simulation breaks down in several ways:

1. **The "persona" is hollow.** Telling someone to "adopt the persona of a malicious actor" doesn't actually give them the mental toolkit of an attacker. Most developers think like developers.

2. **Step 2 asks the wrong question.** "What is the *easiest* way to achieve the Anti-Goal?" biases toward obvious failures, not creative ones. Real attackers think in attack trees, not "easiest path."

3. **The skill doesn't validate the saboteur's reasoning.** Rubber-ducking would catch this: "Did you actually identify a real vulnerability, or did you list a theoretical one?"

**Weaknesses:**
- No validation step to check if the failure modes found are real vs. imagined.
- The persona adoption is hand-wavy without MITRE ATT&CK framework or similar structured attacker thinking.

**Enhancement:** Add a "Saboteur Validation" sub-step: "Verify each failure pathway is actually exploitable in your system architecture. If you're unsure, consult the failure_modes.md reference or run a penetration test."

---

## 9. systems-thinking

**What it reveals:** Safeguards interact in complex ways. Adding safeguards can create:
- **Reinforcing loops:** Over-engineered safeguards create complexity → complexity creates new failure modes → new failure modes require more safeguards (security sprawl).
- **Balancing loops:** A safeguard in one layer (e.g., rate limiting) is compensated by weakness in another (e.g., no per-IP blocking, so bypass via distributed IPs).
- **Cascading failures:** A failed safeguard (e.g., expired certificate) blocks legitimate access, creating DoS.

The skill never addresses safeguard interaction or cascade.

**Weaknesses:**
- Treats each safeguard as independent. In reality, safeguards form a system with emergent behaviors.
- No guidance on "safeguard overlap" (two safeguards protecting the same path, leaving gaps elsewhere).

**Enhancement:** Add a "Safeguard Interaction Check" step: "Map your safeguards as a system. Where do they overlap? Where are there gaps? Does adding Safeguard X create a dependency on Safeguard Y?" Recommend a simple table: Safeguard → Protected Attack Vector → Dependencies.

---

## 10. second-order-thinking

**What it reveals:** Security safeguards have significant second/third-order effects:

- **Second-order:** Adding MFA (security safeguard) → users resent friction → users write down passwords on sticky notes (new vulnerability).
- **Third-order:** Requiring 12-character passwords with special chars → users use Password123! → password cracking rules adapt → users still vulnerable.

The skill designs safeguards but never evaluates their downstream behavioral consequences.

**Weaknesses:**
- No guidance on "safeguard backfire"—when security measures push risk elsewhere rather than eliminate it.
- No cost-benefit analysis within the skill (safeguard effort vs. actual risk reduction).

**Enhancement:** Add a "Second-Order Check" step: "For each safeguard, ask: (1) How will users work around this? (2) What new attack surface does this create? (3) What is the cost to maintain this safeguard over 3 years?" This prevents security theater that merely shifts risk.

---

## Summary

### Strengths
1. **Structured 4-step protocol** forces systematic failure thinking rather than ad-hoc review
2. **Self-improvement loop** with CORRECTIONS.md and pattern promotion is excellent meta-cognition
3. **Failure Modes Reference** provides concrete starting points for practitioners who lack attacker mindset
4. **Strong name/mnemonic** (Saboteur Method, Charlie Munger quote) aids recall
5. **Applicable pre/post-development** (before writing code, during debugging, after incidents)
6. **Cross-references to other skills** (Chesterton's Fence mentioned implicitly via the "fence" metaphor)

### Weaknesses
1. **Catalog dependency risk** — failure_modes.md may replace genuine attacker thinking
2. **No safeguard interaction analysis** — safeguards treated as independent, not systemic
3. **No prioritization** — equal weight to all failure categories despite Pareto distribution of real risk
4. **Lacks "when not to use"** guidance — applied blindly to non-adversarial domains
5. **No validation step** — no check that identified failures are real exploitables
6. **Saboteur persona is hand-wavy** — no structured attacker framework (ATT&CK, STRIDE, etc.)
7. **No second-order effects analysis** — safeguards may backfire or shift risk

### Enhancement Recommendations
1. Add a **Threat Actor framework reference** (MITRE ATT&CK, STRIDE, or similar) to ground the Saboteur Simulation in structured attacker methodology
2. Add a **Safeguard Interaction Matrix** to prevent cascading failures and identify gaps
3. Add **severity-weighted pattern categories** prioritizing injection, broken auth, and data exposure
4. Add a **"Map vs Territory" verification step** comparing failure modes against live threat intelligence
5. Add a **Second-Order Effects Checklist** to prevent safeguard backfire
6. Add a **condensed 3-step version** for rapid use under time pressure
7. Add **"When NOT to use"** guidance distinguishing adversarial (use inversion) from non-adversarial (use risk analysis/Pareto) contexts
8. Add a **"Meta-Inversion" section** addressing the skill's own failure modes to prevent false confidence
