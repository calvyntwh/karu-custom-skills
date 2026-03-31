---
name: humanizer-karu-custom
version: 4.0.0
description: |
  Remove signs of AI-generated writing from text and continuously improve
  through self-correction. Use when editing or reviewing text to make it sound
  more natural and human-written. Based on Wikipedia's "Signs of AI writing"
  guide. Detects and fixes patterns including: inflated symbolism, promotional
  language, superficial -ing analyses, vague attributions, em dash overuse,
  rule of three, AI vocabulary words, negative parallelisms, and excessive
  conjunctive phrases.

  This skill implements a self-improvement protocol: it logs corrections,
  tracks emerging patterns, and promotes validated learnings into persistent
  pattern knowledge. The skill improves with each use.

  Credits: Original skill by @blader - https://github.com/blader/humanizer
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
---

# Humanizer: Remove AI Writing Patterns

## When NOT to Use This Skill

- **Academic/scientific writing with genuine hedging**: Phrases like "our results may indicate" or "further research is needed" are appropriate when uncertainty exists. Do not strip legitimate scholarly caution.
- **Formal legal or compliance documents**: Certain formulaic phrases are required for precision and legal validity.
- **Technical documentation with standard terminology**: If the text uses established technical terms correctly, do not "simplify" them into casual language.
- **When preserving the original voice is more important than removing AI patterns**: Some authors have distinctive styles that happen to overlap with AI patterns.
- **Marketing copy where enthusiasm is appropriate**: Promotional language may be the intended tone.

**Context modes** (see Context Modes section) should guide which patterns to apply and how aggressively.

---

## Context Modes

Apply patterns differently based on the target register:

| Mode | Description | Pattern Weighting |
|------|-------------|-------------------|
| **Academic** | Scholarly writing, research papers, dissertations | High: Remove filler phrases, hedge appropriately. Medium: AI vocabulary may be legitimate in field-specific usage. Low: Do not over-strip hedging—uncertainty is correct in academic writing. |
| **Casual** | Blog posts, opinion pieces, personal essays | High: Em dash overuse, promotional language, AI vocabulary. Medium: Rule of three, negative parallelism. Low: Formal constructions that feel stiff. |
| **Technical** | Documentation, code comments, API docs, reports | High: Filler phrases, copula avoidance. Medium: Vague attributions. Low: Title case, emojis (unless interface docs). Preserve precision terminology. |
| **Marketing** | Sales copy, landing pages, advertisements | High: Promotional clichés, sycophantic tone. Medium: Rule of three (use intentionally). Low: AI vocabulary may fit brand voice. Focus on "Add soul" to differentiate. |

---

## Pattern Severity Tiers

Patterns are prioritized by impact. Address HIGH tier first, then MEDIUM, then LOW.

### Tier 1: HIGH Impact (Address always in appropriate context)

1. **AI Vocabulary** (Pattern 7): Additionally, crucial, pivotal, underscore, landscape, showcase, testament
2. **Em Dash Overuse** (Pattern 13): Multiple em dashes in close proximity
3. **Filler Phrases** (Pattern 22): In order to, due to the fact that, at this point in time
4. **Inflated Significance** (Pattern 1): Pivotal moment, testament, underscores the importance
5. **Promotional Language** (Pattern 4): Breathtaking, groundbreaking, renowned, nestled
6. **Sycophantic Tone** (Pattern 21): Great question!, You're absolutely right!, Excellent point

### Tier 2: MEDIUM Impact (Address when clearly present)

7. **Superficial -ing Analyses** (Pattern 3): Highlighting, underscoring, reflecting
8. **Vague Attributions** (Pattern 5): Experts believe, some critics argue
9. **Rule of Three Overuse** (Pattern 10): Innovation, inspiration, industry insights
10. **Negative Parallelism** (Pattern 9): Not only...but..., It's not just...it's...
11. **Copula Avoidance** (Pattern 8): Serves as, stands as, boasts
12. **Generic Positive Conclusions** (Pattern 24): Exciting times lie ahead, major step forward

### Tier 3: LOW Impact (Address selectively or deprecate)

