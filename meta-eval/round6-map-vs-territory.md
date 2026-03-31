# Meta-Evaluation: map-vs-territory

## 1. chestertons-fence
**What it reveals:** The skill contains several "fences" protecting against false confidence:
- Step 2 "The Probe" explicitly forbids reading code and mandates running it
- The "Fallback" mechanism when code cannot be run directly
- The self-improvement protocol forces documentation updates when Map ≠ Territory

**Weaknesses:** 
- No guidance on *how much* runtime verification is sufficient—a single `print()` might miss edge cases
- The "Map is Wrong" conclusion (Step 3) is a strong assumption; sometimes both Map and Territory are wrong
- No "fence" around when NOT to apply this skill—running code in production without safeguards could cause harm

**Enhancement:** Add a pre-check: "Is running code safe in this context?" to prevent reckless production debugging.

---

## 2. decision-matrix
**What it reveals:** The skill does NOT use decision-matrix thinking—it prescinds from weighing alternatives.

**When runtime verification is better than decision-matrix:**
- When documentation and code disagree (the core use case), running code gives binary truth: works/doesn't work
- When stakes are high and time is short, runtime proof outweighs analytical prediction
- When the "Map" (docs) has low credibility anyway—decision matrices assume inputs are estimable

**Weakness:** The skill never helps you *decide when* to trust the Map vs Territory. It assumes always distrust the Map, but sometimes docs are correct and code is wrong (e.g., compiler bugs, hardware failures).

**Enhancement:** Add a "credibility scoring" step: Rate doc reliability (1-5) before jumping to runtime verification.

---

## 3. first-principles-thinking
**What it reveals:** The basic truth "Map ≠ Territory" is correct but oversimplified:

**Atomic units of the problem:**
- **Map:** Any representation of reality (docs, comments, types, variable names, mental models)
- **Territory:** The actual runtime state (memory values, network responses, disk state)
- **The gap:** Maps are static snapshots; Territory is dynamic and stateful

**Weakness:** The skill assumes the gap is always a "Map problem." But Territory can also be wrong—bugs in code produce wrong runtime behavior. The skill doesn't address "the code itself is wrong."

**Enhancement:** Add Step 0: "Confirm Territory is correct." If the runtime behavior itself is buggy, running it just confirms the wrong thing.

---

## 4. inversion-thinking
**What it reveals:** The failures this skill PREVENTS:
- Trusting outdated documentation
- Debugging the wrong thing based on misleading variable names
- Integration failures from API drift
- Type errors that pass type-checking but fail at runtime

**Weakness:** No guardrails on the skill's own advice. If applied incorrectly, the skill could:
- Cause production incidents by running unvetted code
- Waste time verifying trivially correct Maps
- Create "verification theater" without meaningful checks

**Enhancement:** Add "Anti-Goals" section: What failures does this skill CAUSE if misapplied?

---

## 5. map-vs-territory (self-referential)
**Can you verify the verification methodology itself? YES:**

| Meta-Level Check | Question | Status |
|-----------------|----------|--------|
| Is the skill's own docs accurate? | Does SKILL.md correctly describe its method? | ✅ Auditable |
| Does the self-improvement protocol close the loop? | Will corrections improve the skill over time? | ⚠️ Untested |
| Is there a "Map" of the skill itself? | The 3-step protocol is a Map—does Territory confirm it works? | ⚠️ No data |

**Weakness:** The skill has no self-referential "verify your verification" step. If an agent applies this skill incorrectly, there's no feedback mechanism to catch the failure.

**Enhancement:** Add a "Smoke Test" for the skill itself: Apply to a known case (e.g., "Does `ls` list files?") and verify the protocol produces correct results.

---

## 6. occams-razor
**Is the 3-step protocol minimal or over-engineered?**

| Aspect | Assessment |
|--------|------------|
| Steps | ✅ Minimal—just Doubt, Probe, Update |
| Self-improvement protocol | ⚠️ Could be seen as overhead |
| Pattern categories | ✅ Useful but not required for every use |
| Logging corrections | ⚠️ Overhead if never reviewed |

**Verdict:** The core 3-step protocol is perfectly minimal. The Self-Improvement Protocol is valuable but only if corrections are actually reviewed.

**Weakness:** The skill doesn't help you decide WHEN the overhead of logging is worth it. For one-off debugging, logging is noise.

**Enhancement:** Add a threshold: "Log only when the discrepancy reveals a pattern, not a one-off."

---

## 7. pareto-principle
**What code/doc discrepancies cause 80% of bugs?**

Based on the skill's Pattern Categories, the high-impact 20%:

| Discrepancy Type | Frequency | Impact |
|-----------------|-----------|--------|
| **Type annotation errors** | High | Critical—causes runtime crashes |
| **API drift** | Medium | High—integration failures |
| **Naming lies (isValid)** | High | Medium—logic errors |
| **Outdated docs** | Medium | Low—confusion, not crashes |
| **Comment rot** | Low | Low—rarely causes failures |

**Weakness:** The skill treats all discrepancy types equally. Type annotation errors (TS/Java) are far more dangerous than comment rot.

