# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal academic website built on [al-folio](https://github.com/alshedivat/al-folio), a Jekyll theme for academics. It is deployed to GitHub Pages at https://sebasfr.github.io.

**Stack:** Jekyll (Ruby) + Liquid templates + SCSS + Bootstrap 4 + MDB (Material Design Bootstrap)

## Development Commands

### Local Development

```bash
# Install Ruby dependencies
bundle install

# Install Node dependencies
npm install

# Serve locally with live reload
bundle exec jekyll serve

# Serve with drafts
bundle exec jekyll serve --drafts

# Build for production
bundle exec jekyll build

# Format code (Liquid, HTML, JS, etc.)
npx prettier --write .
```

### Docker Alternative

```bash
docker-compose up
```

## Architecture

### Collections and Content

| Directory | Purpose |
|-----------|---------|
| `_pages/` | Static pages (about, cv, publications, projects, blog, etc.) |
| `_posts/` | Blog posts (filename: `YYYY-MM-DD-title.md`) |
| `_projects/` | Project showcase items |
| `_news/` | Short announcements shown on about page |
| `_books/` | Book reviews |
| `_bibliography/` | BibTeX files for publications (via jekyll-scholar) |
| `_data/` | YAML data for CV, repositories, coauthors, etc. |

### Templates

- `_layouts/` — Page layout templates (Liquid). `default.liquid` is the base; others extend it.
- `_includes/` — Reusable components (header, footer, social links, etc.)

### Styling

- `_sass/` — SCSS source files; `_variables.scss` controls colors/spacing, `_base.scss` is the main stylesheet.
- `assets/css/main.scss` — Entry point that imports all SCSS partials.
- Light/dark mode theming is handled in `_sass/_themes.scss` and `assets/js/theme.js`.

#### Custom Design System

The site was refactored from the default al-folio theme into a **neo-brutalist editorial/serif** design (see commit `61eb7b7`). Subsequent commits added page-head text animations, a refreshed CV, and a vintage-sharpened palette.

**Design tokens** (`_sass/_tokens.scss`):

All typography, spacing, motion, and semantic color tokens are defined as CSS custom properties in `_tokens.scss`, layered on top of the palette in `_variables.scss` / `_themes.scss`. Consume these via `var(--font-serif)`, `var(--type-h1)`, `var(--motion-duration-normal)`, etc. — do not hardcode values.

Key token groups:

- **Type**: `--font-serif`, `--font-mono`, `--type-hero-wordmark`, `--type-drop-numeral`, `--type-h1/h2`, `--type-dek`, `--type-body`, `--type-meta`, `--measure`, `--rail-width`.
- **Editorial semantics**: `--rule-color`, `--rail-bg-color`, `--rail-border-color`, `--mono-label-color`, `--footnote-rail-color` (each has a dark-mode override).
- **Motion**: `--motion-duration-fast/normal/page-turn/letter/axis`, `--motion-ease-out/page-turn/stamp`. All durations collapse to `0ms` under `prefers-reduced-motion`.

**Typography:**

- Global serif is **Fraunces** (loaded via `_sass/_fonts.scss`), with Georgia / Times New Roman fallbacks — exposed as `--font-serif`.
- Monospace is **JetBrains Mono** — exposed as `--font-mono`, used for meta labels, code, and drop-numerals.
- Playfair Display is no longer used.

**Color Themes** (`_sass/_variables.scss` + `_sass/_themes.scss`):

Five named palettes are defined in `_variables.scss` (`econometrician`, `journal`, `ledger`, `algo`, `vintage`), each with full light and dark variants.

**Active theme: `vintage`** (burnt orange `#c2410c` light / muted orange `#fb923c` dark, warm cream/beige surfaces). `_themes.scss` maps `$vintage-*` SCSS variables to the global CSS custom properties for both `:root` (light) and `html[data-theme="dark"]`. To switch themes, replace all `$vintage-*` references in `_themes.scss` and `_tokens.scss` with the corresponding `$<theme>-*` variables.

#### SCSS Partials

The stylesheet is split into focused partials under `_sass/`:

| File | Purpose |
| --- | --- |
| `_tokens.scss` | Design tokens (type/space/motion/semantic colors) |
| `_variables.scss` | Palette SCSS variables for all five themes |
| `_themes.scss` | Maps active palette to `--global-*` custom properties |
| `_fonts.scss` | `@font-face` declarations (Fraunces, JetBrains Mono) |
| `_base.scss` | Global element styling |
| `_layout.scss` / `_grid.scss` | Page layout + editorial grid |
| `_rail.scss` | Sidebar rail (desktop) + mobile drawer styling |
| `_home.scss` / `_cv.scss` / `_research.scss` / `_teaching.scss` / `_notes.scss` / `_post.scss` | Per-page/surface styles |
| `_tabs.scss` / `_typograms.scss` / `_animations.scss` | Interaction + motion primitives |
| `_distill.scss` | Distill-style article layout |

#### Editorial Includes

Custom Liquid components under `_includes/` drive the editorial surfaces:

- `hero_masthead.liquid`, `hero_wordmark.liquid`, `post_supertitle.liquid` — page/article heads with animated type.
- `sidebar_rail.liquid`, `mobile_drawer.liquid` — primary navigation (desktop rail + mobile drawer with theme toggle).
- `sfr_logo.liquid` — site wordmark.
- `dispatches.liquid`, `newsletter.liquid`, `latest_posts.liquid`, `selected_papers.liquid`, `flar_feature.liquid` — home-page content blocks.
- `cv/` and `resume/` — CV/résumé partials used by the `cv` layout.

### Site Configuration

All major site settings are in `_config.yml`:
- Author info, URL, social links
- Feature toggles (navbar, footer, RSS, search, etc.)
- Plugin configuration (jekyll-scholar for bibliography, jekyll-paginate-v2 for blog)
- Google Analytics ID

### Key Plugins

- **jekyll-scholar** — Renders BibTeX bibliography from `_bibliography/` files
- **jekyll-minifier** — Minifies HTML/JS/CSS in production
- **jekyll-paginate-v2** — Blog pagination
- **jekyll-archives** — Tag/category archive pages

## Content Patterns

### Adding a Blog Post

Create `_posts/YYYY-MM-DD-slug.md` with front matter:
```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD HH:MM:SS -0500
tags: [tag1, tag2]
---
```

### Adding a Project

Create `_projects/N_name.md` with front matter including `title`, `description`, `img`, `importance`, `category`.

### Publications

Add BibTeX entries to `_bibliography/papers.bib`. The `_pages/publications.md` page renders them via jekyll-scholar.

### CV

Structured data lives in `_data/cv.yml`. The CV page at `_pages/cv.md` uses `layout: cv`.
