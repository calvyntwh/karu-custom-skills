---
name: map-vs-territory
description: Empiricism and Reality Checking. Prioritizing runtime truth over documentation. Use when debugging discrepancies, validating APIs, or when code comments might be outdated.
license: MIT
---

# Map vs. Territory (The Reality Check)

> "The map is not the territory." - Alfred Korzybski

## When to Use
*   **Debugging:** When "it should work" but doesn't.
*   **Integration:** When using 3rd party APIs or libraries.
*   **Legacy Code:** When comments don't match the code.

## When NOT to Use
*   **Production safety-critical paths:** Running unvetted code in production can cause incidents.
*   **Trivially correct Maps:** When docs are clearly correct and code is obviously right.
*   **High-uncertainty scenarios:** When running code could have irreversible side effects (e.g., `DROP TABLE`, payment processing).
*   **Already-verified code:** Code you've already run and tested in this session.

> [!WARNING]
> **Pre-flight check:** "Is running code safe in this context?" If the answer is uncertain, do NOT run. Use alternative verification (code review, asking a human, feature flags).

## Prioritization by Impact

Investigate discrepancies in this order:

| Priority | Discrepancy Type | Impact | Investigation |
|----------|-------------------|--------|---------------|
| **1 (Critical)** | Type annotation errors | Runtime crashes | Check `type()` or `typeof` first |
| **2 (High)** | API contract drift | Integration failures | Test actual API response |
| **3 (Medium)** | Naming lies (`isValid`, `canDo`) | Logic errors | Evaluate variable at runtime |
| **4 (Low)** | Comment/doc drift | Confusion | Update docs after core fixes |

> [!NOTE]
> If you find Map ≠ Territory **frequently**, the problem is systemic. Recommend fixing the documentation update process, not just individual discrepancies.

## The Protocol: The Reality Check
Do not trust the Map (Docs, Comments, Variable Names).
Trust the Territory (Logs, Memory, Disk, Network).

### 1. The Doubt
Identify the "Map" you are relying on.
*   *"The comment says this function returns a User."*
*   *"The variable is named `isValid`."*
*   *"The API docs say it returns 200 OK."*

### 2. The Probe
Active verify the Territory.

> [!IMPORTANT]
> **DO NOT READ CODE. RUN CODE.**
> Reading code is reading the Map. Running code is touching the Territory.

### Pre-Flight Checklist (Before Probing)
- [ ] **Is running code safe in this context?** (No production side effects)
- [ ] **Is this a one-off or recurring issue?** (Recurring suggests systemic problem)
- [ ] **Rate Map credibility (1-5):** Low credibility = probe first

### Territory Types & Verification Tactics

| Territory Type | How to Verify | Example |
|----------------|---------------|---------|
| **Local runtime state** | `print()`, `console.log()`, inspect variable | `type(user)`, `len(items)` |
| **Logs** | Read persisted output | Server logs, error traces |
| **Network responses** | HTTP client, curl | Raw HTTP body, status code |
| **Disk state** | File read, ls | Check if file exists, read content |

> [!TIP]
> **Fallback:** If you cannot run code directly: (1) Read the code itself, (2) Search for related comments/tickets, (3) Ask a senior developer.

### 3. The Update
If Map $\neq$ Territory, **The Map is Wrong.**

> [!WARNING]
> Sometimes **Territory is wrong**, not the Map. If the runtime behavior itself is buggy (not just outdated), the Map was correctly describing intended behavior. Investigate whether the code has a bug.

*   Update the docs/comments.
*   Rename the variable (`isValid` -> `shouldBeValid`).
*   Fix the mental model.

## Self-Improvement Protocol

> [!TIP]
> **Simplified mode:** Logging is OPTIONAL. Only log when you discover a recurring pattern.

### Logging Corrections (Optional)

**Log to `.learnings/CORRECTIONS.md`:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Map (what was believed):** {doc/comment/variable}
**Territory (reality):** {what actually happened}
**Discrepancy type:** {outdated | wrong | misleading}
**Fix applied:** {what was corrected}
---
```

### Trigger Conditions

Only log when the discrepancy reveals a **pattern**:

| Condition | Example | Log? |
|-----------|---------|------|
| Same discrepancy type 3+ times | "Type annotations wrong in 5 places" | ✅ |
| Systemic pattern found | "Legacy API docs always outdated" | ✅ |
| New category discovered | "Naming lie pattern in auth code" | ✅ |
| Single one-off | "One comment was wrong" | ❌ |

### Pattern Categories for This Skill

- **Outdated docs**: Old behavior, deprecated features
- **Naming lies**: isValid, canDo, hasAccess patterns
- **API drift**: Docs vs implementation diverged
- **Type annotation errors**: TypeScript/Java types wrong
- **Comment rot**: Comments never updated

## Skill Integration

| Skill | Relationship | When to Chain |
|-------|--------------|---------------|
| **chestertons-fence** | Git archaeology is a map probe | When git history is sparse, fall back to this skill |
| **rubber-ducking** | Goal Alignment Check is a map check | When code looks right but user goal is wrong |
| **decision-matrix** | For weighing evidence | When multiple Maps conflict |
| **systems-thinking** | Map ≠ Territory often systemic | If frequent, fix the documentation process |

## Resources
*   [Detailed Research Notes](references/research.md)