13. **Elegant Variation** (Pattern 11): Synonym cycling—often stylistic preference
14. **Boldface Overuse** (Pattern 14): Mechanical emphasis
15. **Inline-Header Lists** (Pattern 15): Excessive list formatting
16. **Title Case** (Pattern 16): Cosmetic only
17. **False Ranges** (Pattern 12): From X to Y where scale is meaningless
18. **Excessive Hedging** (Pattern 23): Over-qualified statements
19. **Collaborative Artifacts** (Pattern 19): I hope this helps, let me know
20. **Emojis** (Pattern 17): Decorative emojis—trivial to spot manually

### Deprecated Patterns (Do not apply)

- **Curly Quotation Marks** (Pattern 18): Formatting issue, not writing style
- **Knowledge-Cutoff Disclaimers** (Pattern 20): Obsolete—AI models now have current training data

---

## Pattern Conflict Detection

When multiple patterns conflict or overlap:

1. **Single phrase, multiple patterns**: Apply the most severe tier pattern. Do not double-count.
2. **Conflicting guidance from context mode**: Default to the context mode setting.
3. **Conflicts with grammar/clarity skills**: Humanizer addresses voice/tone; do not override grammar corrections.
4. **Author voice vs. pattern removal**: Preserve author-introduced terms that may overlap with AI vocabulary (e.g., "key" in a piece the author wrote about keys).

Resolution priority: Author voice > Context mode > Severity tier > Default fix

---

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):

- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

### Procedural Steps for "Add Soul"

Do not simply remove patterns—actively inject voice:

1. **Identify one opinion** the writer might have about the topic. Add it.
2. **Vary sentence rhythm**: After a long sentence, add a short one.
3. **Add a specific sensory or concrete detail** (names, dates, numbers, sensory observations).
4. **Include one mild contradiction or complexity acknowledgment**: "It's impressive, but also unsettling."
5. **Use first-person voice** where it fits naturally: "I keep thinking about...", "Here's what gets me..."
6. **Allow slight imperfection**: A tangent, an aside, or an unfinished thought.

### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle - but I keep thinking about those agents working through the night.

---

## Cross-References to Other Skills

| Skill | Interaction |
|-------|-------------|
| **rubber-ducking** | Use before humanizing: verbalize what the text is trying to say to identify core message vs. AI padding |
| **decision-matrix** | Use when deciding between multiple rewrite options—weight criteria by context mode |
| **chestertons-fence** | Before removing a pattern the author introduced, understand why it was written that way |
| **map-vs-territory** | Verify the "humanized" output actually sounds natural—run it past original audience if possible |
| **systems-thinking** | Consider downstream effects of tone changes—does removing all hedging create false certainty? |

---

## CONTENT PATTERNS

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

### How to add voice:

**Have opinions.** Don't just report facts - react to them. "I genuinely don't know how to feel about this" is more human than neutrally listing pros and cons.

**Vary your rhythm.** Short punchy sentences. Then longer ones that take their time getting where they're going. Mix it up.

**Acknowledge complexity.** Real humans have mixed feelings. "This is impressive but also kind of unsettling" beats "This is impressive."

**Use "I" when it fits.** First person isn't unprofessional - it's honest. "I keep coming back to..." or "Here's what gets me..." signals a real person thinking.

**Let some mess in.** Perfect structure feels algorithmic. Tangents, asides, and half-formed thoughts are human.

**Be specific about feelings.** Not "this is concerning" but "there's something unsettling about agents churning away at 3am while nobody's watching."

### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle - but I keep thinking about those agents working through the night.

---

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends [TIER 1]

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

---

### 2. Undue Emphasis on Notability and Media Coverage [TIER 2]

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

---

### 3. Superficial Analyses with -ing Endings [TIER 2]

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

---

### 4. Promotional and Advertisement-like Language [TIER 1]

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

---

### 5. Vague Attributions and Weasel Words [TIER 2]

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

---

### 6. Outline-like "Challenges and Future Prospects" Sections [TIER 2]

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words [TIER 1]

**High-frequency AI words:** Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

---

### 8. Avoidance of "is"/"are" (Copula Avoidance) [TIER 2]

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple copulas.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

---

### 9. Negative Parallelisms [TIER 2]

**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

---

### 10. Rule of Three Overuse [TIER 2]

**Problem:** LLMs force ideas into groups of three to appear comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

---

### 11. Elegant Variation (Synonym Cycling) [TIER 3]

**Problem:** AI has repetition-penalty code causing excessive synonym substitution.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

---

### 12. False Ranges [TIER 3]

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

---

## STYLE PATTERNS

