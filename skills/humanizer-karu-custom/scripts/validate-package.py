#!/usr/bin/env python3
"""
Validate the humanizer-karu-custom skill package.

Checks SKILL.md, PATTERNS.md, and README.md for consistency.

Run: python3 scripts/validate-package.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "SKILL.md"
PATTERNS_MD = ROOT / "PATTERNS.md"
README_MD = ROOT / "README.md"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"ok: {msg}")


def extract_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        fail("SKILL.md missing frontmatter (must start with ---)")
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter not closed with ---")
    fm = parts[1].strip()
    fields: dict[str, str] = {}
    current_key = None
    for line in fm.splitlines():
        if line.startswith(" ") or line.startswith("\t"):
            if current_key:
                fields[current_key] += "\n" + line.strip()
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            current_key = key.strip()
            fields[current_key] = value.strip()
    return fields


def extract_sequential_nums(section_text: str) -> list[int]:
    return [int(m) for m in re.findall(r"^(\d+)\.\s", section_text, re.MULTILINE)]


def assert_sequential(label: str, nums: list[int]) -> None:
    expected = list(range(1, len(nums) + 1))
    if nums != expected:
        fail(f"{label} numbering not sequential: {nums} (expected {expected})")
    ok(f"{label} numbering sequential 1..{len(nums)}")


def extract_section(text: str, header: str, terminator: str) -> str:
    pattern = re.escape(header) + r".*?(?=" + re.escape(terminator) + r")"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return ""
    return match.group(0)


def main() -> None:
    for p in (SKILL_MD, PATTERNS_MD, README_MD):
        if not p.exists():
            fail(f"{p.name} not found at {p}")

    skill_text = SKILL_MD.read_text(encoding="utf-8")
    patterns_text = PATTERNS_MD.read_text(encoding="utf-8")
    readme_text = README_MD.read_text(encoding="utf-8")

    fm = extract_frontmatter(skill_text)
    if "name" not in fm or fm["name"] != "humanizer-karu-custom":
        fail(f"frontmatter name must be 'humanizer-karu-custom', got {fm.get('name')!r}")
    ok("frontmatter name correct")
    if "version" not in fm:
        fail("frontmatter version missing")
    version = fm["version"]
    ok(f"frontmatter version = {version}")

    for label, header, terminator in [
        ("Tier 1", "### Tier 1: HIGH Impact", "\n### Tier "),
        ("Tier 2", "### Tier 2: MEDIUM Impact", "\n### Tier "),
        ("Tier 3", "### Tier 3: LOW Impact", "\n---"),
    ]:
        section = extract_section(skill_text, header, terminator)
        if not section:
            fail(f"{label} section not found in SKILL.md")
        nums = extract_sequential_nums(section)
        if not nums:
            fail(f"{label} section has no numbered items")
        assert_sequential(label, nums)

    install_section = readme_text.split("## Installation", 1)[-1].split("## ", 1)[0]
    if "github.com/blader/humanizer" in install_section:
        fail("README install section still points to blader/humanizer")
    ok("README install section references this repo")

    if version not in readme_text:
        fail(f"version {version} missing from README Version History")
    ok(f"README references version {version}")

    skill_pattern_refs = set(re.findall(r"\[Pattern (\d+)\]", skill_text))
    patterns_defined = set(re.findall(r"### Pattern (\d+):", patterns_text))
    missing = skill_pattern_refs - patterns_defined
    if missing:
        fail(f"SKILL.md references patterns not in PATTERNS.md: {sorted(missing)}")
    ok(f"all {len(skill_pattern_refs)} SKILL.md pattern refs exist in PATTERNS.md")

    for path in (SKILL_MD, PATTERNS_MD):
        text = path.read_text(encoding="utf-8")
        sections = re.findall(r"^## .+$", text, re.MULTILINE)
        if len(sections) < 3:
            fail(f"{path.name}: expected multiple ## sections, found {len(sections)}")
        ok(f"{path.name}: {len(sections)} ## sections")

    skill_lower = skill_text.lower()
    if "code blocks" not in skill_lower or "inline code" not in skill_lower:
        fail("File mode safeguard (preserve code blocks, inline code) missing from SKILL.md")
    ok("file-mode safeguard present in SKILL.md")

    if "do not add a fact" not in skill_lower:
        fail("Fact preservation rule missing from SKILL.md Process section")
    ok("fact preservation rule present in SKILL.md")

    if "Eval 5" not in skill_text or "Fact Preservation" not in skill_text:
        fail("Eval 5 (Fact Preservation) missing from SKILL.md")
    ok("Eval 5 (Fact Preservation) present")

    if "When not to act" not in skill_text:
        fail("When-not-to-act section missing from SKILL.md")
    ok("When-not-to-act section present")

    if "2026 detection context" not in skill_text.lower():
        fail("2026 detection-context note missing from SKILL.md")
    ok("2026 detection-context note present")

    print(f"\nAll checks passed for humanizer-karu-custom v{version}")


if __name__ == "__main__":
    main()