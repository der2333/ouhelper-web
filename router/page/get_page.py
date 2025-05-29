from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

get_page = APIRouter()

templates = Jinja2Templates(directory="templates")


@get_page.get("/")
async def get_index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@get_page.get("/xuanke")
async def get_xuanke_page(request: Request):
    return templates.TemplateResponse("xuanke.html", {"request": request})
