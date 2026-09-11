r"""Structural checks on the _courses collection.

Catches the class of mistake a Jekyll build would surface -- malformed front
matter, a permalink that disagrees with its slug, an unbalanced `{% raw %}` --
plus the one it would not: a chapter whose `chapter:` number has no counterpart
in the other language, which silently hides the language switcher instead of
erroring.

    python _scripts/verify_courses.py

Exits non-zero if anything is off, so it can gate a commit.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "_courses"

LANGS = ("es", "en")
CHAPTER_KEYS = {"layout", "course", "chapter", "title", "slug", "toc", "lang",
                "permalink"}
INDEX_KEYS = {"layout", "course", "code", "lang", "permalink", "title",
              "title_native", "instructor", "institution", "description"}

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.S)


def load(path: Path) -> tuple[dict, str] | None:
    m = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if not m:
        return None
    return yaml.safe_load(m.group(1)), m.group(2)


def check() -> int:
    problems: list[str] = []
    # course -> lang -> chapter number -> path
    seen: dict[str, dict[str, dict[int, Path]]] = defaultdict(
        lambda: defaultdict(dict))

    course_dirs = sorted(d for d in COURSES.iterdir() if d.is_dir())
    for course_dir in course_dirs:
        course = course_dir.name
        for lang in LANGS:
            langdir = course_dir / lang
            if not langdir.is_dir():
                problems.append("%s: missing %s/ directory" % (course, lang))
                continue

            index = langdir / "index.md"
            if not index.exists():
                problems.append("%s/%s: no index.md" % (course, lang))
            else:
                loaded = load(index)
                if loaded is None:
                    problems.append("%s/%s/index.md: no front matter" % (course, lang))
                else:
                    fm, _ = loaded
                    missing = INDEX_KEYS - set(fm)
                    if missing:
                        problems.append("%s/%s/index.md: missing %s"
                                        % (course, lang, ", ".join(sorted(missing))))
                    if fm.get("layout") != "course-home":
                        problems.append("%s/%s/index.md: layout is %r"
                                        % (course, lang, fm.get("layout")))
                    if fm.get("lang") != lang:
                        problems.append("%s/%s/index.md: lang is %r"
                                        % (course, lang, fm.get("lang")))
                    want = ("/notes/%s/" % course if lang == "en"
                            else "/notes/%s/%s/" % (course, lang))
                    if fm.get("permalink") != want:
                        problems.append("%s/%s/index.md: permalink %r, expected %r"
                                        % (course, lang, fm.get("permalink"), want))

            for path in sorted(langdir.glob("[0-9]*.md")):
                loaded = load(path)
                if loaded is None:
                    problems.append("%s: no front matter" % path.name)
                    continue
                fm, body = loaded
                rel = "%s/%s/%s" % (course, lang, path.name)

                missing = CHAPTER_KEYS - set(fm)
                if missing:
                    problems.append("%s: missing %s"
                                    % (rel, ", ".join(sorted(missing))))
                    continue

                if fm["layout"] != "chapter":
                    problems.append("%s: layout is %r" % (rel, fm["layout"]))
                if fm["course"] != course:
                    problems.append("%s: course is %r" % (rel, fm["course"]))
                if fm["lang"] != lang:
                    problems.append("%s: lang is %r" % (rel, fm["lang"]))
                if not isinstance(fm["chapter"], int):
                    problems.append("%s: chapter is %r, not an integer"
                                    % (rel, fm["chapter"]))
                    continue
                if fm["slug"] != path.stem:
                    problems.append("%s: slug %r does not match the filename"
                                    % (rel, fm["slug"]))
                want = ("/notes/%s/%s/" % (course, fm["slug"]) if lang == "en"
                        else "/notes/%s/%s/%s/" % (course, lang, fm["slug"]))
                if fm["permalink"] != want:
                    problems.append("%s: permalink %r, expected %r"
                                    % (rel, fm["permalink"], want))
                if not str(fm["slug"]).startswith("%02d-" % fm["chapter"]):
                    problems.append("%s: slug does not start with %02d-"
                                    % (rel, fm["chapter"]))

                opens = body.count("{% raw %}")
                closes = body.count("{% endraw %}")
                if opens != closes:
                    problems.append("%s: %d {%% raw %%} vs %d {%% endraw %%}"
                                    % (rel, opens, closes))
                elif opens != 1:
                    problems.append("%s: expected exactly one raw block, found %d"
                                    % (rel, opens))
                if body.count("$$") % 2:
                    problems.append("%s: odd number of $$ delimiters" % rel)

                if fm["chapter"] in seen[course][lang]:
                    problems.append(
                        "%s: chapter %d already used by %s"
                        % (rel, fm["chapter"], seen[course][lang][fm["chapter"]].name))
                seen[course][lang][fm["chapter"]] = path

    # The switcher pairs on (course, chapter, lang); an unmatched number means a
    # page renders with no way to reach its counterpart.
    for course in sorted(seen):
        es = set(seen[course].get("es", {}))
        en = set(seen[course].get("en", {}))
        for n in sorted(es - en):
            problems.append("%s: chapter %d exists in es but not en (%s)"
                            % (course, n, seen[course]["es"][n].name))
        for n in sorted(en - es):
            problems.append("%s: chapter %d exists in en but not es (%s)"
                            % (course, n, seen[course]["en"][n].name))
        if es and es != set(range(1, max(es) + 1)):
            problems.append("%s: es chapter numbers are not 1..%d contiguous"
                            % (course, max(es)))

    for course in sorted(seen):
        print("%-8s es=%-3d en=%-3d" % (course, len(seen[course].get("es", {})),
                                        len(seen[course].get("en", {}))))
    if problems:
        print("\n%d problem(s):" % len(problems))
        for p in problems:
            print("  -", p)
        return 1
    print("\nAll courses structurally sound.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
