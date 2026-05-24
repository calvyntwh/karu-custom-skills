---
name: inversion-thinking
description: Proactive failure analysis using the Saboteur Method. Use when designing critical systems, security features, or debugging root causes.
license: MIT
metadata:
  version: "1.1"
---

# Inversion Thinking (The Saboteur Method)

> "Tell me where I'm going to die so I will never go there." - Charlie Munger

## When to Use
*   **Before** writing complex code (Architecture, Security, Critical features).
*   **During** debugging (to find root causes).
*   **When** a plan seems "too simple" or "optimistic".

## When NOT to Use This Skill
*   **Non-adversarial contexts:** When the "enemy" is nature/probability, not malice—use probabilistic risk analysis instead.
*   **Low-stakes/one-off tasks:** When failure impact is acceptable and full protocol overhead isn't warranted.
*   **Well-understood domains:** When standard safeguards (frameworks, libraries) already cover known failure modes.
*   **Time-critical situations:** Use the condensed 3-step protocol or defer to rubber-ducking.

## Skill Integration Cross-References
*   **Before Inversion:** Use [first-principles-thinking](../first-principles-thinking/SKILL.md) to identify base assumptions that become failure targets
*   **Combined Protocol:** inversion-thinking → [systems-thinking](../systems-thinking/SKILL.md) to check safeguard cascades
*   **Complementary:** Use [decision-matrix](../decision-matrix/SKILL.md) when weighing multiple safeguard options against cost
*   **Validation:** Use [rubber-ducking](../rubber-ducking/SKILL.md) to verify saboteur reasoning is sound

## Severity Tiers
Prioritize failure modes by severity. Under time pressure, focus on Tier 1:

| Tier | Category | Examples | Priority |
|------|----------|----------|----------|
| **1 - Critical** | Injection, Auth bypass, Data exposure | SQL injection, session hijacking, unencrypted PII | Audit first |
| **2 - High** | Race conditions, Privilege escalation | TOCTOU, IDOR, parameter tampering | Audit second |
| **3 - Medium** | DoS, Memory corruption | Resource exhaustion, buffer overflow (managed langs: lower) | Audit third |
| **4 - Low** | Social engineering, Informational | Phishing, path traversal (read-only) | Audit last |

> [!IMPORTANT]
> **STOP condition:** All Tier 1 and Tier 2 failure modes MUST have safeguards before proceeding. If time expires, flag Tier 1 gaps explicitly.

**Pareto note:** ~80% of incidents come from Tier 1. **MUST audit Tier 1 before all else.** If time-constrained, audit only Tier 1.

## Timeboxing
*   **Full protocol:** 30 minutes maximum
*   **Condensed protocol:** 10 minutes maximum
*   **Per failure mode:** 5 minutes investigation max—if unresolved, log as "unvalidated" and escalate
*   **Stop condition:** All Tier 1 and Tier 2 failure modes have safeguards OR time expires

## The Protocol: Become the Saboteur
Do not ask "Does this work?". Ask "How do I break this?".
Follow these 4 steps explicitly.

### 1. Define the Anti-Goal
Explicitly write down the worst-case outcome.
*   *Goal:* "Keep user data safe."
*   *Anti-Goal:* "Leak all user data to the public internet."

#### Identify Assumptions
Before simulating sabotage, list the implicit assumptions the system makes:
*   About trust boundaries (what inputs are trusted?)
*   About input validity (what format is expected?)
*   About timing (what sequencing is assumed?)
*   About environment (what infrastructure is relied upon?)

The Anti-Goal should directly violate at least one of these assumptions.

