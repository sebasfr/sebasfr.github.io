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

The site uses significant customizations over the default al-folio theme:

**Typography** (`_sass/_base.scss`):

- Global font is **Playfair Display** (serif), loaded from Google Fonts.
- `Playfair Display SC` (small caps variant) is used for badges and tags.
- Both variants are imported at the top of `_base.scss`.

**Color Themes** (`_sass/_variables.scss` + `_sass/_themes.scss`):

Five named themes are defined in `_variables.scss`, each with full light and dark mode palettes:

| Theme | Light accent | Dark accent | Aesthetic |
| --- | --- | --- | --- |
| `econometrician` | Economist Red `#e3120b` | Bright Red `#ff4d46` | Teal/data-focused |
| `journal` | Black `#000000` | White `#ffffff` | Monochrome print |
| `ledger` | Oxblood `#9e2a2b` | Coral `#ff8a80` | Warm financial |
| `algo` | Electric Indigo `#4f46e5` | Soft Indigo `#818cf8` | FinTech/modern |
| `vintage` | Burnt Orange `#c2410c` | Muted Orange `#fb923c` | Warm cream/beige |

**Active theme: `vintage`** — `_themes.scss` maps the `vintage-*` SCSS variables to the global CSS custom properties (`--global-bg-color`, `--global-theme-color`, etc.) for both `:root` (light) and `html[data-theme="dark"]`.

To switch themes, replace all `$vintage-*` references in `_themes.scss` with the corresponding `$<theme-name>-*` variables. All theme palettes are already defined in `_variables.scss`.

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
