#!/usr/bin/env python3
"""
The Legend of the Sonzo Dragon

Copyright [2025] David C. Brown

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#from database import connections
from models import explorer

from contextlib import asynccontextmanager
from os.path import join, exists
from pathlib import Path
import json
import logging.config
from pythonjsonlogger import jsonlogger
from typing import AsyncGenerator

# Read logging.json configuration file and apply it to the logger.
with open("logging.json", "r") as f:
    logging_config = json.load(f)
    logging.config.dictConfig(config=logging_config)

logger = logging.getLogger("main")
#logger.setLevel(logging.DEBUG)
logger.info("Starting Server Legend of the Sonzo Dragon.")

app = FastAPI()

# Including Sub-Routers
app.include_router(explorer.router)

# Mounting Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuring Jinja2 Template Engine for HTML Rendering
top = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=join(f"{top}", "templates"))


@app.get("/")
async def home():
    """
    Renders the home page using Jinja2 template engine.

    :return:\n
    """
    logger.info("Rendering Home Page.")
    return {"message": "Welcome to The Legend of the Sonzo Dragon!"}


@app.get("/license")
async def get_license(request: Request) -> HTMLResponse:
    """
    Renders the license page using Jinja2 template engine.

    :param request:\n
    :return:\n
    """
    logger.info("Rendering License Page.")
    return templates.TemplateResponse(request=request, name="license.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9001, reload=True)