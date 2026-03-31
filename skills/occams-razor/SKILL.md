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

## When NOT to Use
*   **Performance-critical paths** where the "simpler" solution has worse algorithmic complexity.
*   **Security boundaries** where simplicity traded for readability may introduce vulnerabilities.
*   **Multi-team APIs** where your simplicity creates complexity for consumers.
*   **Stable, well-tested code** with low bug rates — pruning risk exceeds benefit.
*   **During active incidents** — focus on recovery, not refactoring.
*   **Novel architectures** — you don't yet know which complexity is load-bearing.

## The Protocol: The Subtraction Method
Do not ask "What can I add?". Ask "What can I remove?".
Follow these 4 steps explicitly.

### 0. Problem Verification
Before pruning, verify the problem statement is correct.
Ask: "What problem does this solve for the user?" If you can't answer, **do not prune**.

### 1. The Hypothesis
Assume the current solution is over-engineered.
State: **"This solution is too complex. It can be simpler."**

### 2. The "Why" Test (Safety Check)
Iterate through every component. Prune ruthlessly, but verify safety.
*   **Grep Test:** Search for the string/symbol in the entire codebase. Is it referenced dynamically?
*   **Test Suite:** Run the project's tests. Do they pass?
*   **Chesterton Check:** If uncertain about purpose, invoke [`chestertons-fence`](../chestertons-fence/SKILL.md) protocol first. **Mandatory** for non-trivial components.
*   **Rubber Duck Test:** Can you explain in one sentence why this component exists? If not, invoke chestertons-fence.

### 3. The Prune
Actively remove the unnecessary components.
*   Replace heavy libraries with native language features (e.g., `lodash` -> `Array.map`).
*   Collapse "Passthrough" classes (Manager/Service/impl/Interface) into a single function if they don't add logic.
*   Delete unused config/boilerplate.

### 4. Verification
Does the *bare metal* system still solve the user's Core Problem?
*   If YES: You are done.
*   If NO: Restore only the *minimum* necessary piece.

### Stop Conditions
Stop pruning when:
*   Tests fail and you don't understand why
*   You cannot explain the component's purpose in plain English
*   The component is referenced by code you don't own
*   You've reached the "Core Problem" boundary — removing further breaks user value

## Second-Order Check
Before pruning, anticipate workarounds:

**Ask:** "If I remove this, what will developers likely do instead?"

*   **Over-pruning pattern:** Removed abstraction → developers add inline duplication across 10 callers → **more complexity than removed**
*   **Contract breach:** Removing validation layer → callers must add checks → **distributed complexity**
*   **Knowledge loss:** Removing documentation → tribal knowledge only → **fragility**

If workaround complexity > removed complexity, **do not prune**.

## Skill Integration Matrix

| Skill | When to Chain |
|-------|---------------|
| [`chestertons-fence`](../chestertons-fence/SKILL.md) | **Always** before pruning non-trivial components |
| [`systems-thinking`](../systems-thinking/SKILL.md) | Before pruning components with downstream dependencies |
| [`second-order-thinking`](../second-order-thinking/SKILL.md) | Before pruning widely-used abstractions |
| [`rubber-ducking`](../rubber-ducking/SKILL.md) | When you can't explain why something exists |
| [`decision-matrix`](../decision-matrix/SKILL.md) | When simplicity vs. robustness trade-off is unclear |

**Rule:** If systems-thinking identifies a reinforcing loop involving this component, **do not prune** without tracing the full loop.

## Self-Improvement Protocol (Simplified)

After applying Occam's Razor, log **only failures**:

**Log to `.learnings/simplifications.md`:**
```markdown
- [YYYY-MM-DD] {what was removed} → {outcome}
```

**Log if:**
*   Pruning caused a bug
*   Over-pruning required restoration
*   Second-order workaround created more complexity

**Do NOT log** routine successful prunes — this overhead exceeds value.

## Pattern Categories (Prioritized)

**High-Impact (Prune First):**
- Unused exports / dead code
- Passthrough classes with no logic
- Wrapper libraries around native features

**Medium-Impact (Verify Before):**
- Abstraction layers over stable internals
- Configuration that could be hardcoded
- Boilerplate that exceeds code it wraps

**Low-Impact (Leave Alone):**
- Code referenced by unknown callers
- Security-sensitive validation
- Multi-team API boundaries
