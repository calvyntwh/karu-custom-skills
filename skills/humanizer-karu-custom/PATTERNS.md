# AI Writing Patterns Reference

Detailed pattern documentation with examples. See [SKILL.md](SKILL.md) for the main overview.

---

## Tier 1: HIGH Impact Patterns

### Pattern 1: Undue Emphasis on Significance [TIER 1]

**Words:** stands/serves as, testament, vital/significant/crucial/pivotal, underscores/highlights importance, reflects broader, symbolizing, contributing to, setting the stage for, marks/shapes, represents a shift, key turning point, evolving landscape

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

---

### Pattern 4: Promotional Language [TIER 1]

**Words:** boasts a, vibrant, rich (figurative), profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, breathtaking, must-visit, stunning

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

---

### Pattern 7: Overused AI Vocabulary [TIER 1]

**Words:** Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adj), landscape (noun), pivotal, showcase, tapestry, testament, underscore (verb), valuable, vibrant

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

---

### Pattern 13: Em Dash Usage (Model-Dependent, 2026) [TIER 1, MODEL-DEPENDENT]

**Problem:** Em dash frequency is the most model-specific tell. Different models in 2025–2026 use em dashes at very different rates, so the rule must be calibrated, not absolute.

**Model calibration (2026):**

| Model | Em dash signal | Action |
|-------|----------------|--------|
| Claude (Opus/Sonnet/Haiku) | **HIGH** — 3–4 em dashes per few hundred words is a fingerprint | Always rewrite; replace with period, comma, colon, or parentheses |
| ChatGPT (GPT-5+) | LOW — em dashes are suppressed by training | Leave alone unless writer's sample avoids them |
| Gemini 3 | mixed | Reduce to 1–2 per paragraph |
| Grok | medium | Reduce unless voice uses them |

**Always weak alone for non-Claude sources.** A single em dash needs company from other tells. A writer's voice sample overrides the rule — match the sample's rate. Leave dashes inside code blocks, inline code, commands, paths, and URLs alone.


**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.




---

### Pattern 21: Sycophantic Tone [TIER 1]

**Words:** Great question!, You're absolutely right!, Excellent point, Certainly!

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

---

### Pattern 22: Filler Phrases [TIER 1]

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

---

## Model Era Note (2026)

Patterns P25, P27, P28, P31-P36 are uniform across models (HIGH signal in all). These vary by model:

| Pattern family | Claude | ChatGPT (5.1+) | Gemini | Grok |
|---|---|---|---|---|
| Em dash overuse (P13) | **HIGH** | low (suppressed) | mixed | medium |
| Curly quotes (P18) | low (rare) | **HIGH** | low | medium |
| GPT-5 pattern-heavy transitions (P37) | low | **MEDIUM-HIGH** | medium | medium |
| Claude hedging openers (P38) | **MEDIUM-HIGH** | low | low | low |

---

### Pattern 25: Vague Connection / Association [TIER 1]

**Problem:** LLMs avoid simple `of`/`for`/`by` constructions and reach for indirect phrases (`associated with`, `in connection with`, `particularly/widely associated with`) when describing relationships. Common in newer (2025+) LLMs with retrieval-augmented generation.

**Before:**
> The system has been associated with residential water management applications including swimming-pool backwash and sump-pump discharge.

**After:**
> The system handles residential water from sources including swimming-pool backwash and sump-pump discharge.

---

### Pattern 26: Skipped Heading Levels [TIER 1]

**Problem:** LLMs translate Markdown to wikitext by jumping from level 2 (`==`) to level 4 (`====`), skipping level 3. Rare for manually formatted pages; common in AI output.

**Before:**
> ## Section
> #### Subsection

**After:**
> ## Section
> ### Subsection

---

### Pattern 27: Canned Notability / Media Coverage Parade [TIER 1]

**Problem:** LLMs prove a subject is notable by listing outlets it appeared in. More common in text from AI tools released in 2025 or later.

**Words:** featured in [Outlet A], [Outlet B], and other prominent media outlets, covered by multiple high-quality, independent sources, maintains an active social media presence

**Before:**
> She spoke about AI on CNN, and was featured in Vogue, Wired, Toronto Star, and other media outlets.

**After:**
> She discussed AI on CNN in March 2024, and was profiled in Vogue's November 2023 issue.

---

### Pattern 28: Misattributed Source Analysis [TIER 1]

**Problem:** LLMs with retrieval-augmented generation attach claims to named sources ("Roger Ebert highlighted the lasting influence") regardless of whether those sources actually said anything close. Differs from Pattern 5 (vague attribution) because the source IS named but misrepresented.