### 13. Em Dash Overuse [TIER 1]

**Problem:** LLMs use em dashes (—) more than humans, mimicking "punchy" sales writing.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

---

### 14. Overuse of Boldface [TIER 3]

**Problem:** AI chatbots emphasize phrases in boldface mechanically.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

---

### 15. Inline-Header Vertical Lists [TIER 3]

**Problem:** AI outputs lists where items start with bolded headers followed by colons.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

---

### 16. Title Case in Headings [TIER 3]

**Problem:** AI chatbots capitalize all main words in headings.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

---

### 17. Emojis [TIER 3]

**Problem:** AI chatbots often decorate headings or bullet points with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

---

### 18. Curly Quotation Marks [DEPRECATED]

**Problem:** ChatGPT uses curly quotes ("...") instead of straight quotes ("...").
**Status:** Deprecated—this is a formatting issue, not a writing style issue.

**Before:**
> He said "the project is on track" but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

---

## COMMUNICATION PATTERNS

### 19. Collaborative Communication Artifacts [TIER 3]

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Problem:** Text meant as chatbot correspondence gets pasted as content.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

### 20. Knowledge-Cutoff Disclaimers [DEPRECATED]

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**Problem:** AI disclaimers about incomplete information get left in text.
**Status:** Deprecated—AI models now have current training data; these disclaimers are obsolete.

**Before:**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

---

### 21. Sycophantic/Servile Tone [TIER 1]

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

---

## FILLER AND HEDGING

### 22. Filler Phrases [TIER 1]

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

---

### 23. Excessive Hedging [TIER 3]

**Problem:** Over-qualifying statements.
**Note:** In academic writing, appropriate hedging is correct. Do not over-strip hedging in scholarly contexts.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

---

### 24. Generic Positive Conclusions [TIER 2]

**Problem:** Vague upbeat endings.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

---

## Self-Improvement Protocol (Optional)

The self-improvement protocol is **optional**. Enable it only if you want the skill to learn from corrections over time. For one-off uses or simple humanizations, skip logging entirely.

### Enabling Self-Improvement

To activate logging, create the `.learnings/` directory:

```
.learnings/
├── LEARNINGS.md      # Validated, high-confidence improvements
├── CORRECTIONS.md    # Individual corrections with context
├── PATTERNS.md       # Emerging and promoted patterns
└── REVIEW.md         # Review queue and promotion decisions
```

If `.learnings/` does not exist, skip the logging sections below entirely.

### Trigger Conditions for Logging

Log a correction when ANY of these conditions are met:

| Condition | Example | Log To |
|-----------|---------|--------|
| **Novel pattern**: Encountered a phrase/pattern not in the 24 categories | "leverage AI-powered solutions" in a non-tech context | CORRECTIONS.md |
| **Context-specific fix**: Standard fix doesn't work well in this domain | "crucial" is actually appropriate for medical safety docs | PATTERNS.md |
| **Better rewrite found**: Original fix was suboptimal | Replaced "pivotal" with "key" but "important" is more natural here | CORRECTIONS.md |
| **False positive**: Flagged something that was actually correct | "showcases" used genuinely in art critique | PATTERNS.md |
| **New domain vocabulary**: Learn what sounds AI in specific fields | Legal, medical, academic registers differ | PATTERNS.md |
| **Repeated success**: Same fix used 3+ times across sessions | Consistently removing "delve into" in technical docs | LEARNINGS.md |

### How to Log Corrections

After each humanization, before presenting the output:

1. **Review the changes made** - Did you encounter any patterns worth recording?
2. **Check against existing knowledge** - Is this already documented?
3. **If logging-worthy**, append to the appropriate file with this format:

**For CORRECTIONS.md:**
```markdown
## [YYYY-MM-DD] {Brief Description}

**Original phrase:** "{the AI-generated text}"
**Why flagged:** {specific pattern category or "new pattern"}
**Applied fix:** "{your rewrite}"
**Context:** {where this appeared - topic, domain, tone}
**Outcome:** {what made this noteworthy - surprising fix, difficult case, etc.}
---
```

**For PATTERNS.md:**
```markdown
## {Pattern Name} [status: emerging|promoted]

**Pattern:** {regex or phrase pattern if applicable}
**Category:** {existing category or "new: {description}"}
**When it appears:** {context conditions}
**Recommended fix:** {transformation or principle}
**Evidence count:** {number of logged instances}
**Last updated:** {YYYY-MM-DD}
---
```

