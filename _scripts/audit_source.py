"""Audit Obsidian source markdown for likely LaTeX typos that the converter
can't fix. Reports per-file:
  - empty math `$$` or `$ $`
  - lines with odd number of unescaped `$` (probably mismatched)
  - `\begin{align}` (without 'ed') inside math context
  - `$, $` patterns (text-like content forced into math)
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EMPTY_MATH = re.compile(r"\$\$\s*\$\$|\$\s*\$")
SUSPECT_DOLLAR_TEXT = re.compile(r"\$[\s,;.:]+\$")
BEGIN_ALIGN = re.compile(r"\\begin\{align\}")


def count_unescaped_dollars(line: str) -> int:
    return len(re.findall(r"(?<!\\)\$", line))


def audit(path: Path) -> list[str]:
    issues: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_block = False
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped == "$$":
            in_block = not in_block
            continue
        if EMPTY_MATH.search(line):
            issues.append(f"  L{i}: empty math: {line.strip()[:120]}")
        if SUSPECT_DOLLAR_TEXT.search(line):
            issues.append(f"  L{i}: suspect $...$ with only punct/space: {line.strip()[:120]}")
        if BEGIN_ALIGN.search(line) and not re.search(r"\\begin\{aligned\}", line):
            issues.append(f"  L{i}: \\begin{{align}} (use \\begin{{aligned}}): {line.strip()[:120]}")
        if not in_block:
            n = count_unescaped_dollars(line)
            if n % 2:
                # Skip lines that are all-text with one stray $ in URLs etc.
                # but flag real LaTeX-looking lines.
                if "$" in line and re.search(r"\$\\?[a-zA-Z\\{(]", line):
                    issues.append(
                        f"  L{i}: odd $-count ({n}): {line.strip()[:120]}"
                    )
    return issues


def main() -> None:
    folders = [ROOT / "_posts" / "MA0350", ROOT / "_posts" / "MA0450"]
    total = 0
    for folder in folders:
        for md in sorted(folder.glob("*.md")):
            issues = audit(md)
            if issues:
                rel = md.relative_to(ROOT)
                print(f"{rel}:")
                for line in issues:
                    print(line)
                total += len(issues)
    print(f"\nTotal issues: {total}")


if __name__ == "__main__":
    main()
