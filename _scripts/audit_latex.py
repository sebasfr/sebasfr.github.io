"""Audit rendered chapter HTML for LaTeX corruption symptoms.

Reports per-chapter counts of:
  - HTML-escaped ampersands inside math (\(...\) or \[...\])
  - HTML-escaped < or > inside math
  - bare \begin{align} blocks (need to be \begin{aligned} inside math delimiters)
  - aligned blocks rendered as inline (\(\begin{aligned}...\)) instead of display
  - markdown intrusions: <em>, <strong> inside math spans
  - empty math (\(\) or \[\])
"""

from __future__ import annotations

import re
from urllib.request import urlopen

BASE = "http://localhost:8080/notes"
CHAPTERS = {
    "ma0350": [
        "01-sucesiones",
        "02-subsucesiones",
        "03-limite-superior-e-inferior",
        "04-series-numericas",
        "05-criterios-de-convergencia-de-series",
        "06-integral-de-riemann",
        "07-tecnicas-de-integracion",
        "08-aplicaciones-de-la-integral-de-riemann",
        "09-integrales-impropias",
        "10-series-de-funciones",
        "11-convergencia-de-funciones",
        "12-topicos-importantes-y-ejemplos",
    ],
    "ma0450": [
        "01-topologia-en-rn",
        "02-funciones-de-varias-variables",
        "03-diferenciacion",
        "04-integracion-en-rn",
        "05-calculo-vectorial",
    ],
}

# Math span: \( … \) or \[ … \] (non-greedy across newlines)
INLINE_MATH = re.compile(r"\\\((.*?)\\\)", re.DOTALL)
DISPLAY_MATH = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)


def audit(url: str) -> dict[str, int | list[str]]:
    with urlopen(url) as resp:
        body = resp.read().decode("utf-8", errors="replace")

    # Strip everything before <body> and after </body>
    m = re.search(r"<body.*?</body>", body, re.DOTALL)
    if m:
        body = m.group(0)

    inline_matches = INLINE_MATH.findall(body)
    display_matches = DISPLAY_MATH.findall(body)
    all_math = inline_matches + display_matches

    escaped_amp = sum(c.count("&amp;") for c in all_math)
    escaped_lt = sum(c.count("&lt;") for c in all_math)
    escaped_gt = sum(c.count("&gt;") for c in all_math)
    escaped_quot = sum(c.count("&quot;") for c in all_math)
    inline_with_aligned = sum(1 for c in inline_matches if "\\begin{aligned}" in c)
    bare_align_blocks = len(re.findall(r"\\begin\{align\}", body)) - len(
        re.findall(r"\\begin\{aligned\}", body)
    )
    em_in_math = sum(c.count("<em>") for c in all_math)
    strong_in_math = sum(c.count("<strong>") for c in all_math)
    empty_math = sum(1 for c in all_math if not c.strip())

    # Sample a corrupted snippet
    sample = ""
    for c in all_math:
        if "&amp;" in c or "<em>" in c:
            sample = c[:200]
            break

    return {
        "math_blocks": len(all_math),
        "inline_aligned_misrender": inline_with_aligned,
        "escaped_&": escaped_amp,
        "escaped_<": escaped_lt,
        "escaped_>": escaped_gt,
        "escaped_quot": escaped_quot,
        "bare_align": bare_align_blocks,
        "em_in_math": em_in_math,
        "strong_in_math": strong_in_math,
        "empty_math": empty_math,
        "sample": sample,
    }


def main() -> None:
    issues = 0
    for course, chapters in CHAPTERS.items():
        for chap in chapters:
            url = f"{BASE}/{course}/{chap}/"
            try:
                r = audit(url)
            except Exception as e:
                print(f"[ERR] {course}/{chap}: {e}")
                continue
            problems = []
            for k, v in r.items():
                if k in ("math_blocks", "sample"):
                    continue
                if v:
                    problems.append(f"{k}={v}")
            if problems:
                issues += 1
                print(f"{course}/{chap}: {' '.join(problems)}")
                if r["sample"]:
                    s = r["sample"].replace("\n", " | ")
                    print(f"  sample: {s}")
    if not issues:
        print("All chapters clean.")


if __name__ == "__main__":
    main()
