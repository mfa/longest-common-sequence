from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .algorithm import get_longest_common_sequence

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


class Item(BaseModel):
    positives: list
    negatives: list
    cut_off: int = 3


@app.post("/")
async def lcs(item: Item) -> set[str]:
    # filter empty strings from both lists
    positives = list(filter(None, item.positives))
    negatives = list(filter(None, item.negatives))
    print(positives)
    print(negatives)
    return get_longest_common_sequence(positives, negatives, item.cut_off)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
