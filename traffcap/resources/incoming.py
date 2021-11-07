from typing import Callable
from fastapi import (
    APIRouter,
    Request
)
from fastapi.responses import (
    JSONResponse,
    RedirectResponse
)
from traffcap.repositories import (
    EndpointRepository,
    InboundRequestRepository
)


INCOMING_PREFIX = "r"
incoming_router = APIRouter(prefix=f"/{INCOMING_PREFIX}", tags=["HTTP Capture"])


def check_endpoint_code(func: Callable) -> Callable:
    """
    Check to see if the endpoint ID is in the database
    """
    async def do_check(endpoint_code: str, request: Request) -> JSONResponse:
        endpoint = await EndpointRepository.get_endpoint(endpoint_code)
        if not endpoint:
            return JSONResponse(
                {"reply": "endpoint id not found"},
                status_code=404
            )

        return await func(endpoint_code, request)
    return do_check


@incoming_router.get("/", include_in_schema=False)
async def spa_redirect() -> RedirectResponse:
    """
    If we hit this router without a endpoint ID, redirect to root
    """
    return RedirectResponse("/")


@incoming_router.get("/{endpoint_code}")
@check_endpoint_code
async def record_get(endpoint_code: str, request: Request) -> JSONResponse:
    """
    GET on the endpoint
    1. Check to see if the endpoint ID is in the DB (tick)
    2. Return 404 if it's not found (tick)
    3. Record the endpoint information
    4. Send out notifications if required
    5. Send back any required response
    """
    # Record everything from the request
    # * HTTP
    # * Headers
    # * Body
    # Send notifications
    # Return a response
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({"endpoint_code": endpoint_code})


@incoming_router.post("/{endpoint_code}")
@check_endpoint_code
async def record_post(endpoint_code: str, request: Request) -> JSONResponse:
    """
    POST on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({"endpoint_code": endpoint_code})


@incoming_router.put("/{endpoint_code}")
@check_endpoint_code
async def record_put(endpoint_code: str, request: Request) -> JSONResponse:
    """
    PUT on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({})


@incoming_router.patch("/{endpoint_code}")
@check_endpoint_code
async def record_patch(endpoint_code: str, request: Request) -> JSONResponse:
    """
    PATCH on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({})


@incoming_router.delete("/{endpoint_code}")
@check_endpoint_code
async def delete(endpoint_code: str, request: Request) -> JSONResponse:
    """
    DELETE on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({})


@incoming_router.options("/{endpoint_code}")
@check_endpoint_code
async def record_options(endpoint_code: str, request: Request) -> JSONResponse:
    """
    OPTIONS on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({})


@incoming_router.trace("/{endpoint_code}")
@check_endpoint_code
async def record_trace(endpoint_code: str, request: Request) -> JSONResponse:
    """
    TRACE on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({})


@incoming_router.head("/{endpoint_code}")
@check_endpoint_code
async def record_head(endpoint_code: str, request: Request) -> JSONResponse:
    """
    HEAD on the endpoint
    """
    await InboundRequestRepository.save_request(endpoint_code, request)
    return JSONResponse({})
