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

*   *Action:* `print(type(user))` -> Is it actually a User object? or a Dict? or None?
*   *Action:* `console.log(isValid)` -> Is it `true`? `1`? `"true"`?
*   *Action:* Inspect the raw HTTP body.

> [!TIP]
> **Fallback:** If you cannot run code directly, ask the user to run it and report the output.

### 3. The Update
If Map $\neq$ Territory, **The Map is Wrong.**
*   Update the docs/comments.
*   Rename the variable (`isValid` -> `shouldBeValid`).
*   Fix the mental model.

## Self-Improvement Protocol

This skill learns documentation-to-reality discrepancies.

### Logging Corrections

After applying Map vs Territory:

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

| Condition | Example | Log? |
|-----------|---------|------|
| Doc was outdated | "Comment said X but code was Y" | ✅ |
| Variable name lied | "`isValid` was actually always false" | ✅ |
| API differed from docs | "API returned error, docs said 200" | ✅ |
| Type annotation wrong | "Type said User, runtime was Dict" | ✅ |
| Comment was misleading | "The comment had it backwards" | ✅ |
| Map was correct | "Actually the code was wrong, not the doc" | ✅ |

### Pattern Categories for This Skill

- **Outdated docs**: Old behavior, deprecated features
- **Naming lies**: isValid, canDo, hasAccess patterns
- **API drift**: Docs vs implementation diverged
- **Type annotation errors**: TypeScript/Java types wrong
- **Comment rot**: Comments never updated

### Review & Promote

**Weekly:** Check for recurring discrepancy patterns → Add to LEARNINGS.md
