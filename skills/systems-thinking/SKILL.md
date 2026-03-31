---
name: systems-thinking
description: Architectural analysis using Feedback Loops and System Dynamics. Use when designing architectures, scaling systems, or analyzing side effects.
license: MIT
---

# Systems Thinking (The Loop Protocol)

> "You cannot just change one thing." - Garrett Hardin

## When to Use
*   **Architecture Changes:** Migrating DBs, splitting microservices, changing cache strategies.
*   **Scaling:** "We need to handle 10x traffic."
*   **Performance Tuning:** "The system is slow, let's add threads."
*   **Post-Mortems:** "Why did fixing X break Y?"

## The Protocol: The Loop Protocol
Stop thinking in Lines (Problem -> Solution).
Start thinking in Loops (Action -> Result -> Feedback -> Action).

### 1. Identify the Node
What variable are you changing?
*   *Example:* "I am increasing the Thread Pool size."

### 2. Trace the Edges
What is connected to this node?
*   *Downstream:* Threads consume -> DB Connections.
*   *Upstream:* Threads process -> Incoming Requests.

### 3. Find the Loops
*   **Reinforcing Loop (R):** Does A produce more B, which produces more A? (Explosion).
    *   *Example:* Retry Logic. Fails -> Retry -> More Load -> Fails.
*   **Balancing Loop (B):** Does A produce B, which reduces A? (Stability/Resistance).
    *   *Example:* Auto-scaling. Load High -> Add Servers -> Load per Server Low -> Remove Servers.

### 4. Validation (The Pre-Mortem)
Do not guess. Look for evidence.
*   **Log Analysis:** Look at past logs. Did similar changes cause latency spikes?
*   **Trade-off Question:** "If I maximize X, what *must* decrease?" (e.g., Speed vs Memory).
*   **Drift Test:** "If we do this 1000 times a second, what breaks?"

## Self-Improvement Protocol

This skill learns which architectural changes cause unintended consequences.

### Logging Corrections

After Systems Thinking analysis:

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Change made:** {architectural decision}
**Loop identified:** {reinforcing or balancing}
**Side effect predicted:** {what we thought would happen}
**Actual outcome:** {what actually happened}
**Loop type:** {R (explosion) | B (stabilization)}
---
```

### Trigger Conditions

| Condition | Example | Log? |
|-----------|---------|------|
| Unintended consequence | "Changing X broke Y, which we didn't trace" | ✅ |
| Loop prediction correct | "The reinforcing loop did explode as predicted" | ✅ |
| Missed downstream effect | "Should have traced further" | ✅ |
| Trade-off wrong | "Thought it was speed vs memory, was actually speed vs cost" | ✅ |
| Balancing worked | "Auto-scaling dampened the issue" | ✅ |

### Pattern Categories for This Skill

- **Reinforcing loops**: Success spirals, death spirals, retry storms
- **Balancing loops**: Homeostasis, saturation, bottlenecks
- **Delay effects**: Changes that take time to manifest
- **Trade-off errors**: Wrong optimization target chosen
- **Cascading failures**: Single points of failure
- **Hidden dependencies**: Coupling that wasn't obvious

### Review & Promote

**Monthly:** Check for recurring system patterns → Add to LEARNINGS.md
