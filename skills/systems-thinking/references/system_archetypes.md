# system_archetypes.md - The Architect's Traps

Common patterns where linear solutions cause systemic failure.

## 1. Fixes that Fail
*   **Pattern:** A quick fix reduces the symptom but reinforces the root cause.
*   **Example:** "The DB is slow (Symptom) -> Rewrite query to be unverified/unsafe (Fix) -> Data corruption occurs later (Unintended Consequence)."
*   **Solution:** Focus on the long-term structural fix.

## 2. Shifting the Burden
*   **Pattern:** Solving a problem with a helper/patch, making the system dependent on the patch.
*   **Example:** "Query is slow -> Add Cache." Now you have two problems: The slow query (ignored) and Cache Invalidation.
*   **Solution:** Optimize the query first. Use Cache only for scaling, not fixing bugs.

## 3. Tragedy of the Commons
*   **Pattern:** Optimizing for one individual hurts the whole.
*   **Example:** "Each Microservice retries infinitely." The shared Database dies.
*   **Solution:** Global regulation (e.g., Global Rate Limiting / Circuit Breakers).

## 4. Drifting Goals
*   **Pattern:** Accepting a lower standard becomes the new standard.
*   **Example:** "It's okay if pages load in 2s." -> "2.5s is close enough." -> "3s is fine."
*   **Solution:** Anchor goals to external absolutes (e.g., "Must be under 1s").
