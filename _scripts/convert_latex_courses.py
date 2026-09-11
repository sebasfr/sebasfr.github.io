r"""Convert the MA0505 / MA0561 LaTeX note sets into the _courses collection.

Companion to convert_obsidian_courses.py, which did the same job for MA0350 and
MA0450 from Obsidian markdown. Here the source is LaTeX: five documents written
for exam revision, each a flat run of `namedstd` / `namedres` result boxes with
`proof` environments between them.

Reads  _courses/ma0505/*.tex and _courses/ma0561/*.tex
Writes _courses/<course>/es/NN-slug.md

Only body `\section`s are converted; every `\appendix` section is dropped. The
chapter map below decides how source sections and subsections group into pages:
MA0505 splits by `\section`, MA0561's ring half does too, but its group half
splits by `\subsection` because those three sections run 30k-40k characters.

The maths is moved across verbatim -- macros are expanded (`\R` -> `\mathbb{R}`)
because MathJax on the site has no macro definitions, but nothing else inside a
formula is touched. _scripts/verify_translations.py later checks that the English
translations preserve these formulas exactly.

    python _scripts/convert_latex_courses.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "_courses"

# -----------------------------------------------------------------------------
# Chapter map
# -----------------------------------------------------------------------------
# Each entry: (chapter_number, es_title, [(section_index, [subsection_indices])])
# A subsection list of None means "the whole section, subsections and all".
# Indices are 1-based and count only body sections, in document order.

MA0505_I = "ma0505/Analisis_I_ExamenI.tex"
MA0505_II = "ma0505/Analisis_I_ExamenII.tex"
MA0505_III = "ma0505/Analisis_I_ExamenIII.tex"
MA0561_G = "ma0561/Grupos_Examenes_I_II.tex"
MA0561_R = "ma0561/Grupos_ExamenIII.tex"

CHAPTERS: dict[str, list[dict]] = {
    "ma0505": [
        {"n": 1, "src": MA0505_I, "sec": 1, "subs": None,
         "en": "Review: Norms on Rd and Connectedness"},
        {"n": 2, "src": MA0505_I, "sec": 2, "subs": None,
         "en": "Metric Spaces"},
        {"n": 3, "src": MA0505_I, "sec": 3, "subs": None,
         "en": "Basic Topological Properties"},
        {"n": 4, "src": MA0505_I, "sec": 4, "subs": None,
         "en": "Continuity"},
        {"n": 5, "src": MA0505_I, "sec": 5, "subs": None,
         "en": "Compactness"},
        {"n": 6, "src": MA0505_I, "sec": 6, "subs": None,
         "en": "Completeness"},
        {"n": 7, "src": MA0505_I, "sec": 7, "subs": None,
         "en": "The Arzelà–Ascoli Theorem"},
        {"n": 8, "src": MA0505_I, "sec": 8, "subs": None,
         "en": "Connectedness"},
        {"n": 9, "src": MA0505_I, "sec": 9, "subs": None,
         "en": "Baire Categories"},
        {"n": 10, "src": MA0505_II, "sec": 1, "subs": None,
         "en": "Functions of Bounded Variation"},
        {"n": 11, "src": MA0505_II, "sec": 2, "subs": None,
         "en": "The Riemann–Stieltjes Integral"},
        {"n": 12, "src": MA0505_II, "sec": 3, "subs": None,
         "en": "Outer Measure"},
        {"n": 13, "src": MA0505_II, "sec": 4, "subs": None,
         "en": "Lebesgue Measure"},
        {"n": 14, "src": MA0505_II, "sec": 5, "subs": None,
         "en": "Measurable Functions"},
        {"n": 15, "src": MA0505_III, "sec": 1, "subs": None,
         "en": "The Egorov and Lusin Theorems"},
        {"n": 16, "src": MA0505_III, "sec": 2, "subs": None,
         "en": "Convergence in Measure"},
        {"n": 17, "src": MA0505_III, "sec": 3, "subs": None,
         "en": "The Lebesgue Integral of Non-negative Functions"},
        {"n": 18, "src": MA0505_III, "sec": 4, "subs": None,
         "en": "Properties of the Integral of Non-negative Functions"},
        {"n": 19, "src": MA0505_III, "sec": 5, "subs": None,
         "en": "The Lebesgue Integral of Measurable Functions"},
        {"n": 20, "src": MA0505_III, "sec": 6, "subs": None,
         "en": "The Relationship Between the Riemann and Lebesgue Integrals"},
    ],
    "ma0561": [
        # Group half: split by subsection. 1.1-1.5 merge, 1.6-1.7 merge, and the
        # 947-character 1.9 (Centro y centralizador) folds into the first page.
        {"n": 1, "src": MA0561_G, "sec": 1, "subs": [1, 2, 3, 4, 5, 9],
         "title": "Grupos, subgrupos y centralizadores",
         "en": "Groups, Subgroups and Centralizers"},
        {"n": 2, "src": MA0561_G, "sec": 1, "subs": [6, 7],
         "title": "Grupos cíclicos y sus subgrupos",
         "en": "Cyclic Groups and Their Subgroups"},
        {"n": 3, "src": MA0561_G, "sec": 1, "subs": [8],
         "title": "Grupo de permutaciones", "en": "The Permutation Group"},
        {"n": 4, "src": MA0561_G, "sec": 2, "subs": [1],
         "title": "Homomorfismos de grupos", "en": "Group Homomorphisms"},
        {"n": 5, "src": MA0561_G, "sec": 2, "subs": [2],
         "title": "Cadenas y sucesiones exactas",
         "en": "Chain Complexes and Exact Sequences"},
        {"n": 6, "src": MA0561_G, "sec": 2, "subs": [3],
         "title": "Traslación y conjugación", "en": "Translation and Conjugation"},
        {"n": 7, "src": MA0561_G, "sec": 2, "subs": [4], "title": "Coclases",
         "en": "Cosets"},
        {"n": 8, "src": MA0561_G, "sec": 2, "subs": [5],
         "title": "Subgrupos normales", "en": "Normal Subgroups"},
        {"n": 9, "src": MA0561_G, "sec": 2, "subs": [6], "title": "Grupo cociente",
         "en": "The Quotient Group"},
        {"n": 10, "src": MA0561_G, "sec": 2, "subs": [7],
         "title": "Teoremas del isomorfismo", "en": "The Isomorphism Theorems"},
        {"n": 11, "src": MA0561_G, "sec": 3, "subs": [1],
         "title": "Acciones de grupo", "en": "Group Actions"},
        {"n": 12, "src": MA0561_G, "sec": 3, "subs": [2],
         "title": "Órbitas y estabilizadores", "en": "Orbits and Stabilizers"},
        {"n": 13, "src": MA0561_G, "sec": 3, "subs": [3], "title": "Grupos simples",
         "en": "Simple Groups"},
        {"n": 14, "src": MA0561_G, "sec": 3, "subs": [4],
         "title": "Teoremas de Sylow", "en": "The Sylow Theorems"},
        # Ring half: split by section, as written.
        {"n": 15, "src": MA0561_R, "sec": 1, "subs": None, "en": "Rings"},
        {"n": 16, "src": MA0561_R, "sec": 2, "subs": None,
         "en": "The Polynomial Ring"},
        {"n": 17, "src": MA0561_R, "sec": 3, "subs": None, "en": "Ideals"},
        {"n": 18, "src": MA0561_R, "sec": 4, "subs": None, "en": "Prime Ideals"},
        {"n": 19, "src": MA0561_R, "sec": 5, "subs": None,
         "en": "Products of Rings"},
        {"n": 20, "src": MA0561_R, "sec": 6, "subs": None, "en": "Quotient Rings"},
        {"n": 21, "src": MA0561_R, "sec": 7, "subs": None,
         "en": "Ring Homomorphisms"},
        {"n": 22, "src": MA0561_R, "sec": 8, "subs": None,
         "en": "Prime Subrings and Characteristic"},
        {"n": 23, "src": MA0561_R, "sec": 9, "subs": None,
         "en": "The Field of Fractions"},
        {"n": 24, "src": MA0561_R, "sec": 10, "subs": None,
         "en": "Factorization of Homomorphisms"},
    ],
}

# TikZ pictures, in document order per source file, mapped to the SVG that
# replaces them. Anything not listed here is dropped with a warning.
FIGURES: dict[str, list[tuple[str, str]]] = {
    MA0505_II: [
        ("/assets/img/courses/ma0505/variacion-acotada-poligonal.svg",
         "Aproximación poligonal de una curva"),
        ("/assets/img/courses/ma0505/medida-elemental-intervalo.svg",
         "La medida elemental de un intervalo"),
        ("/assets/img/courses/ma0505/conjunto-de-cantor.svg",
         "Los primeros pasos de la construcción del conjunto de Cantor"),
    ],
    MA0561_R: [
        ("/assets/img/courses/ma0561/factorizacion-de-homomorfismos.svg",
         "La factorización de un homomorfismo a través del cociente"),
    ],
}

# -----------------------------------------------------------------------------
# Macro expansion
# -----------------------------------------------------------------------------
# Gathered from the five preambles. MathJax on the site defines none of these,
# so every one has to be written out before the formula reaches the page.

SIMPLE_MACROS = {
    "Z": r"\mathbb{Z}",
    "R": r"\mathbb{R}",
    "Q": r"\mathbb{Q}",
    "N": r"\mathbb{N}",
    "C": r"\mathbb{C}",
    "F": r"\mathbb{F}",
    "HH": r"\mathbb{H}",
    "ind": r"\mathbf{1}",
    "Rext": r"\overline{\mathbb{R}}",
}

OPERATORS = [
    "Ker", "Imm", "Aut", "End", "Hom", "Frac", "Nil", "Rad", "Spec", "mSpec",
    "Char", "sgn", "mcd", "MCD", "Var", "diam",
]
OPERATOR_TEXT = {"Imm": "Im", "Char": "char"}

# Longest name first so \MCD is not eaten by \mcd's pattern, \mSpec not by \Spec.
_MACRO_NAMES = sorted(
    list(SIMPLE_MACROS) + OPERATORS, key=len, reverse=True
)
_MACRO_RE = re.compile(r"\\(" + "|".join(_MACRO_NAMES) + r")(?![a-zA-Z])")


def expand_macros(s: str) -> str:
    def sub(m: re.Match) -> str:
        name = m.group(1)
        if name in SIMPLE_MACROS:
            return SIMPLE_MACROS[name]
        return r"\operatorname{%s}" % OPERATOR_TEXT.get(name, name)

    return _MACRO_RE.sub(sub, s)


# -----------------------------------------------------------------------------
# Accents and text-mode escapes
# -----------------------------------------------------------------------------

ACCENTS = {
    "'a": "á", "'e": "é", "'i": "í", "'o": "ó", "'u": "ú",
    "'A": "Á", "'E": "É", "'I": "Í", "'O": "Ó", "'U": "Ú",
    "`a": "à", "`e": "è", "`i": "ì", "`o": "ò", "`u": "ù",
    "`A": "À", "`E": "È", "`I": "Ì", "`O": "Ò", "`U": "Ù",
    '"a': "ä", '"e': "ë", '"i': "ï", '"o': "ö", '"u': "ü",
    '"A': "Ä", '"O': "Ö", '"U': "Ü",
    "~n": "ñ", "~N": "Ñ", "~a": "ã", "~o": "õ",
    "^a": "â", "^e": "ê", "^i": "î", "^o": "ô", "^u": "û",
    "c c": "ç", "cc": "ç",
}


def strip_accent_macros(s: str) -> str:
    """`\\'a`, `\\'{a}`, `\\~n` -> the real character."""
    # Braced form first: \'{a}
    def braced(m: re.Match) -> str:
        return ACCENTS.get(m.group(1) + m.group(2), m.group(0))

    s = re.sub(r"\\(['`\"~^])\{([A-Za-z])\}", braced, s)
    s = re.sub(r"\\(['`\"~^])([A-Za-z])", braced, s)
    # \i and \j are dotless i/j used under accents; by this point the accent is
    # already resolved, so they are plain letters.
    s = re.sub(r"\\i(?![a-zA-Z])", "i", s)
    s = re.sub(r"\\j(?![a-zA-Z])", "j", s)
    return s


# -----------------------------------------------------------------------------
# Small helpers
# -----------------------------------------------------------------------------


def slugify(title: str) -> str:
    s = unicodedata.normalize("NFKD", title)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("–", "-").replace("—", "-").replace("'", "")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)


def match_brace(s: str, open_idx: int) -> int:
    """Index of the `}` closing the `{` at open_idx."""
    depth = 0
    i = open_idx
    while i < len(s):
        if s[i] == "\\":
            i += 2
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("unbalanced braces at %d" % open_idx)


def take_args(s: str, i: int, n: int) -> tuple[list[str], int]:
    """Read n brace groups starting at i; return their contents and the end index."""
    args = []
    for _ in range(n):
        while i < len(s) and s[i] in " \n\t":
            i += 1
        if i >= len(s) or s[i] != "{":
            raise ValueError("expected argument at %d: %r" % (i, s[i: i + 40]))
        j = match_brace(s, i)
        args.append(s[i + 1: j])
        i = j + 1
    return args, i


def clean_title(t: str) -> str:
    """A `\\section{...}` argument reduced to plain text fit for front matter."""
    # \texorpdfstring{$\R^{d}$}{Rd} keeps the plain-text alternative by design.
    while True:
        m = re.search(r"\\texorpdfstring", t)
        if not m:
            break
        args, end = take_args(t, m.end(), 2)
        t = t[: m.start()] + args[1] + t[end:]
    t = strip_accent_macros(t)
    t = re.sub(r"\\[a-zA-Z]+\s*", "", t)
    t = t.replace("$", "").replace("{", "").replace("}", "")
    t = t.replace("---", "—").replace("--", "–")
    return re.sub(r"\s+", " ", t).strip()


# -----------------------------------------------------------------------------
# Maths
# -----------------------------------------------------------------------------

DISPLAY_ENVS = ("align*", "align", "gather*", "gather", "multline*", "multline")
DISPLAY_ENV_MAP = {
    "align*": "aligned", "align": "aligned",
    "gather*": "gathered", "gather": "gathered",
    "multline*": "gathered", "multline": "gathered",
}

# Maths-only environments. Inside `$…$` or `\[…\]` they are carried across
# untouched; on the rare occasion one is written bare, it becomes a display.
BARE_MATH_ENVS = (
    "aligned", "gathered", "cases", "split", "array", "subequations",
    "matrix", "pmatrix", "bmatrix", "vmatrix", "Vmatrix", "smallmatrix",
)


def prepare_math(math: str) -> str:
    """Macros expanded and accents resolved; everything else left untouched.

    Accents matter because prose set in `\\text{…}` inside a formula is still
    prose -- `\\text{partici\\'on}` has to become `\\text{partición}` or MathJax
    prints the escape verbatim.
    """
    math = expand_macros(math)
    math = strip_accent_macros(math)
    return re.sub(r"\\qedhere\s*", "", math).strip()


def render_display(math: str) -> str:
    """A display formula as the site writes them: `$$` alone on its own lines."""
    return "\n\n$$\n%s\n$$\n\n" % prepare_math(math)


def render_inline(math: str) -> str:
    """Inline maths. The site uses `$$…$$` for inline too, not single `$`."""
    return "$$%s$$" % prepare_math(math)


def end_of_math_span(s: str, i: int) -> int:
    """Index just past the `$` closing the one at i, ignoring escaped dollars."""
    j = i + 1
    while j < len(s):
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "$":
            return j + 1
        j += 1
    raise ValueError("unterminated $ at %d: %r" % (i, s[i: i + 60]))


# -----------------------------------------------------------------------------
# Text-mode markup
# -----------------------------------------------------------------------------

INLINE_WRAPPERS = [
    ("emph", "*"), ("textit", "*"), ("textsl", "*"),
    ("textbf", "**"), ("textsc", ""), ("texttt", "`"),
    ("hlu", "*"), ("underline", "*"), ("mbox", ""), ("textrm", ""),
]

DROP_COMMANDS = [
    "noindent", "newpage", "clearpage", "par", "qedhere", "smallskip",
    "medskip", "bigskip", "centering", "itshape", "upshape", "normalfont",
    "scriptsize", "footnotesize", "small", "normalsize", "large", "Large",
    "allowdisplaybreaks", "nopagebreak", "pagebreak", "hfill", "vfill",
    "displaystyle", "leavevmode",
]


def convert_text_markup(s: str) -> str:
    """Text-mode LaTeX to markdown. Must run after maths has been extracted."""
    # \emph{...} and friends -> markdown emphasis, innermost first.
    for name, marker in INLINE_WRAPPERS:
        pattern = re.compile(r"\\" + name + r"\s*\{")
        while True:
            m = pattern.search(s)
            if not m:
                break
            j = match_brace(s, m.end() - 1)
            inner = s[m.end(): j]
            s = s[: m.start()] + marker + inner + marker + s[j + 1:]

    s = strip_accent_macros(s)

    for cmd in DROP_COMMANDS:
        s = re.sub(r"\\" + cmd + r"(?![a-zA-Z])\s?", "", s)

    s = re.sub(r"\\(?:hspace|vspace)\*?\{[^{}]*\}", "", s)
    s = re.sub(r"\\label\{[^{}]*\}", "", s)
    s = re.sub(r"\\(?:ref|eqref|pageref)\{[^{}]*\}", "", s)

    # Escaped punctuation
    for a, b in [(r"\%", "%"), (r"\&", "&"), (r"\_", "_"), (r"\#", "#"),
                 (r"\{", "{"), (r"\}", "}")]:
        s = s.replace(a, b)

    s = s.replace("---", "—").replace("--", "–")
    s = s.replace(r"\dots", "…").replace(r"\ldots", "…")
    s = s.replace("``", "\u201c").replace("''", "\u201d")
    s = s.replace("~", " ").replace("\\ ", " ").replace("\\,", " ")
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s


# -----------------------------------------------------------------------------
# Lists, figures and tables
# -----------------------------------------------------------------------------


def split_items(body: str) -> list[str]:
    """Split an enumerate/itemize body on top-level `\\item`."""
    items: list[str] = []
    depth = 0
    cur: list[str] = []
    i = 0
    while i < len(body):
        if body.startswith(r"\begin{", i):
            depth += 1
            cur.append(body[i])
            i += 1
            continue
        if body.startswith(r"\end{", i):
            depth -= 1
            cur.append(body[i])
            i += 1
            continue
        if depth == 0 and re.match(r"\\item(?![a-zA-Z])", body[i:]):
            if cur:
                items.append("".join(cur))
            cur = []
            i += len(r"\item")
            # \item[label] -- the optional label is dropped, markdown numbers itself
            if i < len(body) and body[i] == "[":
                k = body.index("]", i)
                i = k + 1
            continue
        cur.append(body[i])
        i += 1
    if cur:
        items.append("".join(cur))
    return [it for it in items if it.strip()]


def render_list(env: str, body: str, convert) -> str:
    items = split_items(body)
    lines = []
    for k, raw in enumerate(items, 1):
        text = convert(raw).strip()
        text = re.sub(r"\n{2,}", "\n\n", text)
        bullet = "- " if env.startswith("itemize") else "%d. " % k
        first, *rest = text.split("\n")
        lines.append(bullet + first)
        for r in rest:
            lines.append(("    " + r) if r.strip() else "")
    return "\n" + "\n".join(lines) + "\n"


def render_tabular(body: str, convert) -> str:
    """A LaTeX tabular as a markdown table (used for small Cayley tables)."""
    body = re.sub(r"\\hline|\\toprule|\\midrule|\\bottomrule", "", body)
    rows = [r.strip() for r in body.split(r"\\") if r.strip()]
    out = []
    for idx, row in enumerate(rows):
        cells = [convert(c).strip() for c in row.split("&")]
        out.append("| " + " | ".join(cells) + " |")
        if idx == 0:
            out.append("|" + "|".join([" --- "] * len(cells)) + "|")
    return "\n" + "\n".join(out) + "\n"


# -----------------------------------------------------------------------------
# Document parsing
# -----------------------------------------------------------------------------


def read_body(rel: str) -> str:
    t = (COURSES / rel).read_bytes().decode("utf-8").replace("\r\n", "\n")
    bm = re.search(r"^\\begin\{document\}", t, re.M)
    am = re.search(r"^\\appendix", t, re.M)
    body = t[bm.start(): am.start()]
    body = body[body.index(r"\end{titlepage}") + len(r"\end{titlepage}"):]
    # Drop the front matter between the titlepage and the first \section.
    first = re.search(r"^\\section\{", body, re.M)
    return body[first.start():]


def strip_comments(s: str) -> str:
    out = []
    for line in s.split("\n"):
        j = 0
        cut = None
        while j < len(line):
            if line[j] == "\\":
                j += 2
                continue
            if line[j] == "%":
                cut = j
                break
            j += 1
        out.append(line if cut is None else line[:cut])
    # A trailing `%` glues lines together in LaTeX; collapse those.
    return "\n".join(out)


def parse_sections(body: str) -> list[dict]:
    """[{title, subs: [{title, text}], preamble}] for the body sections."""
    sections = []
    positions = [(m.start(), m.end()) for m in re.finditer(r"^\\section\{", body, re.M)]
    for k, (start, end) in enumerate(positions):
        close = match_brace(body, end - 1)
        title = body[end:close]
        stop = positions[k + 1][0] if k + 1 < len(positions) else len(body)
        content = body[close + 1: stop]
        subs = []
        spos = [(m.start(), m.end()) for m in re.finditer(r"^\\subsection\{", content, re.M)]
        preamble = content[: spos[0][0]] if spos else content
        for j, (s0, s1) in enumerate(spos):
            sclose = match_brace(content, s1 - 1)
            stitle = content[s1:sclose]
            sstop = spos[j + 1][0] if j + 1 < len(spos) else len(content)
            subs.append({"title": stitle, "text": content[sclose + 1: sstop]})
        sections.append({"title": title, "subs": subs, "preamble": preamble})
    return sections


# -----------------------------------------------------------------------------
# Block conversion
# -----------------------------------------------------------------------------


class Converter:
    def __init__(self, src: str):
        self.src = src
        self.figures = list(FIGURES.get(src, []))
        self.fig_index = 0
        self.warnings: list[str] = []

    # -- leaf text -----------------------------------------------------------
    def text(self, s: str, holes: list[str] | None = None) -> str:
        """Prose. Formulas arrive as placeholders and are put back afterwards.

        Keeping them out of the way matters because a formula routinely sits
        inside a markup span -- `\\emph{una función $f$ acotada}` -- and the
        span has to stay whole while the markup rules run.
        """
        s = convert_text_markup(s)
        if holes:
            s = re.sub(r"\x00(\d+)\x00", lambda m: holes[int(m.group(1))], s)
        return s

    # -- structured blocks ---------------------------------------------------
    def blocks(self, s: str) -> str:
        """One linear pass over a chunk of LaTeX.

        Maths, environments and prose are recognised in the same loop, so a
        `\\begin{aligned}` sitting inside a `\\[ … \\]` is consumed as part of
        that display rather than being mistaken for a block of its own.
        """
        out: list[str] = []
        pending: list[str] = []
        holes: list[str] = []

        def hole(rendered: str) -> None:
            pending.append("\x00%d\x00" % len(holes))
            holes.append(rendered)

        def flush() -> None:
            if pending:
                out.append(self.text("".join(pending), holes))
                pending.clear()

        i = 0
        n = len(s)
        while i < n:
            # --- maths ---------------------------------------------------------
            if s.startswith(r"\[", i):
                j = s.index(r"\]", i)
                hole(render_display(s[i + 2: j]))
                i = j + 2
                continue
            if s.startswith(r"\(", i):
                j = s.index(r"\)", i)
                hole(render_inline(s[i + 2: j]))
                i = j + 2
                continue
            if s.startswith(r"\$", i):
                pending.append("$")
                i += 2
                continue
            # TeX display maths. Rare here (one occurrence across the five
            # documents) but it has to be matched before the single-$ case,
            # which would otherwise read `$$` as an empty inline span.
            if s.startswith("$$", i):
                j = s.index("$$", i + 2)
                hole(render_display(s[i + 2: j]))
                i = j + 2
                continue
            if s[i] == "$":
                j = end_of_math_span(s, i)
                hole(render_inline(s[i + 1: j - 1]))
                i = j
                continue
            # --- environments --------------------------------------------------
            m = re.match(r"\\begin\{([A-Za-z*]+)\}", s[i:])
            if m:
                env = m.group(1)
                end = self._find_end(s, i, env)
                if env in DISPLAY_ENVS:
                    inner = s[i + m.end(): end - len(r"\end{%s}" % env)]
                    inner = inner.replace(r"\nonumber", "").replace(r"\notag", "")
                    target = DISPLAY_ENV_MAP[env]
                    hole(render_display(
                        "\\begin{%s}%s\\end{%s}" % (target, inner, target)))
                    i = end
                    continue
                if env in BARE_MATH_ENVS:
                    # A matrix or cases block that was written outside $…$.
                    hole(render_display(s[i:end]))
                    i = end
                    continue
                flush()
                inner = s[i + m.end(): end - len(r"\end{%s}" % env)]
                out.append(self.environment(env, inner, s[i: i + m.end()]))
                i = end
                continue
            if s[i] == "\\" and i + 1 < n:
                pending.append(s[i: i + 2])
                i += 2
                continue
            pending.append(s[i])
            i += 1
        flush()
        return "".join(out)

    @staticmethod
    def _find_end(s: str, start: int, env: str) -> int:
        open_tag = r"\begin{%s}" % env
        close_tag = r"\end{%s}" % env
        depth = 0
        i = start
        while i < len(s):
            if s.startswith(open_tag, i):
                depth += 1
                i += len(open_tag)
                continue
            if s.startswith(close_tag, i):
                depth -= 1
                i += len(close_tag)
                if depth == 0:
                    return i
                continue
            i += 1
        raise ValueError("unterminated %s" % env)

    def environment(self, env: str, inner: str, opening: str) -> str:
        if env in ("namedstd", "namedres"):
            args, rest_at = take_args(inner, 0, 2)
            kind = clean_title(args[0])
            # The name carries maths often enough -- "Familia de normas $p$ en
            # $\R^{d}$" -- that it goes through the full scanner, matching how
            # ma0350/ma0450 write `### Definición ($$\mathbb{R}^{n}$$)`.
            name = re.sub(r"\s+", " ", self.blocks(args[1])).strip()
            body = self.blocks(inner[rest_at:])
            return "\n\n### %s (%s)\n\n%s\n\n" % (kind, name, body.strip())

        if env == "proof":
            body = self.blocks(inner).strip()
            # Fold the label into the first paragraph so it reads as one block.
            body = re.sub(r"^\s+", "", body)
            return "\n\n***Prueba:*** %s\n\n" % body

        if env in ("enumerate", "itemize", "description"):
            # Drop the enumitem option block: [label=(\arabic*),leftmargin=2em]
            body = inner
            if body.lstrip().startswith("["):
                k = body.index("[")
                body = body[body.index("]", k) + 1:]
            return render_list(env, body, self.blocks)

        if env == "center":
            return self.centered(inner)

        if env == "tikzpicture":
            return self.figure()

        if env in ("tabular", "longtable", "tabularx"):
            body = inner
            if body.lstrip().startswith("{"):
                k = body.index("{")
                body = body[match_brace(body, k) + 1:]
            # Cells hold maths as often as prose -- a Cayley table is all
            # symbols -- so they go through the full scanner, not just markup.
            return render_tabular(body, self.blocks)

        if env in ("quote", "quotation", "minipage", "flushleft", "flushright"):
            return self.blocks(inner)

        self.warnings.append("unhandled environment: %s" % env)
        return self.blocks(inner)

    def centered(self, inner: str) -> str:
        # Notebook photographs that were never included in the repository.
        if r"\fbox" in inner and "Figura del cuaderno" in inner:
            return "\n\n"
        return self.blocks(inner)

    def figure(self) -> str:
        if self.fig_index >= len(self.figures):
            self.warnings.append("tikzpicture with no figure mapping")
            return "\n\n"
        path, caption = self.figures[self.fig_index]
        self.fig_index += 1
        return "\n\n![%s](%s)\n\n" % (caption, path)


# -----------------------------------------------------------------------------
# Assembly
# -----------------------------------------------------------------------------


def tidy(md: str) -> str:
    md = md.replace("\r\n", "\n")
    # Source indentation carries no meaning here, and a leading tab would make
    # kramdown read the line as a code block. List continuations are indented by
    # render_list with spaces, after this runs.
    md = re.sub(r"^\t+", "", md, flags=re.M)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    # A display formula whose sentence-ending punctuation was written after the
    # closing delimiter, which would otherwise leave a paragraph holding a lone
    # full stop. The source usually puts it inside; pull it in when it doesn't.
    md = re.sub(r"\n\$\$\n\n([.,;:])[ \t]*(?=\n|\Z)", r"\1\n$$\n", md)
    # A heading always gets a blank line before and after it.
    md = re.sub(r"\n(#{2,4} )", r"\n\n\1", md)
    md = re.sub(r"(#{2,4} [^\n]+)\n(?!\n)", r"\1\n\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def front_matter(course: str, n: int, title: str, slug: str, lang: str) -> str:
    """Chapter front matter.

    `chapter` has to agree across languages: lang_switch.liquid pairs a page
    with its counterpart on (course, chapter, lang), so a mismatch silently
    hides the switcher. English sits at the unprefixed URL, as in ma0350/ma0450.
    """
    permalink = (f"/notes/{course}/{slug}/" if lang == "en"
                 else f"/notes/{course}/{lang}/{slug}/")
    return (
        "---\n"
        "layout: chapter\n"
        f"course: {course}\n"
        f"chapter: {n}\n"
        f'title: "{title}"\n'
        f"slug: {slug}\n"
        "toc:\n"
        "  sidebar: right\n"
        f"lang: {lang}\n"
        f"permalink: {permalink}\n"
        "---\n\n"
    )


def build_chapter(course: str, ch: dict) -> tuple[str, str, str, dict]:
    body = strip_comments(read_body(ch["src"]))
    sections = parse_sections(body)
    section = sections[ch["sec"] - 1]

    conv = Converter(ch["src"])

    def tikz_count(*chunks: str) -> int:
        return sum(len(re.findall(r"\\begin\{tikzpicture\}", c)) for c in chunks)

    def section_text(sec: dict) -> str:
        return sec["preamble"] + "".join(s["text"] for s in sec["subs"])

    # FIGURES lists a source file's pictures in document order, so count the
    # ones this chapter is preceded by to land on the right entry.
    seen = sum(tikz_count(section_text(sections[k])) for k in range(ch["sec"] - 1))
    if ch["subs"] is not None:
        chosen = [section["subs"][j - 1] for j in ch["subs"]]
        seen += tikz_count(section["preamble"])
        seen += tikz_count(*[section["subs"][j - 1]["text"]
                             for j in range(1, min(ch["subs"]))])
    else:
        chosen = section["subs"]
    conv.fig_index = seen

    parts: list[str] = []
    if ch["subs"] is None and section["preamble"].strip():
        parts.append(conv.blocks(section["preamble"]))
    for sub in chosen:
        parts.append("\n\n## %s\n\n" % clean_title(sub["title"]))
        parts.append(conv.blocks(sub["text"]))

    title = ch.get("title") or clean_title(section["title"])
    slug = "%02d-%s" % (ch["n"], slugify(title))
    md = tidy("".join(parts))

    # Structural gate: nothing may be lost between the LaTeX and the markdown.
    src_text = "".join(s["text"] for s in chosen) + (
        section["preamble"] if ch["subs"] is None else "")
    stats = {
        "results_src": len(re.findall(r"\\begin\{named(?:std|res)\}", src_text)),
        "results_md": len(re.findall(r"^### ", md, re.M)),
        "proofs_src": len(re.findall(r"\\begin\{proof\}", src_text)),
        "proofs_md": len(re.findall(r"\*\*\*Prueba:\*\*\*", md)),
        "subs_src": len(chosen),
        "subs_md": len(re.findall(r"^## ", md, re.M)),
        "warnings": conv.warnings,
    }
    body = front_matter(course, ch["n"], title, slug, "es")
    return title, slug, body + "{% raw %}\n" + md + "{% endraw %}\n", stats


def main(dry_run: bool, manifest: str | None) -> int:
    problems: list[str] = []
    entries: list[dict] = []
    for course, chapters in CHAPTERS.items():
        outdir = COURSES / course / "es"
        if not dry_run:
            outdir.mkdir(parents=True, exist_ok=True)
        for ch in chapters:
            title, slug, text, stats = build_chapter(course, ch)
            path = outdir / ("%s.md" % slug)
            en_title = ch["en"]
            en_slug = "%02d-%s" % (ch["n"], slugify(en_title))
            entries.append({
                "course": course,
                "chapter": ch["n"],
                "es_title": title,
                "es_path": str((path).relative_to(ROOT)).replace("\\", "/"),
                "en_title": en_title,
                "en_path": "_courses/%s/en/%s.md" % (course, en_slug),
                "en_front_matter": front_matter(
                    course, ch["n"], en_title, en_slug, "en"),
                "results": stats["results_md"],
                "proofs": stats["proofs_md"],
                "subsections": stats["subs_md"],
            })
            flag = ""
            if stats["results_src"] != stats["results_md"]:
                problems.append("%s: %d results in source, %d in markdown"
                                % (path.name, stats["results_src"], stats["results_md"]))
                flag = "  <-- RESULT COUNT"
            if stats["proofs_src"] != stats["proofs_md"]:
                problems.append("%s: %d proofs in source, %d in markdown"
                                % (path.name, stats["proofs_src"], stats["proofs_md"]))
                flag = "  <-- PROOF COUNT"
            if stats["subs_src"] != stats["subs_md"]:
                problems.append("%s: %d subsections in source, %d headings"
                                % (path.name, stats["subs_src"], stats["subs_md"]))
                flag = "  <-- SUBSECTION COUNT"
            for w in stats["warnings"]:
                problems.append("%s: %s" % (path.name, w))
            print("%-58s %6d chars  res=%-3d proofs=%-3d subs=%d%s"
                  % (path.relative_to(ROOT), len(text), stats["results_md"],
                     stats["proofs_md"], stats["subs_md"], flag))
            if not dry_run:
                path.write_text(text, encoding="utf-8")

    if manifest:
        Path(manifest).write_text(
            json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
        print("\nmanifest: %s (%d chapters)" % (manifest, len(entries)))

    if problems:
        print("\n%d problem(s):" % len(problems))
        for p in problems:
            print("  -", p)
        return 1
    print("\nAll chapters converted with matching result, proof and subsection counts.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--manifest", help="write a JSON chapter manifest here")
    args = ap.parse_args()
    sys.exit(main(args.dry_run, args.manifest))