### 2. The Saboteur Simulation
Adopt the persona of a malicious actor or the embodiment of Entropy (Murphy's Law).

#### Structured Attacker Framework
Use MITRE ATT&CK or STRIDE as mental scaffolding:
*   **STRIDE categories:** Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
*   **ATT&CK tactics:** Initial Access → Execution → Persistence → Privilege Escalation → Defense Evasion → Credential Access → Discovery → Lateral Movement → Collection → Exfiltration → Impact

Ask: **"I want to achieve the Anti-Goal. What is the easiest way to do it?"**

> [!IMPORTANT]
> **CRITICAL:** If Tier 1 (Critical) failure modes are found, they MUST have safeguards before proceeding.

### 3. Proof of Fragility
List concrete, specific pathways to failure. Use `references/failure_modes.md` for inspiration.
*   "I will send a 10GB file to crash the memory."
*   "I will send a request with `admin=true`."
*   "I will unplug the database cable mid-transaction."

#### Validation Step
For each failure pathway, verify it is actually exploitable in your architecture:
*   Is the attack surface exposed? (network, API, UI?)
*   Does the vulnerability actually exist in your implementation?
*   Can you demonstrate exploitability (even theoretically)?

Log unvalidated failures separately. If you cannot verify exploitability, treat as lower confidence.

### 4. Inversion (The Fix)
Design specific safeguards to block those pathways.
*   "Enforce 10MB limit (HTTP 413)."
*   "Validate permissions on server side."
*   "Use atomic transactions with rollback."

#### Safeguard Interaction Analysis
Map safeguards as a system—not independent fixes:
| Safeguard | Protected Attack Vector | Dependencies | May Create |
|-----------|------------------------|--------------|------------|
| Rate limiting | DoS | Redis, clock sync | Legitimate users blocked |
| Input validation | Injection | Parsing library | False positives |

Ask:
1. Where do safeguards overlap? (redundancy is good)
2. Where are there gaps? (single point of failure)
3. Does Safeguard X create dependency on Safeguard Y?
4. Does a failed Safeguard Y cause cascading failure?

#### Second-Order Check
For each safeguard, ask:
1. How will users work around this? (security friction creates new vulnerabilities)
2. What new attack surface does this create?
3. What is the maintenance cost over 3 years?

If safeguard backfires, reconsider the design.

## Condensed Protocol (Time-Pressured)
When under 10 minutes:
1. **Define Anti-Goal** (1 min): State the worst case in one sentence.
2. **Saboteur + Fix pairs** (7 min): For each failure mode, immediately state the counter-safeguard. Skip catalog lookup.
3. **Verify safeguards** (2 min): Spot-check one safeguard for interaction effects.

## Meta-Inversion: When Inversion Fails
Apply inversion to the skill itself:

*   **Anti-Goal of inversion-thinking:** "Never anticipate failure; assume everything works on first try."
*   **Saboteur Simulation:** "How do I ensure this skill gets skipped?" → Make it too complex, too vague, or too time-consuming.
*   **Proof of Fragility:** The skill fails when:
    *   Practitioners are under time pressure (shortcut the protocol)
    *   The skill produces false confidence (checked obvious cases, missed creative ones)
    *   Safeguards become the attack surface (over-engineered → new vulnerabilities)
    *   Checklist mentality replaces genuine attacker thinking

**When NOT to trust inversion-thinking output:**
- Catalog-driven reasoning (relying on failure_modes.md without genuine attack trees)
- No Tier 1 findings after 30 minutes (either system is secure or analysis was superficial)
- Safeguards require >20% of implementation effort (may indicate over-engineering)

## Self-Improvement Protocol

**Log only novel failure modes or safeguard failures.**

```markdown
## [YYYY-MM-DD] {Brief Description}
**Failure mode**: {what was discovered}
**Safeguard**: {what was added}
**Outcome**: {did it work?}
---
```

**Promote after 3+ similar discoveries.**

## Resources
*   [Failure Modes Reference](references/failure_modes.md)

---

## Evaluations

### Eval 1: Tier 1 Injection Prevention
**Scenario:** User wants to add file upload feature. Code has `system("cat " + filename)`.
**Expected:** Identifies as Critical Tier, finds injection vulnerability, proposes input validation + sanitization.
**Pass criteria:** MUST identify shell injection as Tier 1, produces specific safeguard (not just "be careful").

### Eval 2: Safeguard Interaction Cascade
**Scenario:** Adding rate limiting + IP blocklist. Both involve Redis.
**Expected:** Identifies safeguard dependencies, asks about Redis failure modes, checks for cascading failure.
**Pass criteria:** Maps safeguard dependencies, identifies single point of failure in Redis.

### Eval 3: Meta-Inversion (Skill Self-Check)
**Scenario:** Skill produces 0 Tier 1 findings after 30 minutes.
**Expected:** Triggers meta-inversion warning — either system is unusually secure OR analysis was superficial.
**Pass criteria:** Correctly identifies false confidence risk, suggests deeper investigation.