**Enhancement:** Prioritize the pattern table: "Start with type annotations, then API contracts, then naming, then comments."

---

## 8. rubber-ducking
**Explain Map vs Territory. Where is it confusing?**

**Duck translation:**
> "When debugging, do not trust what the documentation says. Instead, run the code and look at what actually happens."

**Confusion points:**
1. **"Map" is overloaded** — sometimes means docs, sometimes comments, sometimes variable names, sometimes mental models. The skill lists all four but doesn't clarify when each matters.
2. **"Territory" is ambiguous** — Does it mean logs? Memory? Network? The examples show `print()`, `console.log()`, HTTP body—but these are all DIFFERENT territories with different reliability.
3. **"The Map is Wrong" is absolute** — In reality, sometimes both Map and Territory are wrong. The skill doesn't address this nuance.
4. **The fallback is weak** — "Ask the user to run it" is not verification; it's delegation without accountability.

**Enhancement:** Disambiguate Territory: Is it (a) local runtime state, (b) logs, (c) external API responses? Each has different reliability.

---

## 9. systems-thinking
**What feedback loops exist between documentation and code changes?**

```
[Developer writes code] → [Code changes Territory]
       ↑                         ↓
[Docs stale] ← [Documentation not updated]
       ↑                         ↓
[Debugging wrong] ← [Map ≠ Territory detected]
```

**Reinforcing loops (R):**
- More complex code → More documentation drift → More debugging confusion → More "fixes" that introduce more complexity
- Skill used often → Corrections logged → Patterns identified → Better skill → Used more often

**Balancing loops (B):**
- Map is wrong → Probe runs → Map updated → Alignment restored

**Delay effects:**
- Documentation drift accumulates silently until a crisis debugging session surfaces it
- Corrections may never be reviewed if "weekly review" isn't enforced

**Weakness:** No acknowledgment of these loops. Users may think they're solving a one-off problem when they're fighting a systemic issue.

**Enhancement:** Add a "System Health Check": "If you find Map ≠ Territory frequently, the real problem is the documentation update process, not the individual discrepancies."

---

## 10. second-order-thinking
*(Note: second-order-thinking is not an available skill in the agent's toolkit. This analysis applies second-order reasoning manually.)*

**What happens when you trust the Map too long?**

| Time Horizon | Consequence |
|--------------|-------------|
| **Immediate** | Wasted debugging time chasing the wrong thing |
| **Medium** | Mental model drifts further from reality; "obvious" fixes fail |
| **Long** | Team develops lore and workarounds that encode the Map's errors; new members are confused; velocity drops |
| **Escalation** | Production incidents caused by assumptions that "should be true" |

**The trap:** Once you trust the Map, you stop questioning it. Each debugging session adds evidence to your (wrong) mental model. Confirmation bias builds. The Map becomes a prison.

**Weakness:** The skill has no "detox" protocol for teams that have been trusting wrong Maps for too long.

**Enhancement:** Add a "Map Audit" for legacy systems: "If Map ≠ Territory has been found >5 times, reset assumptions entirely."

---

## Summary

### Strengths
- **Clarity:** The 3-step protocol (Doubt → Probe → Update) is memorable and actionable
- **Strong framing:** "DO NOT READ CODE. RUN CODE." is a powerful anti-dogma
- **Practical examples:** Concrete actions (`print(type(user))`, `console.log(isValid)`) guide implementation
- **Self-improvement loop:** The logging protocol enables pattern learning
- **Addresses real problem:** Documentation-code drift is a universal pain point

### Weaknesses
- **No safety guards:** Running code without context can cause production issues
- **No prioritization:** All discrepancy types treated equally despite vastly different severities
- **Ambiguous terminology:** "Map" and "Territory" are overloaded and context-dependent
- **Self-referential gap:** No mechanism to verify the skill itself is applied correctly
- **No "when NOT to use" guidance:** Over-application wastes time on correct Maps
- **Feedback loop blindness:** No acknowledgment that Map ≠ Territory is often systemic

### Enhancement Recommendations

1. **Add pre-flight checks:**
   - "Is running code safe in this context?"
   - "Is this a one-off or recurring issue?"
   - "Rate Map credibility (1-5) before probing"

2. **Prioritize by impact:**
   - Type annotation errors → Critical (check first)
   - API drift → High (verify before integrating)
   - Naming lies → Medium (rename after confirming behavior)
   - Comment/doc drift → Low (update after core fixes)

3. **Disambiguate "Territory":**
   - Local runtime state (variables, memory)
   - Logs (persisted state)
   - Network responses (external territory)
   - Each requires different verification tactics

4. **Add skill self-verification:**
   - Include a smoke test case with known outcome
   - Log when the skill itself produces incorrect conclusions

5. **Address systemic issues:**
   - If Map ≠ Territory is frequent, recommend documentation process fixes, not just individual corrections

6. **Add warning: Map can be correct:**
   - "The Map is Wrong" assumption is sometimes wrong
   - Include case: "Territory was wrong due to code bug, not Map error"
