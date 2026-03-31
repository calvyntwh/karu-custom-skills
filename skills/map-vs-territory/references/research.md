# Research: Map vs. Territory

## 1. Core Concept
The abstraction (Map) is not the reality (Territory). Confusing the two leads to cognitive errors where we act on the model rather than the real world.

> "The map is not the territory." - Alfred Korzybski

## 2. Origins & Key Figures
*   **Alfred Korzybski (1931):** Polish-American scholar who introduced General Semantics. He presented the paper "A Non-Aristotelian System and its Necessity for Rigour in Mathematics and Physics", famously stating "the map is not the territory".
*   **René Magritte:** Surrealist artist whose painting *The Treachery of Images* (citation: "Ceci n'est pas une pipe") visually illustrates this concept.
*   **Baudrillard (Simulacra):** Argued that in the postmodern world, the map has *preceded* the territory (Hyperreality).

## 3. Related Concepts
### Model Drift
The Territory changes (code is updated, environment changes), but the Map (docs, mental model) stays static. Over time, the Map becomes a lie.

### Leaky Abstractions (Joel Spolsky)
"All non-trivial abstractions, to some degree, are leaky."
*   *Example:* TCP is a "reliable" map over IP (unreliable territory). Sometimes the territory leaks through (packet loss, latency), and the map breaks.

## 4. Application to Engineering
*   **Debugging:** Code comments ("This variable is never null") are Maps. The runtime memory is the Territory.
*   **Incidents:** Dashboards (Map) might say "System Green" while users are screaming (Territory).
*   **Testing:** Mocks are Maps. Integration tests check the Territory.

## 5. Sources
*   *Science and Sanity* by Alfred Korzybski
*   *The Law of Leaky Abstractions* by Joel Spolsky
