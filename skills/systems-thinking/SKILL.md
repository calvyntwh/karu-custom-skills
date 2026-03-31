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
*   **Adding new services** that touch shared resources.

## When NOT to Use
*   **Simple, isolated changes** — single function, known system, no shared state.
*   **Well-understood systems with < 5 connected components** — use simplified trace only.
*   **Time-critical decisions** — loop analysis takes longer than linear analysis.
*   **Experimental/prototype code** — where failure is expected and recovery is cheap.
*   **Greenfield projects** — no loops exist yet to analyze.

## The Protocol: The Loop Protocol

Stop thinking in Lines (Problem -> Solution).
Start thinking in Loops (Action -> Result -> Feedback -> Action).

### Protocol Triage

Match rigor to risk:
*   **Simplified (fast):** Known system, < 5 components, reversible change → Steps 1-2 only.
*   **Full (thorough):** Novel architecture, post-mortem, irreversible change → All steps.

### 1. Identify the Node
What variable are you changing?
*   *Example:* "I am increasing the Thread Pool size."

**Node Discovery:** Ask "What does this component talk to?" — trace data flow, not code structure.

### 2. Trace the Edges
What is connected to this node?
*   *Downstream:* Threads consume -> DB Connections.
*   *Upstream:* Threads process -> Incoming Requests.

**Hidden Edge Hunt:** Ask "What has broken in production that nobody predicted?" — force confrontation with unmapped dependencies.

### 3. Find the Loops

**Loop Priority (Analyze in Order):**
1. **Reinforcing loops (R)** — Explosion risk. Short delay makes these dangerous.
2. **Balancing loops (B)** — Bottleneck risk. Protect critical resource limits.
3. **Delay-heavy loops** — Silent accumulation risk. Problems manifest long after cause.

**Reinforcing Loop (R):** Does A produce more B, which produces more A?
*   *Example:* Retry Logic. Fails -> Retry -> More Load -> Fails.
*   *Saboteur Mode:* "If I wanted this to fail catastrophically, what would I amplify?"

**Balancing Loop (B):** Does A produce B, which reduces A?
*   *Example:* Auto-scaling. Load High -> Add Servers -> Load per Server Low -> Remove Servers.

**Delay Effect:** Does change take time to manifest?
*   *Example:* Cache warming, connection pool exhaustion, resource leaks.

### 4. Validation (The Pre-Mortem)
Do not guess. Look for evidence.
*   **Log Analysis:** Look at past logs. Did similar changes cause latency spikes?
*   **Trade-off Question:** "If I maximize X, what *must* decrease?" (e.g., Speed vs Memory).
*   **Drift Test:** "If we do this 1000 times a second, what breaks?"

### 5. Duck Translation
Explain each loop in one sentence:
> "The [NODE] causes [EDGE], which causes [NODE], which [INCREASES/DECREASES] the original."

If you can't say it plainly, you don't understand the loop.

### 6. Second-Order Effects Check
Ask for each loop identified:
*   Does this loop affect other loops?
*   Does success here create conditions for failure elsewhere?
*   Does removing this loop create a new reinforcing loop?

### Stop Conditions
Stop analysis when:
*   You've identified all loops connecting to the change
*   Additional nodes reveal no new edges
*   You've hit an **emergence boundary** — nodes interact to produce behavior none have alone
*   Time spent exceeds value of further analysis (Pareto: 80% of insights from 20% of loops)

## Skill Integration Matrix

| Skill | When to Chain |
|-------|---------------|
| [`chestertons-fence`](../chestertons-fence/SKILL.md) | Before removing any node — verify it's not load-bearing |
| [`occams-razor`](../occams-razor/SKILL.md) | After systems-thinking: if no loops involve this component, simplification is safer |
| [`inversion-thinking`](../inversion-thinking/SKILL.md) | For each R-loop, ask "How do I amplify this failure?" |
| [`second-order-thinking`](../second-order-thinking/SKILL.md) | Trace cascades beyond immediate loop effects |
| [`decision-matrix`](../decision-matrix/SKILL.md) | When criteria become circular — collapse into meta-criteria |
| [`rubber-ducking`](../rubber-ducking/SKILL.md) | When loop explanation doesn't sound right in plain English |

**Common Chain:** `systems-thinking` → `occams-razor` (simplify what isn't load-bearing) → `chestertons-fence` (verify before removing)

## Self-Improvement Protocol (Simplified)

After architecture analysis, log **only surprises**:

**Log to `.learnings/system-loops.md`:**
```markdown
- [YYYY-MM-DD] {system} → {loop type} → {predicted} vs {actual}
```

**Log if:**
*   Unintended consequence occurred
*   Loop behaved differently than predicted
*   Missed a hidden dependency

**Do NOT log** routine confirmations — loop analysis is documentation enough.

## Pattern Categories (Prioritized)

**High-Risk (Analyze First):**
- Reinforcing loops with short delays (explosion risk)
- Balancing loops protecting critical resources (bottleneck risk)
- Shared state mutations

**Medium-Risk (Verify):**
- Delay-heavy loops (silent accumulation)
- External service dependencies
- Caching layers

**Low-Risk (Acknowledge):**
- Well-isolated components
- Read-only operations
- Replicated services
