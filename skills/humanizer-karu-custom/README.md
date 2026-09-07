# Humanizer

A Claude Code skill that removes signs of AI-generated writing from text, making it sound more natural and human.

## Installation

### Recommended (clone from this repo)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/calvyntwh/karu-custom-skills.git
cp -r karu-custom-skills/skills/humanizer-karu-custom ~/.claude/skills/humanizer-karu-custom
```

### Manual install/update (only the skill file)

If you already have this repo cloned (or you downloaded `SKILL.md`), copy the skill file into Claude Code's skills directory:

```bash
mkdir -p ~/.claude/skills/humanizer-karu-custom
cp SKILL.md ~/.claude/skills/humanizer-karu-custom/
```

## Usage

In Claude Code, invoke the skill:

```
/humanizer

[paste your text here]
```

Or ask Claude to humanize text directly:

```
Please humanize this text: [your text]
```

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comprehensive guide comes from observations of thousands of instances of AI-generated text.

### Key Insight from Wikipedia

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## 38 Patterns Detected (Tier 1/2/3 with Before/After Examples)

The full pattern catalog is in [PATTERNS.md](PATTERNS.md). Summary:

**Tier 1 — HIGH impact** (16 patterns, address always): AI vocabulary, em dash overuse (model-aware), filler phrases, inflated significance, promotional language, sycophantic tone, vague connection, skipped heading levels, notability/media-coverage parade, misattributed source analysis, Not X but Y, one-line closers, staged run-up, arguing with no one, repeated sentence openings, `X and Y` decorative headings.

**Tier 2 — MEDIUM impact** (10 patterns, address when clearly present): -ing analyses, vague attributions, rule of three, negative parallelism, copula avoidance, generic positive conclusions, punctuation density, hedging verb padding, GPT-5 pattern-heavy transitions, Claude hedging openers.

**Tier 3 — LOW impact** (9 patterns, address selectively): elegant variation, boldface overuse, inline-header lists, title case headings, false ranges, excessive hedging, collaborative artifacts, emojis, curly quotation marks.

See [PATTERNS.md](PATTERNS.md) for full descriptions, before/after examples, and the 2026 model-aware calibration table.

## Full Example

**Before (AI-sounding):**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently. It's not just an update, it's a revolution in how we think about productivity. Industry experts believe this will have a lasting impact on the entire sector, highlighting the company's pivotal role in the evolving technological landscape.

**After (Humanized):**
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Primary source
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - Maintaining organization

## Version History

- **5.1.0** - Added Process section (mark/draft/check/final), three output modes (paste/file/embedded), six new Tier 1 patterns from blader/Wikipedia 2026 (Not X but Y, One-line closers, Staged run-up, Arguing with no one, Repeated sentence openings, `X and Y` headings), GPT-5 transitions and Claude hedging as Tier 2, model-aware em dash calibration, When-not-to-act voice-carrier list, 2026 detection-context note.
- **5.0.1** - Tightened Add Soul step 4: do not invent specifics the source lacks. Added Eval 5 (fact preservation in rewrite).
- **5.0.0** - Model-aware detection across Claude/ChatGPT/Gemini/Grok. Pattern numbering tied to PATTERNS.md.
- **2.1.1** - Fixed pattern #18 example (curly quotes vs straight quotes)
- **2.1.0** - Added before/after examples for all 24 patterns
- **2.0.0** - Complete rewrite based on raw Wikipedia article content
- **1.0.0** - Initial release


## License

MIT
