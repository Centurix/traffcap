from fastapi import FastAPI
from fastapi.responses import JSONResponse
from traffcap.resources import routers
from traffcap.service_providers import start_service_providers
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
"""
Traffcap
========

A Requestbin like application using FastAPI
* SQLite database for storing endpoints and traffic
* Frontend for managing endpoints and traffic
* A variety of notification mechanisms
"""


description = """
Traffcap API provides a REST interface to the endpoints and recorded traffic
that Traffcap captures.
"""

openapi_tags = [
    {
        "name": "HTTP Capture",
        "description": "Requests made to these endpoints are recorded"
    },
    {
        "name": "Endpoint Management",
        "description": "Manage the collection of endpoints"
    }
]

app = FastAPI(
    title="Traffcap API",
    description=description,
    version="1.0.0",
    contact={
        "name": "Chris Read",
        "email": "centurix@gmail.com"
    },
    openapi_tags=openapi_tags
)


@app.on_event("startup")
async def startup() -> None:
    await start_service_providers()

# Register all routes for resources
for route in routers:
    app.include_router(route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        content={
            "errors": [{
                "status": exc.status_code,
                "detail": exc.detail
            }]
        }
    )
