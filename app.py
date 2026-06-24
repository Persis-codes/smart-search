import indexer
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from search import search_files

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "results": []
        }
    )


@app.get("/search")
async def search(request: Request, query: str):

    results = search_files(query)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "results": results,
            "query": query
        }
    )