**Before:**
> Fridrichová highlights that Blois and Bar perceive truncations as a **distortion of the language rather than an enrichment**, a perspective that still fuels linguistic debates today.

**After:**
> Fridrichová reads Blois and Bar as critical of truncations, not endorsing them.

### Pattern 31: Not X but Y [TIER 1]

**Watch for:** not X but Y; not just, not only, not merely X, but Y; it's not X, it's Y; the reversed form X rather than Y; the same contrast split across sentences ("This does not mean X. It means Y."); clipped negative tails ("..., no guessing").

**Problem:** The negative half names something no one claimed, so the positive half sounds larger. State the point directly. Keep a contrast only when the negative half corrects a belief the reader actually holds, or when both halves carry information.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.
**After:**
> The heavy beat adds to the aggressive tone.

---

### Pattern 32: One-line Closers & Dramatic Fragments [TIER 1]

**Watch for:** a one-sentence paragraph that restates the paragraph before it; "That is the real win."; "Read that again."; "Let that sink in."; the same closer after several sections; a row of fragments ("No aesthetic prior. No nostalgia."); one word in ALL CAPS or with periods between words (`every. single. day.`).

**Problem:** The line asks the reader to pause on a claim instead of adding to it. One short sentence can carry emphasis when it carries a new fact. Cut a closer that repeats. Merge a row of fragments into a sentence with a specific claim.

**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.
**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs.

---

### Pattern 33: Staged Run-Up Before the Point [TIER 1]

**Watch for:** Let's dive in, let's explore, let's break this down, here's what you need to know, without further ado, heads up, quick note, Honestly?, Look, Here's the thing, The thing is, Real talk, casual versions like "one thing that bit me, so pay attention".

**Problem:** The writer announces the point or stages a moment of candor instead of making the point. Remove the run-up, not just its tone. "Honestly" or "look" inside a casual sentence is ordinary; the tell is the standalone opener before a routine claim.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.
**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

---

### Pattern 34: Arguing with No One [TIER 1]

**Watch for:** This isn't (mainly) about, I'm not saying, To be clear, Don't get me wrong, This is not to say, Some might say... but, A tempting approach would be, One might be tempted to, An obvious approach would be, You might think... but, It would be easy to just.

**Problem:** The text answers an objection or rejects an option that appears nowhere else. Remove the defense; if it holds a real claim, state the claim.

**Before:**
> This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter. You could categorize the problem another way, but the issue is whether the agent can use the instruction when it acts.
**After:**
> The issue is whether the agent can use the instruction when it acts.

---

### Pattern 35: Repeated Sentence Openings [TIER 1]

**Watch for:** Several sentences in a row starting with the same subject, often `she`/`he`/`the team`, because repetition is handled by rule instead of by ear.

**Problem:** Merge the sentences, change the subject, or begin with the action. Do not ban the repeated word; a remaining sentence may still start with "She." Writers also repeat on purpose for rhythm ("She came. She saw. She conquered.").

**Before:**
> She noted the door. She noted the lock on it. She filed both away.
**After:**
> She noted the door and its lock, then filed both away.

---

### Pattern 36: `X and Y` Decorative Headings [TIER 1]

**Watch for:** `Awards and recognition`, `Challenges and Legacy`, `Future Outlook`, `Recognition`, `Awards and Accolades`, and similar X-and-Y heading patterns as standalone sections. Almost ubiquitous in 2025+ AI output.

**Problem:** Section headings in the `X and Y` form appear at the end of articles to gesture at importance. Convert to specific facts, or remove the section.

**Before:**
> ## Awards and Recognition
>
> She has received numerous accolades from industry publications.
**After:**
> In 2023, Fast Company named her to its annual list of innovative founders.


### Pattern 37: GPT-5 Pattern-Heavy Transitions [TIER 2, MODEL-SPECIFIC]

**Watch for:** "However, it's important to consider…", "That said, critics argue…", "It's important to acknowledge that…", "This perspective, while valid…", "Of course, one could argue…", "While [X] may be true, [Y] also deserves consideration."

**Problem:** GPT-5 and successors balance perspectives by default, even when the user did not ask. The result is a counterpoint inserted into every paragraph that follows a formula. State the counterpoint plainly if it is real; cut it if it is filler.

**Before:**
> The migration reduced latency by 40%. However, it's important to consider that some legacy clients were affected.
**After:**
> The migration reduced latency by 40%. A few legacy clients had to update their SDKs to stay compatible.

---

### Pattern 38: Claude Hedging Openers [TIER 2, MODEL-SPECIFIC]

