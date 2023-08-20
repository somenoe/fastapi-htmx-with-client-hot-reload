import arel
from pathlib import Path
from decouple import config
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time

app = FastAPI()
templates = Jinja2Templates("./templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

BASE_DIR = Path(__file__).parent


async def delay_before_reload() -> None:
    time.sleep(0.3)


if _debug := config("DEBUG", cast=bool, default=False):
    hot_reload = arel.HotReload(paths=[
        arel.Path(BASE_DIR/"templates", on_reload=[
            delay_before_reload
        ]),
        arel.Path(BASE_DIR/"static", on_reload=[
            delay_before_reload
        ]),
    ])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = _debug
    templates.env.globals["hot_reload"] = hot_reload


@app.get("/")
def index(request: Request):
    context = {
        "request": request,
        "title": "Home"
    }
    return templates.TemplateResponse("index.html", context=context)


@app.get("/form")
def index(request: Request):
    return templates.TemplateResponse("form.html", context={"request": request})
