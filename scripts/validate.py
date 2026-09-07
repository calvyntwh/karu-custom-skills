#!/usr/bin/env python3
"""
Validate all skills in the karu-custom-skills monorepo.

Checks each skills/<name>/SKILL.md for the karu fingerprint:
- Valid YAML frontmatter with name matching the directory
- Frontmatter has description
- Frontmatter has version (top-level OR metadata.version)
- Has ## When to Use section
- Has ## When NOT to Use section
- Has ## Self-Improvement Protocol section
- Has at least 3 ## Evaluations / ### Eval subsections
- If references/ exists, has ## Resources section linking to it

Also runs the humanizer-specific checks (skills/humanizer-karu-custom/scripts/validate-package.py)
as a delegate.

Run: python3 scripts/validate.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"ok: {msg}")


def extract_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
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


def find_section(text: str, header: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(header)}\s*$", text, re.MULTILINE))


def count_evals(text: str) -> int:
    return len(re.findall(r"^###\s+Eval\b", text, re.MULTILINE))


def has_resources_link(text: str) -> bool:
    return "## Resources" in text


def references_dir_exists(skill_dir: Path) -> bool:
    return (skill_dir / "references").is_dir()


def check_skill(skill_dir: Path) -> list[str]:
    """Return list of errors for this skill. Empty list = pass."""
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]
    text = skill_md.read_text(encoding="utf-8")
    fm = extract_frontmatter(text)

    name = skill_dir.name
    if "name" not in fm:
        errors.append("frontmatter missing 'name'")
    elif fm["name"] != name:
        errors.append(f"frontmatter name {fm['name']!r} != dir name {name!r}")

    if "description" not in fm:
        errors.append("frontmatter missing 'description'")

    has_top_version = "version" in fm
    has_meta_version = "metadata" in fm and "version" in fm["metadata"]
    if not (has_top_version or has_meta_version):
        errors.append("frontmatter missing version (top-level or metadata.version)")

    if not find_section(text, "When to Use"):
        errors.append("missing ## When to Use section")
    if not find_section(text, "When NOT to Use"):
        errors.append("missing ## When NOT to Use section")
    if not find_section(text, "Self-Improvement Protocol"):
        errors.append("missing ## Self-Improvement Protocol section")

    eval_count = count_evals(text)
    if eval_count < 3:
        errors.append(f"only {eval_count} ### Eval subsections (need >= 3)")

    if references_dir_exists(skill_dir) and not has_resources_link(text):
        errors.append("references/ exists but ## Resources section missing")

    return errors


def main() -> None:
    if not SKILLS_DIR.is_dir():
        fail(f"skills/ directory not found at {SKILLS_DIR}")

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        fail("no skills found")

    total_errors = 0
    for skill_dir in skill_dirs:
        errors = check_skill(skill_dir)
        if errors:
            total_errors += len(errors)
            print(f"FAIL {skill_dir.name}:")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"ok   {skill_dir.name}")

    if total_errors:
        fail(f"{total_errors} error(s) across {len(skill_dirs)} skills")

    print(f"\nAll {len(skill_dirs)} skills pass karu fingerprint checks.")

    humanizer_validator = ROOT / "skills" / "humanizer-karu-custom" / "scripts" / "validate-package.py"
    if humanizer_validator.exists():
        print("\nDelegating to humanizer-specific validator...")
        result = subprocess.run(
            [sys.executable, str(humanizer_validator)],
            cwd=ROOT / "skills" / "humanizer-karu-custom",
            check=False,
        )
        if result.returncode != 0:
            sys.exit(result.returncode)


if __name__ == "__main__":
    main()