**Watch for:** "I'd be happy to", "I'd like to", "Sure!", "It depends on…", "Of course!" as a sentence-fragment opener, "That depends" without follow-up.

**Problem:** Claude uses sentence-fragment openers that read as warm in conversation but as filler in prose. If the writer's voice does not use them, remove. Keep them when matching a conversational or coaching voice.

**Before:**
> Sure! I can help with that. It depends on what you're trying to do, but here are a few options.
**After:**
> That depends on the use case. Three options to consider:



## Tier 2: MEDIUM Impact Patterns

### Pattern 3: Superficial -ing Analyses [TIER 2]

**Words:** highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, cultivating, fostering, encompassing, showcasing

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

---

### Pattern 5: Vague Attributions [TIER 2]

**Words:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources (when few cited)

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

---

### Pattern 6: Formulaic Challenges Sections [TIER 2]

**Words:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

### Pattern 8: Copula Avoidance [TIER 2]

**Words:** serves as, stands as, marks, represents, boasts, features, offers

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

---

### Pattern 9: Negative Parallelisms [TIER 2]

**Problem:** "Not only...but...", "It's not just...it's..."

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

---

### Pattern 10: Rule of Three Overuse [TIER 2]

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

---

### Pattern 24: Generic Positive Conclusions [TIER 2]

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

---

### Pattern 29: Punctuation Density Too Low [TIER 2]

**Problem:** AI text averages fewer commas, semicolons, and parentheses per word than human text. Sentences average longer, paragraph punctuation density is lower.

**Detection rule:** <1 comma per 25 words = suspect.

**Before:**
> The new policy applies to all employees and contractors and includes provisions for remote work and flexible scheduling and was introduced after extensive consultation with the management board and the union representatives.

**After:**
> The new policy applies to all employees and contractors. It includes provisions for remote work and flexible scheduling, and was introduced after consulting the management board and union representatives.

---

### Pattern 30: Hedging Verb Padding [TIER 2]

**Problem:** LLMs pad ideas with verbs that add no information. Distinct from Pattern 3 (-ing analyses) by grammatical form.

**Words:** ensures, ensuring, highlights (when not adding info), supports, reflects (figurative), facilitates, fosters (figurative)

**Before:**
> The new dashboard ensures that managers can track team performance, highlighting key metrics and ensuring alignment with company goals.

**After:**
> The dashboard shows team performance against the company's stated goals.

---

## Tier 3: LOW Impact Patterns

### Pattern 11: Elegant Variation (Synonym Cycling) [TIER 3]

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

---

### Pattern 12: False Ranges [TIER 3]

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

---

### Pattern 14: Boldface Overuse [TIER 3]

**Before:**
> It blends **OKRs**, **KPIs**, and visual strategy tools such as the **Business Model Canvas** and **Balanced Scorecard**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

---

### Pattern 15: Inline-Header Lists [TIER 3]

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

---

### Pattern 16: Title Case in Headings [TIER 3]

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

---

### Pattern 17: Emojis [TIER 3, MODEL-DEPENDENT]

**Problem:** AI chatbots decorate section headings or bullet points with emoji. Almost always in talk page comments and edit summaries; rarer in 2026 main-article text but still seen.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.


---

### Pattern 19: Collaborative Communication Artifacts [TIER 3]

**Words:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

### Pattern 23: Excessive Hedging [TIER 3]

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

---

## Deprecated Patterns (Do Not Apply)

### Pattern 20: Knowledge-Cutoff Disclaimers [DEPRECATED]
"as of [date]", "Up to my last training update", etc. Obsolete—AI models now have current training data.

---

### Pattern 18: Curly Quotation Marks [TIER 3, MODEL-SPECIFIC]

**Note:** formerly deprecated as a "formatting issue." Re-promoted in 2026 because the pattern is now strongly model-specific. **False positives:** macOS/iOS smart quotes auto-convert straight → curly.

**Before:**
> “The new policy” — said the manager, ‘effective immediately’.

**After:**
> "The new policy," said the manager, "effective immediately."


## Add Soul: Injecting Human Voice

### Signs of Soulless Writing (Even If "Clean")
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

### Procedural Steps
1. **Identify one opinion** the writer might have about the topic. Add it.
2. **Vary sentence rhythm**: After a long sentence, add a short one.
3. **Add specific details**: names, dates, numbers, sensory observations.
4. **Include contradiction**: "It's impressive, but also unsettling."
5. **Use first-person** where it fits: "I keep thinking about..."
6. **Allow imperfection**: tangents, asides, unfinished thoughts.

### Before (Clean but Soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

### After (Has a Pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle - but I keep thinking about those agents working through the night.