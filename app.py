"""Run locally:  uvicorn app:app --reload  ->  http://127.0.0.1:8000"""
from datetime import date
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import content

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Bhuvaneshwari M — Portfolio", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")
templates.env.globals["static"] = lambda path: f"/static/{path}"
templates.env.globals["year"] = date.today().year


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", content.context())


@app.get("/healthz")
def health():
    return {"status": "ok"}
