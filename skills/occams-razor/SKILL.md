---
name: occams-razor
description: Complexity Pruning and Simplification using the Subtraction Method. Use when refactoring, reducing boilerplate, or challenging over-engineered solutions.
license: MIT
---

# Occam's Razor (The Subtraction Method)

> "Entities should not be multiplied without necessity." - William of Ockham

## When to Use
*   **Before** adding a new library or dependency.
*   **When** refactoring legacy code.
*   **When** a solution feels "heavy", "boilerplate-y", or hard to explain.
*   **During** Code Review to challenge over-engineering.

## The Protocol: The Subtraction Method
Do not ask "What can I add?". Ask "What can I remove?".
Follow these 4 steps explicitly.

### 1. The Hypothesis
Assume the current solution is over-engineered.
State: **"This solution is too complex. It can be simpler."**

### 2. The "Why" Test (Safety Check)
Iterate through every component. Prune ruthlessly, but verify safety.
*   **Grep Test:** Search for the string/symbol in the entire codebase. Is it referenced dynamically?
*   **Test Suite:** Run the project's tests. Do they pass?
*   **Chesterton Check:** If uncertain about purpose, invoke [`chestertons-fence`](../chestertons-fence/SKILL.md) protocol first.
*   **Decision Matrix:**
    *   *Unused & No Deps:* **DELETE**.
    *   *Unused but "Nice to have":* **DELETE**.
    *   *Referenced or Tests Fail:* **KEEP**.

### 3. The Prune
Actively remove the unnecessary components.
*   Replace heavy libraries with native language features (e.g., `lodash` -> `Array.map`).
*   Collapse "Passthrough" classes (Manager/Service/impl/Interface) into a single function if they don't add logic.
*   Delete unused config/boilerplate.

### 4. Verification
Does the *bare metal* system still solve the user's Core Problem?
*   If YES: You are done.
*   If NO: Restore only the *minimum* necessary piece.
