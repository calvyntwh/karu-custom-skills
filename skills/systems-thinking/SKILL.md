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
