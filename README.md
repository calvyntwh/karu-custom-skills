# karu-custom/skills

A collection of **self-improving** AI agent skills for KiloCode CLI, Claude Code, and other Agent Skills-compatible agents. Each skill learns from corrections and improves over time.

## Why Self-Improving Skills?

Most AI agent skills are static prompts that don't improve. These skills:
- **Log corrections** after each use
- **Track emerging patterns** across sessions
- **Promote validated learnings** to persistent knowledge
- **Reduce repeated mistakes** automatically

## Skills (10 total)

### Writing & Text

| Skill | Description | Grade |
|-------|-------------|-------|
| **[humanizer-karu-custom](skills/humanizer-karu-custom)** | Remove AI patterns and add human voice. 24 pattern categories, tested with 92% accuracy. | A |

### Reasoning & Analysis

| Skill | Description | Grade |
|-------|-------------|-------|
| **[chestertons-fence](skills/chestertons-fence)** | Don't delete code until you understand why it was written. | A |
| **[decision-matrix](skills/decision-matrix)** | Weighted trade-off analysis to eliminate recommendation bias. | A |
| **[first-principles-thinking](skills/first-principles-thinking)** | Break problems to basic truths for innovative solutions. | A |
| **[inversion-thinking](skills/inversion-thinking)** | Proactive failure analysis using the Saboteur Method. | A |
| **[map-vs-territory](skills/map-vs-territory)** | Trust runtime truth over documentation. | A |
| **[occams-razor](skills/occams-razor)** | Complexity pruning and simplification. | A |
| **[pareto-principle](skills/pareto-principle)** | 80/20 rule for strategic prioritization. | B+ |
| **[rubber-ducking](skills/rubber-ducking)** | Verbalize code to catch semantic errors before running. | A |
| **[systems-thinking](skills/systems-thinking)** | Feedback loop analysis for architecture decisions. | A |

## Evaluation Results

All 10 skills tested with real scenarios:

| Grade | Count | Skills |
|-------|-------|--------|
| **A** | 9 | chestertons-fence, decision-matrix, first-principles, inversion, map-vs-territory, occams-razor, rubber-ducking, systems-thinking, humanizer |
| **B+** | 1 | pareto-principle |

## Installation

### Clone All Skills

```bash
git clone https://github.com/calvyntwh/karu-custom-skills.git ~/.agents/skills
```

### Clone Individual Skills

```bash
git clone https://github.com/calvyntwh/karu-custom-skills.git
cp -r skills/humanizer-karu-custom ~/.agents/skills/
```

## Usage

Explicit invocation (recommended):
```
Use the humanizer-karu-custom skill to fix this text
Use the decision-matrix skill to compare React vs Vue
Use the chestertons-fence skill before deleting this code
Use the inversion-thinking skill to analyze security vulnerabilities
```

## How Self-Improvement Works

Each skill has a `.learnings/` directory:

```
skill/
├── SKILL.md
└── .learnings/
    ├── CORRECTIONS.md   # Individual corrections
    ├── PATTERNS.md     # Emerging patterns
    ├── LEARNINGS.md    # Validated patterns (promoted)
    └── REVIEW.md       # Review queue
```

After using a skill, if you corrected something or discovered a new pattern, check `.learnings/` to log and improve future performance.

## Credits

- **[blader/humanizer](https://github.com/blader/humanizer)** - Original humanizer skill
- **[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing)** - Pattern reference
- **[Anthropic Skills](https://github.com/anthropics/skills)** - Agent Skills specification
- **[OpenClaw self-improving-agent](https://github.com/openclaw/skills)** - Self-improvement inspiration

## License

MIT License

Copyright (c) 2024 blader (humanizer original)
Copyright (c) 2026 calvyntwh