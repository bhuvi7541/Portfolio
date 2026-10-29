"""Export the site as plain static files (for Netlify / GitHub Pages / Vercel).

    python build.py      ->  dist/index.html + dist/static/...
"""
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content

BASE_DIR = Path(__file__).resolve().parent
DIST = BASE_DIR / "dist"

env = Environment(loader=FileSystemLoader(BASE_DIR / "templates"), autoescape=select_autoescape())
env.globals["static"] = lambda path: f"static/{path}"
env.globals["year"] = date.today().year

if DIST.exists():
    shutil.rmtree(DIST)
shutil.copytree(BASE_DIR / "static", DIST / "static")
(DIST / "index.html").write_text(env.get_template("index.html").render(**content.context()), encoding="utf-8")
print(f"Built -> {DIST / 'index.html'}")
