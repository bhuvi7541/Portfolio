# Bhuvaneshwari M — Portfolio

A clean, professional portfolio built with FastAPI, Jinja2 templates, plain CSS and vanilla JS, with no build tools and no frontend frameworks. Light and dark themes included.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
# open http://127.0.0.1:8000
```

## Export as a static site (Netlify / GitHub Pages / Vercel)

```bash
python build.py        # writes dist/index.html + dist/static/
```

Drag `dist/` onto Netlify, or push it to a `gh-pages` branch.

## Editing content

All text, projects, skills and links are in **`content.py`**, so you never need to touch HTML to update the site.

- New project: add a dict to `PROJECTS`. Projects with `images` (real screenshots in `static/img/`) are shown large with a screenshot viewer; projects without images are shown as text cards. `in_progress: True` adds an "In progress" badge.
- Hero carousel: edit `SHOWCASE`.
- New skill: add it to the right group in `SKILLS`.
- New job: add an entry at the top of `EXPERIENCE`.
- Résumé: replace `static/files/Bhuvaneshwari_M_Resume.pdf`.

## Structure

```
app.py               FastAPI app (serves templates + static)
build.py             static export → dist/
content.py           all site content
templates/
  base.html          layout, fonts, theme bootstrap
  index.html         assembles the sections
  partials/          _header, _hero, _about, _skills, _experience, _projects, _contact, _footer, _macros
static/css/style.css design tokens (light + dark), all styles
static/js/main.js    theme toggle, mobile menu, hero carousel, screenshot viewer, copy email
```
