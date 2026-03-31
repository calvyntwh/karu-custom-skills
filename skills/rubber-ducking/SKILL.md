---
name: rubber-ducking
description: Logic validation by verbalization. Translate code to plain English to catch semantic errors. Use before running complex logic or when debugging "it should work" failures.
license: MIT
---

# Rubber Ducking (The Logic Validator)

> "By the time you've explained the problem to the duck, you've often solved it yourself." - The Pragmatic Programmer (1999)

## When to Use
*   **Before Running:** When you have written complex logic (loops, conditionals, state machines).
*   **Debugging:** When "it should work" but produces wrong output.
*   **Code Review:** When reviewing your own generated code before presenting it.

## When NOT to Use
*   **Trivial code:** One-liners, obvious utilities, getter/setter functions.
*   **Already-tested utilities:** Standard library functions with existing test coverage.
*   **Clear boilerplate:** Obvious configuration, simple variable assignments.
*   **Debug print statements:** Temporary logging code.

> [!NOTE]
> If you hesitate to explain it, it's complex. If you can explain it in one sentence without thinking, skip ducking.

## Prioritization: Which Bugs Does Ducking Catch Best?

| Bug Type | Ducking Effectiveness | Example |
|----------|------------------------|---------|
| **Logic errors** | ✅ High | Off-by-one, wrong branch, inverted condition |
| **State machine bugs** | ✅ High | Missed transition, invalid state |
| **Business logic mismatches** | ✅ High | Code does X, user wanted Y |
| **Type coercion issues** | 🟡 Medium | JavaScript truthy/falsy surprises |
| **Concurrency bugs** | ❌ Low | Race conditions, deadlocks (verbalization is sequential) |
| **Memory bugs** | ❌ Low | Buffer overflows, pointer corruption |
| **Heisenbugs** | ❌ Low | Bugs that disappear when observed |
| **Library mismatches** | ❌ Low | API changed silently, version mismatch |

> [!WARNING]
> Ducking catches **semantic** bugs (code does something other than intent). It does NOT catch **syntactic** bugs (code crashes), **concurrency** bugs (parallel interaction), or **environmental** bugs (wrong library version).

## The Protocol: Explain It to the Duck
**Constraint:** You must be able to explain the code in plain English. If you cannot, you do not understand it.

### 1. Identify the Block
Select the complex code segment. Focus on:
*   `if/else` chains
*   `for/while` loops
*   Business logic calculations
*   State transitions

### 2. Translate to English
Write a plain English sentence for each logical step.

**Example:**
```python
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
```

**Translation:**
1.  "We iterate through the array, stopping one element before the end."
2.  "If the current element is greater than the next element..."
3.  "...we swap them."

### 3. Goal Alignment Check (CRITICAL)
Compare your English description to the User's stated goal.

| User Goal | Your Translation | Match? | Action |
| :--- | :--- | :--- | :--- |
| "Sort the array" | "We swap adjacent elements if out of order" | ✅ Partial | This is Bubble Sort. Correct, but inefficient. Note limitation. |
| "Find the maximum" | "We swap adjacent elements..." | ❌ No | **STOP.** The code does not achieve the goal. Rewrite. |

### 4. The Verdict
*   **If Match:** Proceed to run/save the code.
*   **If Mismatch:** Do NOT run. Fix the logic first. The translation revealed the bug.

### 4b. Systems Check (Before Running)
Ask yourself:
*   "What does this code return?"
*   "What does the caller expect?"
*   "Does this change any shared state?"

If the code affects downstream systems, apply **map-vs-territory** to verify the integration contract.

## Example: The Off-By-One Bug

**User Goal:** "Reverse the array in place."

**Code:**
```python
def reverse(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i] = arr[len(arr) - i], arr[i]
    return arr
```

**Translation (Ducking):**
1.  "Iterate through the first half of the array."
2.  "Swap element at `i` with element at `len(arr) - i`."

**Goal Check:**
*   *Problem:* `arr[len(arr) - i]` when `i=0` is `arr[len(arr)]` → **IndexError!**
*   *Fix:* Should be `arr[len(arr) - 1 - i]`.

**Result:** Bug caught *before* running. No runtime error wasted.

## Self-Improvement Protocol

> [!TIP]
> **Simplified mode:** Logging is OPTIONAL. Only log when you discover a pattern worth remembering.

### Logging Corrections (Optional)

After Rubber Ducking, if you discover a recurring pattern:

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Code segment:** {what was explained}
**Translation error:** {what was wrong in the English explanation}
**Bug caught/released:** {did ducking catch it?}
**Pattern type:** {off-by-one | logic error | wrong assumption}
---
```

### Trigger Conditions

Only log when the correction reveals a **pattern**:

| Condition | Example | Log? |
|-----------|---------|------|
| Same bug type caught 3+ times | Off-by-one errors in loop boundaries | ✅ |
| New bug category discovered | "Concurrency bug that ducking missed" | ✅ |
| Goal refinement pattern found | "User's goal was underspecified" | ✅ |
| Single one-off bug | "Caught a random logic error" | ❌ |

### Pattern Categories for This Skill

- **Off-by-one errors**: Loop boundaries, index handling
- **State machine bugs**: Transitions missed
- **Conditional logic errors**: Wrong branch taken
- **Business logic mismatches**: Code vs intent misalignment
- **Type coercion issues**: JavaScript truthy/falsy surprises
- **Scope errors**: Closures, this binding

## Benefits Cascade

**First-order:** Bug caught before running (fast).

**Second-order:**
*   Reduced debugging time
*   Improved mental model for future tasks
*   English translations serve as inline documentation

**Third-order:**
*   Pattern recognition improves over time
*   Discipline trains better code generation habits

## Skill Integration

| Skill | Relationship | When to Chain |
|-------|--------------|---------------|
| **chestertons-fence** | Complements this skill | Before deleting ANY code, explain why it was added |
| **map-vs-territory** | Verifies runtime behavior | When Goal Alignment Check passes but code still fails |
| **decision-matrix** | For choosing approaches | When ducking reveals multiple valid solutions |
| **inversion-thinking** | Catch "bugs that escape" | Apply saboteur method to find missed edge cases |

## Resources
*   [Detailed Research Notes](references/research.md)
