# karu-custom/skills

A collection of self-improving AI agent skills for KiloCode CLI, Claude Code, and any Agent Skills-compatible agent.

## Features

- **Self-Improving**: Skills log corrections and learn from feedback
- **Tested**: Real-world evaluation with measurable results
- **Cross-Platform**: Works with KiloCode CLI, Claude Code, and more

## Skills

### Writing & Text

| Skill | Description |
|-------|-------------|
| **[humanizer-karu-custom](/calvyntwh/karu-custom-skills/tree/main/skills/humanizer-karu-custom)** | Remove AI patterns and add human voice. 24 pattern categories, self-improving. |

### Reasoning & Analysis

| Skill | Description |
|-------|-------------|
| **[chestertons-fence](/calvyntwh/karu-custom-skills/tree/main/skills/chestertons-fence)** | Don't delete code until you understand why it was written. |
| **[decision-matrix](/calvyntwh/karu-custom-skills/tree/main/skills/decision-matrix)** | Weighted trade-off analysis to eliminate recommendation bias. |
| **[first-principles-thinking](/calvyntwh/karu-custom-skills/tree/main/skills/first-principles-thinking)** | Break problems to basic truths for innovative solutions. |
| **[inversion-thinking](/calvyntwh/karu-custom-skills/tree/main/skills/inversion-thinking)** | Proactive failure analysis using the Saboteur Method. |
| **[map-vs-territory](/calvyntwh/karu-custom-skills/tree/main/skills/map-vs-territory)** | Trust runtime truth over documentation. |
| **[occams-razor](/calvyntwh/karu-custom-skills/tree/main/skills/occams-razor)** | Complexity pruning and simplification. |
| **[pareto-principle](/calvyntwh/karu-custom-skills/tree/main/skills/pareto-principle)** | 80/20 rule for strategic prioritization. |
| **[rubber-ducking](/calvyntwh/karu-custom-skills/tree/main/skills/rubber-ducking)** | Verbalize code to catch semantic errors. |
| **[systems-thinking](/calvyntwh/karu-custom-skills/tree/main/skills/systems-thinking)** | Feedback loop analysis for architecture decisions. |

### Meta & Tools

| Skill | Description |
|-------|-------------|
| **[skill-creator](/calvyntwh/karu-custom-skills/tree/main/skills/skill-creator)** | Create new skills with best practices. |
| **[find-skills](/calvyntwh/karu-custom-skills/tree/main/skills/find-skills)** | Discover and install community skills. |

### Terminal & Navigation

| Skill | Description |
|-------|-------------|
| **[cmux](/calvyntwh/karu-custom-skills/tree/main/skills/cmux)** | Terminal multiplexer control. |
| **[cmux-browser](/calvyntwh/karu-custom-skills/tree/main/skills/cmux-browser)** | Browser automation with cmux. |
| **[cmux-debug-windows](/calvyntwh/karu-custom-skills/tree/main/skills/cmux-debug-windows)** | Debug window management. |
| **[cmux-markdown](/calvyntwh/karu-custom-skills/tree/main/skills/cmux-markdown)** | Open markdown in formatted viewer. |

## Installation

### For KiloCode CLI

```bash
git clone https://github.com/calvyntwh/karu-custom-skills.git ~/.agents/skills
```

### For Claude Code

```bash
git clone https://github.com/calvyntwh/karu-custom-skills.git ~/.claude/skills
```

### Individual Skills

```bash
# Clone just one skill
git clone https://github.com/calvyntwh/karu-custom-skills.git
cp -r skills/humanizer-karu-custom ~/.agents/skills/
```

## Usage

Explicit invocation (recommended):
```
Use the humanizer-karu-custom skill to fix this text
Use the decision-matrix skill to compare React vs Vue
Use the chestertons-fence skill before deleting this code
```

## Self-Improvement

Skills marked with 🌱 include self-improvement systems. After using a skill, if you corrected something:
- Check `.learnings/CORRECTIONS.md` for logged corrections
- Check `.learnings/PATTERNS.md` for emerging patterns

## Credits

- [blader/humanizer](https://github.com/blader/humanizer) - Original humanizer
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Signs_of_AI_writing) - Pattern reference
- [Anthropic Skills](https://github.com/anthropics/skills) - Agent Skills spec

## License

MIT License - see individual skill folders for details.

Copyright (c) 2024 blader (humanizer original)
Copyright (c) 2026 calvyntwh