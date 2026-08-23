# Gates: ponytail-shrink pass for humanizer v5.0

OWNS: skills/humanizer-karu-custom/**

- [x] G1: PATTERNS.md has zero inline per-pattern Model caveat blocks
  CHECK: sh -c 'grep -c "^\*\*Model caveat" skills/humanizer-karu-custom/PATTERNS.md || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G2: Model Era Note table trimmed to non-uniform rows only
  CHECK: sh -c 'grep -c "^| Vague connection\|^| Notability parade\|^| Misattribution" skills/humanizer-karu-custom/PATTERNS.md || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G3: PATTERNS.md P25 Words list removed
  CHECK: sh -c 'awk "/^### Pattern 25/,/^---/" skills/humanizer-karu-custom/PATTERNS.md | grep -c "^\*\*Words:\*\*" || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G4: PATTERNS.md P26 detection rule removed
  CHECK: sh -c 'awk "/^### Pattern 26/,/^---/" skills/humanizer-karu-custom/PATTERNS.md | grep -c "Detection rule" || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G5: PATTERNS.md P29 detection rule trimmed (3 thresholds → 1)
  CHECK: sh -c 'awk "/^### Pattern 29/,/^---/" skills/humanizer-karu-custom/PATTERNS.md | grep -c "Average sentence length\|0 semicolons" || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G6: PATTERNS.md P17 inline caveat removed
  CHECK: sh -c 'grep -c "rarely produces emoji" skills/humanizer-karu-custom/PATTERNS.md || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G7: PATTERNS.md P18 inline caveat removed
  CHECK: sh -c 'grep -c "curly quotes by default" skills/humanizer-karu-custom/PATTERNS.md || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G8: SKILL.md Tier 1 Em Dash parenthetical shortened
  CHECK: sh -c 'grep -c "Claude-only HIGH" skills/humanizer-karu-custom/SKILL.md || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G9: SKILL.md tier numbering per-tier starting at 1 (max number = 10)
  CHECK: sh -c 'awk "/^### Tier [123]/,/^---/" skills/humanizer-karu-custom/SKILL.md | grep -oE "^[0-9]+\." | tr -d "." | sort -n | tail -1'
  EXPECT: 10
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=10

- [x] G10: SKILL.md Tier 3 Emojis parenthetical shortened
  CHECK: sh -c 'grep -c "ChatGPT/Grok: higher signal" skills/humanizer-karu-custom/SKILL.md || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G11: SKILL.md Eval 4 block is 6 lines
  CHECK: sh -c 'awk "/^### Eval 4/,/^### 5.0.0/" skills/humanizer-karu-custom/SKILL.md | wc -l'
  EXPECT: 6
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=6

- [x] G12: SKILL.md 5.0.0 changelog trimmed to 4 bullets
  CHECK: sh -c 'awk "/^### 5.0.0/,/^### 4.1.0/" skills/humanizer-karu-custom/SKILL.md | grep -c "^- "'
  EXPECT: 4
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=4

- [x] G13: SKILL.md description field shortened (no per-pattern enumeration)
  CHECK: sh -c 'sed -n "/^description:/,/^allowed-tools:/p" skills/humanizer-karu-custom/SKILL.md | grep -c "vague connection\|notability parade\|hedging verb" || true'
  EXPECT: 0
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=0

- [x] G14: Net line change vs base commit ff306db is negative
  CHECK: sh -c 'git diff ff306db..HEAD --numstat -- skills/humanizer-karu-custom/ | awk "{a+=\$1; r+=\$2} END{if (r>a) print \"NEGATIVE\"; else print \"POSITIVE\"}"'
  EXPECT: NEGATIVE
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=NEGATIVE

- [x] G15: Installed skill synced from worktree
  CHECK: sh -c 'diff -q /Users/calvyn/.agents/skills/humanizer-karu-custom/SKILL.md skills/humanizer-karu-custom/SKILL.md && diff -q /Users/calvyn/.agents/skills/humanizer-karu-custom/PATTERNS.md skills/humanizer-karu-custom/PATTERNS.md && echo SYNCED'
  EXPECT: SYNCED
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=SYNCED

- [x] G16: Branch pushed with shrink commit d81cc0d
  CHECK: sh -c 'git log origin/humanizer-v5-model-aware --oneline -1'
  EXPECT: d81cc0d
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=d81cc0d refactor(humanizer): ponytail-shrink pass for v5.0

- [x] G17: No regression — version still 5.0.0, all 29 patterns present
  CHECK: sh -c 'echo "$(grep -c "^version: 5.0.0" skills/humanizer-karu-custom/SKILL.md) $(grep -c "^### Pattern " skills/humanizer-karu-custom/PATTERNS.md)"'
  EXPECT: 1 29
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/calvyn/Repo/github.com/worktrees/humanizer-v5; path=35188aaf8cd4/25 entries; output=1 29