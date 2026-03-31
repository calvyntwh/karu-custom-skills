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

**Pareto note:** ~80% of incidents come from Tier 1. If time-constrained, audit only Tier 1.

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

This skill learns failure patterns to anticipate sabotage more accurately.

### Logging Corrections

After applying Inversion Thinking:

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Anti-Goal:** {what was the worst case}
**Failure pathway found:** {how could it break}
**Safeguard added:** {what was implemented}
**Outcome:** {did the safeguard work?}
---
```

### Trigger Conditions

| Condition | Example | Log? |
|-----------|---------|------|
| Found a novel failure mode | "Never thought of X attack vector" | ✅ |
| Missed obvious failure | "Should have caught that earlier" | ✅ |
| Safeguard failed | "The fix didn't prevent the breach" | ✅ |
| False positive | "The 'vulnerability' was actually safe" | ✅ |
| Over-engineered protection | "The safeguard was overkill" | ✅ |
| Safeguard interaction caused failure | "Safeguard X failed, cascading to Y" | ✅ |
| Second-order backfire | "Users wrote down passwords due to MFA complexity" | ✅ |
| Unvalidated failure mode | "Theoretical vulnerability not actually exploitable" | ✅ |

### Pattern Categories for This Skill

- **Memory attacks**: Buffer overflow, injection
- **Race conditions**: TOCTOU, deadlocks
- **Authentication bypasses**: Privilege escalation, session hijacking
- **Data corruption**: Partial writes, rollback failures
- **Denial of service**: Resource exhaustion, infinite loops
- **Social engineering**: Phishing, pretexting

### Review & Promote

**Weekly:** Check for recurring failure patterns → Add to LEARNINGS.md

## Resources
*   [Failure Modes Reference](references/failure_modes.md)
