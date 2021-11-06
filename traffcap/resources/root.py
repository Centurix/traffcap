import os
from fastapi import APIRouter
from fastapi.responses import (
    Response,
    FileResponse
)
from fastapi import Request
"""
Deal with SPA static files, return:
* index.html
* favicon.ico
* css/*
* img/*
* js/*
Without blocking the rest of the API
"""

SPA_FOLDER = os.path.join("tcspa", "dist")
root_router = APIRouter(include_in_schema=False)


async def return_file_contents(folder: str, filename: str):
    # check first if requested file exists
    file = os.path.join(SPA_FOLDER, folder, filename)

    if os.path.exists(file):
        return FileResponse(file)

    # otherwise return index files
    return Response("Not found", status_code=404)

@root_router.get("/")
async def get_spa() -> Response:
    return FileResponse(os.path.join(SPA_FOLDER, 'index.html'))

@root_router.get("/favicon.ico")
async def get_favicon() -> Response:
    return FileResponse(os.path.join(SPA_FOLDER, 'favicon.ico'))

@root_router.get("/css/{catchall:path}", response_class=FileResponse)
async def read_css(request: Request) -> Response:
    return await return_file_contents("css", request.path_params["catchall"])

@root_router.get("/img/{catchall:path}", response_class=FileResponse)
async def read_img(request: Request) -> Response:
    return await return_file_contents("img", request.path_params["catchall"])

@root_router.get("/js/{catchall:path}", response_class=FileResponse)
async def read_js(request: Request) -> Response:
    return await return_file_contents("js", request.path_params["catchall"])
