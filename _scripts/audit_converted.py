r"""Scan converted chapter markdown for LaTeX that failed to make it across.

Complements audit_latex.py, which inspects *rendered* HTML from a running
server. This one reads the markdown, so it can gate a conversion before
anything is committed.

Checks are split by context, because the same string means different things
inside and outside a formula: `\underline{x}` and a `$` inside `\text{…}` are
perfectly ordinary maths, while either one loose in the prose is a bug.

    python _scripts/audit_converted.py [es|en] [course …]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "_courses"

CUSTOM_MACROS = ("R|Z|Q|N|C|F|HH|ind|Rext|Ker|Imm|Aut|End|Hom|Frac|Nil|Rad"
                 "|Spec|mSpec|Char|mcd|MCD|Var|diam")

# Anything left in the prose after conversion.
TEXT_CHECKS = {
    "lone $ delimiter": re.compile(r"\$"),
    r"raw \[ or \]": re.compile(r"\\\[|\\\]"),
    "unexpanded macro": re.compile(r"\\(?:" + CUSTOM_MACROS + r")(?![a-zA-Z])"),
    "leftover environment": re.compile(r"\\(?:begin|end)\{[A-Za-z*]+\}"),
    "text-mode macro": re.compile(
        r"\\(?:emph|textbf|textit|textsc|hlu|underline|noindent|qedhere"
        r"|texorpdfstring|fbox|itshape|hspace|vspace|item|label|ref)"
        r"(?![a-zA-Z])"),
    "accent macro": re.compile(r"\\['`\"~^][A-Za-z]"),
    "internal placeholder": re.compile(r"\x00"),
}

# Anything left inside a formula that MathJax on this site cannot render.
MATH_CHECKS = {
    "unexpanded macro": re.compile(r"\\(?:" + CUSTOM_MACROS + r")(?![a-zA-Z])"),
    "accent macro": re.compile(r"\\['`\"~^][A-Za-z]"),
    "bare align/gather": re.compile(r"\\begin\{(?:align|gather|multline)\*?\}"),
    "prose environment": re.compile(
        r"\\begin\{(?:namedstd|namedres|proof|enumerate|itemize|center"
        r"|tikzpicture|tabular)\}"),
    "internal placeholder": re.compile(r"\x00"),
}

# `$$$$` is an empty maths span: the delimiter pairing has slipped, and every
# `$$` after it opens where it should close. Checked before the split, because
# the split itself is what the slip corrupts.
WHOLE_FILE_CHECKS = {
    "empty maths span ($$$$)": re.compile(r"\$\$\$\$"),
    "tab-indented line": re.compile(r"^\t", re.M),
}

# Spanish left behind in an English chapter. Only words with no English homograph
# are listed, so a hit is a real miss rather than something to eyeball.
SPANISH_WORDS = (
    "sea|sean|entonces|luego|pues|as[ií]|donde|existe|existen|tal que|para todo"
    "|para toda|para todos|si y solo si|demostraci[oó]n|prueba|ejercicio"
    "|ejemplo|teorema|definici[oó]n|lema|corolario|adem[aá]s|tambi[eé]n|cada"
    "|conjunto|sucesi[oó]n|funci[oó]n|medible|cerrado|abierto|acotado|anillo"
    "|cuerpo|cociente|coclase|n[uú]cleo|grupo|subgrupo|ideal(?:es)? primo"
    "|por tanto|de modo que|es decir|note que|observe que|se tiene"
    "|los|las|una|con|que|para|por|del|sobre el|sin embargo"
)
SPANISH_RE = re.compile(r"(?<![\w-])(?:" + SPANISH_WORDS + r")(?![\w-])", re.I)

# Accented characters are a strong signal of untranslated prose, but plenty of
# mathematicians' names legitimately carry one.
ACCENT_WHITELIST = (
    "Arzelà", "Carathéodory", "Hölder", "Möbius", "Poincaré", "Cesàro",
    "Lévy", "Fréchet", "Borel", "Lebesgue", "Kürschák", "Gödel", "Erdős",
    "Šarkovskii", "Radó", "Frobenius", "Möbius",
)
ACCENTED_RE = re.compile(r"[a-zA-Z]*[áéíóúñÁÉÍÓÚÑàèìòùâêîôûäëïöüçÀÈÌÒÙ][a-zA-Z]*")

MATH_SPAN = re.compile(r"\$\$.*?\$\$", re.S)
FRONT_MATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
LIQUID = re.compile(r"\{%\s*(?:end)?raw\s*%\}")


def split_math(body: str) -> tuple[str, list[str]]:
    """Return the prose with formulas blanked out, plus the formulas."""
    maths: list[str] = []

    def take(m: re.Match) -> str:
        maths.append(m.group(0))
        return "\n"

    return MATH_SPAN.sub(take, body), maths


def report(name: str, label: str, hits: list, haystack: str) -> None:
    h = hits[0]
    snippet = haystack[max(0, h.start() - 50): h.start() + 50].replace("\n", " ")
    print("  %-24s %3d   ...%s..." % (label, len(hits), snippet))


def check(lang: str, courses: list[str]) -> int:
    issues = 0
    files = []
    for c in courses:
        files += sorted((COURSES / c / lang).glob("[0-9]*.md"))
    if not files:
        print("no %s chapters found for %s" % (lang, ", ".join(courses)))
        return 1

    for f in files:
        body = FRONT_MATTER.sub("", f.read_text(encoding="utf-8"))
        body = LIQUID.sub("", body)
        found = False

        for label, pat in WHOLE_FILE_CHECKS.items():
            hits = list(pat.finditer(body))
            if hits:
                if not found:
                    print(f.name)
                    found = True
                issues += len(hits)
                report(f.name, "file: " + label, hits, body)

        prose, maths = split_math(body)

        for label, pat in TEXT_CHECKS.items():
            hits = list(pat.finditer(prose))
            if hits:
                if not found:
                    print(f.name)
                    found = True
                issues += len(hits)
                report(f.name, "prose: " + label, hits, prose)

        # An English chapter is a translation, so anything Spanish is a miss.
        # Link and image targets are exempt: an asset keeps the filename it was
        # shipped with, whatever language that name is in.
        if lang == "en":
            prose = re.sub(r"\]\([^)]*\)", "]()", prose)
            hits = list(SPANISH_RE.finditer(prose))
            if hits:
                if not found:
                    print(f.name)
                    found = True
                issues += len(hits)
                words = sorted({h.group(0).lower() for h in hits})
                report(f.name, "prose: untranslated Spanish", hits, prose)
                print("  %-24s     words: %s" % ("", ", ".join(words[:12])))

            accented = [m for m in ACCENTED_RE.finditer(prose)
                        if m.group(0) not in ACCENT_WHITELIST]
            if accented:
                if not found:
                    print(f.name)
                    found = True
                issues += len(accented)
                words = sorted({m.group(0) for m in accented})
                report(f.name, "prose: accented word", accented, prose)
                print("  %-24s     words: %s" % ("", ", ".join(words[:12])))

        joined = "\n".join(maths)
        for label, pat in MATH_CHECKS.items():
            hits = list(pat.finditer(joined))
            if hits:
                if not found:
                    print(f.name)
                    found = True
                issues += len(hits)
                report(f.name, "math: " + label, hits, joined)

        if body.count("$$") % 2:
            if not found:
                print(f.name)
            issues += 1
            print("  %-24s odd number of $$ delimiters" % "unbalanced")

    print("\n%d chapter(s) scanned, %d issue(s)." % (len(files), issues))
    return 1 if issues else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    lang = args[0] if args else "es"
    courses = args[1:] or ["ma0505", "ma0561"]
    sys.exit(check(lang, courses))
