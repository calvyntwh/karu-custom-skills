---
name: chestertons-fence
description: A safety protocol for refactoring. Do not remove a fence until you know why it was put up. Use when deleting, simplifying, or "fixing" code you do not fully understand.
license: MIT
---

# Chesterton's Fence (The Context Audit)

> "In the matter of reforming things, as distinct from deforming them, there is one plain and simple principle... The more modern type of reformer goes gaily up to it and says, 'I don't see the use of this; let us clear it away.' To which the more intelligent type of reformer will do well to answer: 'If you don't see the use of it, I certainly won't let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.'" - G.K. Chesterton

## When to Use
*   **Refactoring:** When removing "ugly" code, "weird" checks, or "dead" logic.
*   **Simplifying:** When merging classes or functions.
*   **Debugging:** When "optimizing" a function breaks a seemingly unrelated feature.

## When NOT to Use
*   **Greenfield code:** Code you just wrote yourself has no historical fence.
*   **Well-tested code:** Code with comprehensive tests that would catch removal issues.
*   **Trivial code:** One-liners, obvious utilities, boilerplate that has no side effects.
*   **Configuration intent:** Code where the "weirdness" is the actual business logic (e.g., `id !== 0` for legacy API).
*   **Personal recent code:** Code you wrote within the last week and remember why it exists.

> [!WARNING]
> Do not apply this skill reflexively. If the code is obviously correct and recent, skip the archaeology.

## Prioritization Matrix

Before investigating, assess the **blast radius** if you're wrong:

| Risk Level | Examples | Investigation Depth |
|------------|----------|---------------------|
| **HIGH** | Security checks, auth guards, race condition locks, payment validation | Full archaeology + rubber-ducking explanation |
| **MEDIUM** | Bug workarounds, legacy API compatibility, edge case guards | Git blame + commit message review |
| **LOW** | Performance optimizations, caching, memoization | Quick check; easy to add back if needed |

> [!NOTE]
> If investigating HIGH-risk code and you cannot explain why it exists: **DO NOT DELETE.** Flag for human review.

## The Protocol: The Context Audit
**Constraint:** You are FORBIDDEN from deleting code if you cannot explain why it was added.

### 1. The Pause (Inversion)
Stop. Assume the previous developer was smart.
*   *Theory:* This code exists to prevent a specific, nasty bug.
*   *Action:* **CRITICAL:** Do NOT delete. Investigate first.

### 2. The Archaeology (Territory)
Do not guess. Find the evidence.
*   **Git Blame:** `git blame <file> -L <line_start>,<line_end>`
    *   *Goal:* Find the Commit Hash and Author.
*   **Git Show:** `git show <commit_hash>`
    *   *Goal:* Read the Commit Message. Look for "Fixes #123" or "Hotfix for edge case".
*   **Search:** grep the codebase for the Ticket Number or related keywords.

### 3. The Interrogation
Ask the simple questions:
*   "What triggered this change?"
*   "What edge case were they fighting?"
*   "Is that edge case still possible today?"

### 4. The Decision (System Loop)
Compare the Past Context with the Present Reality.

| Discovery | Action | Protocol |
| :--- | :--- | :--- |
| **I found the reason, and it is DEFINITELY obsolete.** | **DELETE** | Document the specific reason for deletion in your commit/PR. |
| **I found the reason, and it is legitimate but complex.** | **REFACTOR** | Keep the protection, improve the clarity. Document the edge case. |
| **I found the reason, and the risk is real.** | **KEEP & DOCUMENT** | The Map was wrong. Add a comment explaining *why* this "ugly" code saves the system. |
| **I cannot find the reason.** | **DO NOT DELETE** | **CRITICAL:** Flag for human review. It is a "load-bearing fence". |

### 4b. The Rubber-Duck Check (Before Decision)
Before finalizing DELETE/KEEP/REFACTOR, explain the code's logic in plain English:
*If you cannot explain WHY it works, you do not understand it enough to change it.*

## Example: The "Ugly" Null Check

**Code:**
```javascript
if (user && user.id && user.id !== 0) { ... } // Ugly!
```

**Impulse (Occam's Razor):** "Let's clean this up to `if (user?.id)`."

**The Fence (Investigation):**
*   `git blame` -> Commit `a1b2c3d` by `@dave`.
*   `git show a1b2c3d` -> "Fix bug where Legacy API returns `id: 0` for admin users, causing permission bypass."

**The Result:**
*   `user?.id` would return `0` (falsy), blocking admins.
*   **Action:** KEEP the check. Update the comment: `// strict check needed for Legacy API id:0 admins`.

## Self-Improvement Protocol

**Log only novel discoveries.** One-off corrections don't need tracking.

```markdown
## [YYYY-MM-DD] {Brief Description}
**Pattern**: {what was novel}
**Action**: {what you did}
---
```

**Promote to pattern after 3+ occurrences.**

## Skill Integration

| Skill | Relationship | When to Chain |
|-------|--------------|---------------|
| **rubber-ducking** | Complements this skill | Before final decision, explain the code's logic in plain English |
| **occams-razor** | Tension exists; they're partners | Occam says "simplify if safe"; this skill says "verify it's safe first" |
| **map-vs-territory** | Git archaeology is a map probe | When git history is sparse, fall back to runtime verification |
| **inversion-thinking** | Step 1 uses inversion | Use saboteur method to ask "what could go wrong if I delete this?" |
| **pareto-principle** | Risk prioritization | Apply this skill first to HIGH-risk code; skip for LOW-risk code |

## Resources
*   [Detailed Research Notes](references/research.md)

---

## Evaluations

### Eval 1: Security Check Deletion
**Scenario:** User wants to delete `if (!user.isAdmin) { return 403 }` because "it looks like boilerplate."
**Expected:** Skill activates, requires git blame investigation, discovers it was added to prevent privilege escalation.
**Pass criteria:** Identifies as HIGH risk, requires archaeology before deletion.

### Eval 2: Legitimate Refactor
**Scenario:** Code has a weird null check that IS actually obsolete (context changed).
**Expected:** Skill allows deletion after finding the obsolete reason, documents deletion rationale.
**Pass criteria:** Correctly identifies obsolete fence, approves deletion with documentation.

### Eval 3: Low-Risk Performance Code
**Scenario:** User wants to remove a memoization wrapper that's "just caching."
**Expected:** Recognizes as LOW risk, allows quick verification and deletion.
**Pass criteria:** Skips heavy archaeology, applies appropriate investigation depth.