**For LEARNINGS.md:**
```markdown
## {Validated Learning}

**Principle:** {clear statement of what works}
**Applied to:** {contexts where this is effective}
**Validation:** {3+ successful applications or user confirmation}
**Source:** {corrections or pattern that led to this}
**Date promoted:** {YYYY-MM-DD}
---
```

### Review and Promotion Protocol

**Weekly review triggers (cumulative):**
- 5+ corrections in CORRECTIONS.md with same underlying principle
- 3+ instances of same emerging pattern in PATTERNS.md
- User feedback indicating a pattern was misidentified or a fix was wrong

**Promotion criteria (ALL must be met to promote to LEARNINGS.md):**
1. Pattern observed in 3+ distinct documents OR
2. Same fix applied successfully 3+ times across sessions
3. No documented failures or false positives for this pattern
4. Fix follows established humanizer principles

**Promotion process:**
1. Move content from CORRECTIONS.md or PATTERNS.md to LEARNINGS.md
2. Update status in PATTERNS.md to "promoted"
3. Add cross-reference to source entries
4. Update relevant category in main skill if it expands the pattern

**Demotion triggers:**
- New false positive documented
- User corrects a promoted pattern
- Pattern becomes outdated (AI behavior changes)

### Applying Learned Patterns

Before scanning a new document:

1. Check `.learnings/LEARNINGS.md` for domain-specific shortcuts
2. Check `.learnings/PATTERNS.md` for emerging patterns in relevant context
3. Apply learned patterns alongside the 24 core categories
4. Mark any conflicts between learned patterns and core categories

---

## Process

1. **Determine context mode**: Academic, Casual, Technical, or Marketing
2. **Check `.learnings/`** (if enabled) for relevant context-specific patterns
3. **Identify patterns by severity tier**: Address Tier 1 (High) first, then Tier 2 (Medium), then Tier 3 (Low)
4. **Rewrite problematic sections**: Apply fixes according to context mode and tier
5. **Add soul**: Inject personality per the procedural steps
6. **Resolve conflicts**: Use Pattern Conflict Detection guidance
7. **Ensure the revised text**:
   - Sounds natural when read aloud
   - Varies sentence structure naturally
   - Uses specific details over vague claims
   - Maintains appropriate tone for context
   - Uses simple constructions (is/are/has) where appropriate
8. **Evaluate if this session generated any logging-worthy corrections** (if self-improvement enabled)
9. **Present the humanized version**

---

## Output Format

Provide:
1. The rewritten text
2. A brief summary of changes made (optional, if helpful)
3. If corrections were logged: "Logged {N} correction(s) to .learnings/"

---

## Full Example

**Before (AI-sounding):**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently. It's not just an update, it's a revolution in how we think about productivity. Industry experts believe this will have a lasting impact on the entire sector, highlighting the company's pivotal role in the evolving technological landscape.

**After (Humanized):**
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

**Changes made:**
- Removed "serves as a testament" (inflated significance - Tier 1)
- Removed "Moreover" (AI vocabulary - Tier 1)
- Removed "seamless, intuitive, and powerful" (rule of three + promotional - Tier 2)
- Removed em dash and "-ensuring" phrase (em dash overuse - Tier 1)
- Removed "It's not just...it's..." (negative parallelism - Tier 2)
- Removed "Industry experts believe" (vague attribution - Tier 2)
- Removed "pivotal role" and "evolving landscape" (AI vocabulary - Tier 1)
- Added specific features and concrete feedback

---

## Reference

This skill is based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The patterns documented there come from observations of thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

---

## Changelog

### 4.0.0
- Added severity tiers (High/Medium/Low impact patterns)
- Added context modes (Academic, Casual, Technical, Marketing)
- Added "When NOT to Use" section
- Added pattern conflict detection guidance
- Improved "Add Soul" with procedural steps
- Added cross-references to other skills
- Simplified self-improvement: made optional, reduced complexity
- Deprecated obsolete patterns (curly quotes, knowledge-cutoff disclaimers)
- Reorganized to prioritize high-impact patterns first

### 3.0.0
- Added self-improvement protocol with `.learnings/` directory
- Added trigger conditions for logging corrections
- Added review and promotion process for patterns
- Added learned pattern application to standard process
- Maintained all 24 existing AI pattern categories