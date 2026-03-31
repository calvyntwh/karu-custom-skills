---
name: inversion-thinking
description: Proactive failure analysis using the Saboteur Method. Use when designing critical systems, security features, or debugging root causes.
license: MIT
---

# Inversion Thinking (The Saboteur Method)

> "Tell me where I'm going to die so I will never go there." - Charlie Munger

## When to Use
*   **Before** writing complex code (Architecture, Security, Critical features).
*   **During** debugging (to find root causes).
*   **When** a plan seems "too simple" or "optimistic".

## The Protocol: Become the Saboteur
Do not ask "Does this work?". Ask "How do I break this?".
Follow these 4 steps explicitly.

### 1. Define the Anti-Goal
Explicitly write down the worst-case outcome.
*   *Goal:* "Keep user data safe."
*   *Anti-Goal:* "Leak all user data to the public internet."

### 2. The Saboteur Simulation
Adopt the persona of a malicious actor or the embodiment of Entropy (Murphy's Law).
Ask: **"I want to achieve the Anti-Goal. What is the easiest way to do it?"**

### 3. Proof of Fragility
List concrete, specific pathways to failure. Use `references/failure_modes.md` for inspiration.
*   "I will send a 10GB file to crash the memory."
*   "I will send a request with `admin=true`."
*   "I will unplug the database cable mid-transaction."

### 4. Inversion (The Fix)
Design specific safeguards to block those pathways.
*   "Enforce 10MB limit (HTTP 413)."
*   "Validate permissions on server side."
*   "Use atomic transactions with rollback."

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
