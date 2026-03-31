# karu-custom/skills

A collection of self-improving AI agent skills for KiloCode CLI, Claude Code, and other Agent Skills-compatible agents. Each skill includes a self-improvement system that logs corrections and learns from feedback.

## Features

- **Self-Improving**: Skills log corrections and learn from feedback over time
- **Cross-Platform**: Works with KiloCode CLI, Claude Code, and other compatible agents
- **Reasoning-Focused**: Mental models and systematic thinking approaches

## Skills

### Writing

| Skill | Description |
|-------|-------------|
| **[humanizer-karu-custom](skills/humanizer-karu-custom)** | Remove AI patterns from text and add human voice. Based on Wikipedia's "Signs of AI writing" guide. |

### Reasoning & Analysis

| Skill | Description |
|-------|-------------|
| **[chestertons-fence](skills/chestertons-fence)** | Safety protocol: don't delete code until you understand why it was written. |
| **[decision-matrix](skills/decision-matrix)** | Weighted trade-off analysis for making better decisions. |
| **[first-principles-thinking](skills/first-principles-thinking)** | Break problems to basic truths for innovative solutions. |
| **[inversion-thinking](skills/inversion-thinking)** | Proactive failure analysis using the Saboteur Method. |
| **[map-vs-territory](skills/map-vs-territory)** | Trust runtime truth over documentation. |
| **[occams-razor](skills/occams-razor)** | Complexity pruning using the Subtraction Method. |
| **[pareto-principle](skills/pareto-principle)** | 80/20 rule for strategic prioritization. |
| **[rubber-ducking](skills/rubber-ducking)** | Verbalize code to catch semantic errors. |
| **[systems-thinking](skills/systems-thinking)** | Feedback loop analysis for architecture decisions. |

## Installation

```bash
# Clone all skills
git clone https://github.com/calvyntwh/karu-custom-skills.git ~/.agents/skills

# Or install individual skills
git clone https://github.com/calvyntwh/karu-custom-skills.git
cp -r skills/humanizer-karu-custom ~/.agents/skills/
```

## Usage

```bash
# Writing tasks
Use the humanizer-karu-custom skill to fix this text

# Decision making  
Use the decision-matrix skill to compare React vs Vue

# Code safety
Use the chestertons-fence skill before deleting code
```

## How Self-Improvement Works

Each skill includes a `.learnings/` directory:

```
skill/
├── SKILL.md
└── .learnings/
    ├── CORRECTIONS.md   # Log corrections
    ├── PATTERNS.md     # Track patterns
    ├── LEARNINGS.md    # Validated learnings
    └── REVIEW.md       # Review queue
```

## Credits

- **[blader/humanizer](https://github.com/blader/humanizer)** - Original humanizer skill
- **[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing)** - Pattern reference
- **[Anthropic Skills](https://github.com/anthropics/skills)** - Agent Skills specification

## License

MIT License

Copyright (c) 2024 blader (humanizer original)  
Copyright (c) 2026 calvyntwh