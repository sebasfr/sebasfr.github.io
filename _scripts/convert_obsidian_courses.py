"""One-time conversion of Obsidian course notes into Jekyll _courses collection.

Reads from _posts/MA0XXX/, writes to _courses/ma0xxx/. Strips Obsidian header
metadata, rewrites [[wikilinks]] to plain text, and rewrites ![[embeds]] to
Markdown image references that point at /assets/img/courses/ma0xxx/.
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_BASE = ROOT / "_posts"
DST_COURSES = ROOT / "_courses"
DST_ASSETS = ROOT / "assets" / "img" / "courses"

COURSES = {
    "MA0350": {
        "slug": "ma0350",
        "title_en": "Single Variable Real Analysis",
        "instructor": "Prof. Pedro Méndez",
    },
    "MA0450": {
        "slug": "ma0450",
        "title_en": "Multivariate Real Analysis",
        "instructor": "Prof. Juan Gabriel Calvo",
    },
}

TAG_LINE_RE = re.compile(r"^\s*#\w+(\s+#\w+)*\s*$")  # #Mate #MA0350
H1_LINE_RE = re.compile(r"^\s*#\s+\S")  # # Heading (title duplicate)
PARENS_NOTE_RE = re.compile(r"^\s*\(Ver\s+presentaci[oó]n\)\s*$", re.IGNORECASE)
META_LABEL_RE = re.compile(
    r"^\s*(Fecha|Temas\s+relacionados|Prerrequisitos|Ver\s+tambi[eé]n|"
    r"Generaliza|Generalizaci[oó]n|Conecta\s+con|Taylor)\b.*?:",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"^\s*Fecha\s*:\s*(.*?)\s*$", re.IGNORECASE)
WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\]]+)\]\]")
EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")

# Inline math `$ … $` (single dollars) — kramdown's GFM mode does not recognise
# this as math and runs underscore-italic processing inside, corrupting LaTeX
# like ${x_n}_{n=1}^\infty$. Promote to `$$ … $$` which kramdown does treat as
# math. Pattern excludes already-doubled dollars and unmatched singletons.
INLINE_MATH_RE = re.compile(r"(?<!\$)\$([^$\n]+?)\$(?!\$)")


def slugify(value: str) -> str:
    """ASCII-fold and slugify a Spanish title for URLs and filenames."""
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def parse_filename(path: Path) -> tuple[int, str, str]:
    """Return (chapter_number, spanish_title, slug) for '01 - Sucesiones.md'."""
    stem = path.stem
    m = re.match(r"^(\d+)\s*[-–—]\s*(.+)$", stem)
    if not m:
        raise ValueError(f"Unexpected filename: {path}")
    num = int(m.group(1))
    title = m.group(2).strip()
    slug = f"{num:02d}-{slugify(title)}"
    return num, title, slug


def replace_wikilink(match: re.Match[str]) -> str:
    """[[Target]], [[Target|alias]], [[Target#Heading|alias]] -> plain text."""
    inner = match.group(1)
    if "|" in inner:
        return inner.split("|", 1)[1]
    if "#" in inner:
        return inner.split("#", 1)[1]
    return inner


def make_embed_replacer(course_slug: str):
    def replace_embed(match: re.Match[str]) -> str:
        inner = match.group(1).strip()
        # Drop Obsidian fragment (e.g. svg#invert_B) — its CSS hack does not apply here.
        filename = inner.split("#", 1)[0].strip()
        # Embeds may include a relative directory prefix (e.g. "attachments/foo.svg").
        # We resolve every embed by basename — all assets sit in the per-course folder.
        basename = Path(filename).name
        url_filename = basename.replace(" ", "%20")
        alt = Path(basename).stem
        return f"![{alt}](/assets/img/courses/{course_slug}/{url_filename})"
    return replace_embed


def strip_obsidian_header(body: str) -> tuple[str, str | None]:
    """Strip leading Obsidian metadata lines. Return (cleaned_body, fecha_or_none).

    Stops at the first non-blank line that is not: a tag line, an H1, a known
    metadata label (Fecha, Ver también, etc.), or a (Ver presentación)-style note.
    """
    lines = body.splitlines()
    fecha: str | None = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if (
            TAG_LINE_RE.match(line)
            or H1_LINE_RE.match(line)
            or PARENS_NOTE_RE.match(line)
            or META_LABEL_RE.match(line)
        ):
            m = DATE_RE.match(line)
            if m and fecha is None:
                value = m.group(1).strip()
                fecha = value or None
            i += 1
            continue
        break
    cleaned = "\n".join(lines[i:]).lstrip("\n")
    return cleaned, fecha


def front_matter(course_slug: str, chapter: int, title: str, fecha: str | None) -> str:
    fields = [
        "layout: chapter",
        f"course: {course_slug}",
        f"chapter: {chapter}",
        f'title: "{title.replace(chr(34), chr(92) + chr(34))}"',
        f"slug: {chapter:02d}-{slugify(title)}",
        "toc:",
        "  sidebar: right",
        "lang: es",
    ]
    if fecha:
        fields.append(f"fecha: {fecha}")
    return "---\n" + "\n".join(fields) + "\n---\n\n"


# Match any `$$…$$` region (single-line inline or multi-line block). DOTALL so
# `.` spans newlines; non-greedy so multiple regions don't merge.
BLOCK_MATH_RE = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)


def transform_math(text: str) -> str:
    """Normalise math markup so kramdown handles it correctly.

    Two things go wrong without this:
      1. kramdown's GFM input mode runs underscore-italic processing inside
         single-`$ … $` math, corrupting things like `${x_n}_{n=1}^\\infty$`.
         Fix: promote single-dollar inline math to `$$ … $$`, which kramdown
         recognises as math and leaves alone.
      2. Promotion must NOT touch `$ … $` that sits inside an existing
         `$$ … $$` block (e.g. `\\text{para $a \\neq 1$.}` inside aligned),
         because injecting `$$…$$` there breaks the outer block.
      3. Multi-line block math whose opener or closer share a line with
         content (e.g. `$$ \\frac{…} \\tag{1}` … blank line … `$$`) must be
         normalised to a clean `$$\\n<body>\\n$$` form so kramdown recognises
         the block.

    Strategy: scan for `$$…$$` regions; promote `$…$` only outside; normalise
    each region's content (strip, preserve internal newlines as-is).
    """

    def promote(match: re.Match[str]) -> str:
        return f"$${match.group(1)}$$"

    pieces: list[str] = []
    pos = 0
    for m in BLOCK_MATH_RE.finditer(text):
        before = text[pos : m.start()]
        pieces.append(INLINE_MATH_RE.sub(promote, before))
        body = m.group(1)
        if "\n" in body:
            # Multi-line block math. Force paragraph isolation by surrounding
            # with `\n\n`. This pulls the block out of any enclosing list item
            # or paragraph (kramdown can't render multi-line math nested in a
            # list item), but it's the only way to make MathJax see a clean
            # display block.
            cleaned = body.strip("\n")
            cleaned_lines = [ln for ln in cleaned.splitlines() if ln.strip() != ""]
            pieces.append("\n\n$$\n" + "\n".join(cleaned_lines) + "\n$$\n\n")
        else:
            # Single-line inline `$$ … $$` — keep verbatim.
            pieces.append(f"$${body}$$")
        pos = m.end()
    pieces.append(INLINE_MATH_RE.sub(promote, text[pos:]))
    return "".join(pieces)


def isolate_block_math(text: str) -> str:
    """Ensure `$$ … $$` blocks (with `$$` markers on their own lines) sit in
    their own paragraph — kramdown only treats them as block math when there
    is a blank line before the opener and after the closer. Adds blanks at
    those two boundaries only; never inside the block."""
    lines = text.splitlines()
    out: list[str] = []
    in_block = False
    for i, line in enumerate(lines):
        if line.strip() == "$$":
            if not in_block:  # opener
                if out and out[-1].strip() != "":
                    out.append("")
                out.append(line)
                in_block = True
            else:  # closer
                out.append(line)
                if i + 1 < len(lines) and lines[i + 1].strip() != "":
                    out.append("")
                in_block = False
            continue
        out.append(line)
    return "\n".join(out)


HACER_DIBUJO_RE = re.compile(
    r"\*+\s*hacer\s+dibujo[^*\n]*\*+\s*",
    re.IGNORECASE,
)


def strip_author_notes(text: str) -> str:
    """Remove "Hacer dibujo" author-to-self notes left over in the Obsidian
    source. Matches `***Hacer dibujo***`, `**Hacer dibujo**`, mismatched
    asterisks, and trailing-qualifier variants like
    `***Hacer dibujo de convergencia***`."""
    return HACER_DIBUJO_RE.sub("", text)


def strip_leading_tabs(text: str) -> str:
    """Strip leading tabs from each line.

    Obsidian uses tabs for visual indentation of continuation prose; kramdown
    treats tab-indented lines as code blocks, which mangles LaTeX. Replace
    each leading tab with nothing so the line becomes plain prose. (Real code
    blocks in these notes are fenced with triple backticks, not tab-indented.)
    """
    return "\n".join(line.lstrip("\t") for line in text.splitlines())


def convert_chapter(src: Path, course_slug: str, dst_dir: Path) -> tuple[int, str, str]:
    chapter_num, spanish_title, slug = parse_filename(src)
    raw = src.read_text(encoding="utf-8")
    body, fecha = strip_obsidian_header(raw)
    body = WIKILINK_RE.sub(replace_wikilink, body)
    body = EMBED_RE.sub(make_embed_replacer(course_slug), body)
    body = strip_author_notes(body)
    body = strip_leading_tabs(body)
    body = transform_math(body)
    body = isolate_block_math(body)
    # Wrap body in {% raw %} so Liquid does not try to parse `{{ … }}` patterns
    # inside math expressions (e.g. \{ x_{1} \} or {{n_{k}}}).
    out = (
        front_matter(course_slug, chapter_num, spanish_title, fecha)
        + "{% raw %}\n"
        + body.rstrip()
        + "\n{% endraw %}\n"
    )
    out_path = dst_dir / f"{slug}.md"
    out_path.write_text(out, encoding="utf-8")
    return chapter_num, spanish_title, slug


GLOBAL_ATTACHMENTS = SRC_BASE / "attachments"


def copy_attachments(src_dir: Path, course_slug: str) -> int:
    """Copy attachments to the per-course asset folder. Merges files from the
    course's local `attachments/` folder and from the shared global folder
    (`_posts/attachments/`), which mirrors the Obsidian vault's global
    attachment store. Per-course files win on name collision."""
    dst = DST_ASSETS / course_slug
    dst.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    count = 0
    if src_dir.exists():
        for f in src_dir.iterdir():
            if f.is_file():
                shutil.copy2(f, dst / f.name)
                seen.add(f.name)
                count += 1
    if GLOBAL_ATTACHMENTS.exists():
        for f in GLOBAL_ATTACHMENTS.iterdir():
            if f.is_file() and f.name not in seen:
                shutil.copy2(f, dst / f.name)
                count += 1
    return count


def main() -> None:
    DST_COURSES.mkdir(exist_ok=True)
    DST_ASSETS.mkdir(parents=True, exist_ok=True)

    for code, meta in COURSES.items():
        src_dir = SRC_BASE / code
        course_slug = meta["slug"]
        dst_dir = DST_COURSES / course_slug
        dst_dir.mkdir(parents=True, exist_ok=True)

        chapters: list[tuple[int, str, str]] = []
        for md in sorted(src_dir.glob("*.md")):
            chapters.append(convert_chapter(md, course_slug, dst_dir))

        n_assets = copy_attachments(src_dir / "attachments", course_slug)
        print(f"{code}: {len(chapters)} chapters, {n_assets} attachments")
        for num, title, slug in chapters:
            print(f"  {num:02d}  {title}  ->  {slug}.md")


if __name__ == "__main__":
    main()
