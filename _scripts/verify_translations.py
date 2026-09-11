"""Check that each translated chapter preserves the maths of its counterpart.

Prose is expected to differ between _courses/<course>/es/ and .../en/; the LaTeX
must not. For every chapter present in both languages this compares, in order,
the display-math blocks, the inline `$$…$$` spans and the image targets. A
mismatch means a translation edit leaked into a formula.

    python _scripts/verify_translations.py

Exits non-zero if anything is off, so it can gate a commit.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "_courses"

DISPLAY_RE = re.compile(r"^\$\$\n(.*?)^\$\$", re.MULTILINE | re.DOTALL)
INLINE_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)

# Prose set in a LaTeX text-mode box is content, not notation — "si $n$ es par"
# is meant to be translated. Blank the argument out before comparing so the
# check still catches a stray edit to the formula around it.
TEXT_ARG_RE = re.compile(r"\\(?:text|textrm|textit|textbf|mbox)\{[^{}]*\}")

# An operator whose name is spelled out of Spanish words is content too: "mcd"
# is máximo común divisor, and an English reader expects "gcd". Only the pairs
# listed here count as equivalent, so a real notation change — Ker against Im,
# say — still fails the comparison.
TRANSLATED_OPERATORS = {"mcd": "gcd", "MCD": "GCD"}
OPERATOR_RE = re.compile(r"\\operatorname\{([A-Za-z]+)\}")


def body(path: Path) -> str:
    return FRONT_MATTER_RE.sub("", path.read_text(encoding="utf-8"))


def inline_math(text: str) -> list[str]:
    """`$$…$$` spans sitting inside a line (display blocks own whole lines)."""
    return INLINE_RE.findall(DISPLAY_RE.sub("\n", text))


def canonical_operator(match: re.Match) -> str:
    """Collapse a translated operator name onto its Spanish spelling."""
    name = match.group(1)
    for es_name, en_name in TRANSLATED_OPERATORS.items():
        if name in (es_name, en_name):
            return r"\operatorname{<%s>}" % es_name
    return match.group(0)


def normalise(fragment: str) -> str:
    fragment = TEXT_ARG_RE.sub("<text>", fragment)
    return OPERATOR_RE.sub(canonical_operator, fragment)


def compare(name: str, es: list[str], en: list[str], errors: list[str], label: str) -> None:
    if len(es) != len(en):
        errors.append(f"{label}: {name} count differs - es={len(es)} en={len(en)}")
        return
    for i, (a, b) in enumerate(zip(es, en)):
        if normalise(a) != normalise(b):
            errors.append(
                f"{label}: {name} #{i + 1} differs\n"
                f"      es: {a.strip()[:160]}\n"
                f"      en: {b.strip()[:160]}"
            )


def by_number(paths: list[Path]) -> dict[str, Path]:
    """Chapters pair on their leading NN-, not their slug: the English slug is
    itself a translation ('01-sucesiones' <-> '01-sequences')."""
    return {p.name.split("-", 1)[0]: p for p in paths}


def main() -> int:
    errors: list[str] = []
    checked = 0

    for course_dir in sorted(p for p in COURSES.iterdir() if p.is_dir()):
        es_dir, en_dir = course_dir / "es", course_dir / "en"
        if not (es_dir.is_dir() and en_dir.is_dir()):
            continue

        es_by_num = by_number([p for p in sorted(es_dir.glob("*.md")) if p.stem != "index"])
        en_by_num = by_number([p for p in sorted(en_dir.glob("*.md")) if p.stem != "index"])

        missing = sorted(set(es_by_num) - set(en_by_num))
        if missing:
            errors.append(f"{course_dir.name}: no English chapter for {', '.join(missing)}")
        extra = sorted(set(en_by_num) - set(es_by_num))
        if extra:
            errors.append(f"{course_dir.name}: English chapter {', '.join(extra)} has no Spanish source")

        for num in sorted(set(es_by_num) & set(en_by_num)):
            label = f"{course_dir.name}/{num}"
            es_body, en_body = body(es_by_num[num]), body(en_by_num[num])

            for text, lang in ((es_body, "es"), (en_body, "en")):
                if text.count("{% raw %}") != text.count("{% endraw %}"):
                    errors.append(f"{label} ({lang}): unbalanced raw/endraw guard")

            compare("display block", DISPLAY_RE.findall(es_body), DISPLAY_RE.findall(en_body), errors, label)
            compare("inline math", inline_math(es_body), inline_math(en_body), errors, label)
            compare("image", IMAGE_RE.findall(es_body), IMAGE_RE.findall(en_body), errors, label)
            checked += 1

    if errors:
        print(f"FAIL - {len(errors)} problem(s) across {checked} chapter pair(s):\n")
        for e in errors:
            print("  - " + e)
        return 1

    print(f"OK - {checked} chapter pair(s) match on maths, inline spans and images.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
