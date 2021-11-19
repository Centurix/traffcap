import asyncio
from typing import (
    List,
    Dict
)
from fastapi import (
    APIRouter,
    HTTPException,
    WebSocket
)
from traffcap.endpoints import generate_code
from traffcap.repositories import EndpointRepository
from traffcap.libs.pydantic_jsonapi import JsonApiModel  # Factory
from traffcap.dto.endpoint import Endpoint
from time import sleep


endpoints_router = APIRouter(prefix="/endpoints", tags=["Endpoint Management"])
EndpointRequest, EndpointResponse = JsonApiModel("endpoints", Endpoint)
EndpointRequestList, EndpointResponseList = JsonApiModel("endpoints", Endpoint, list_response=True)


@endpoints_router.get("/", response_model=EndpointResponseList)
async def get_all_endpoints() -> List[Dict[str, object]]:
    """
    Return endpoints from the database
    """
    endpoints = await EndpointRepository.list_endpoints()

    return EndpointResponseList(
        data=[EndpointResponseList.resource_object(
            id=endpoint.code,
            attributes=endpoint
        ) for endpoint in endpoints]
    )

@endpoints_router.get("/{endpoint_code}")
async def get_endpoint(endpoint_code: str) -> EndpointResponse:
    endpoint = await EndpointRepository.get_endpoint(endpoint_code)

    if not endpoint:
        # Raise a 404
        raise HTTPException(status_code=404, detail="Endpoint not found")

    return EndpointResponse(
        data=EndpointResponse.resource_object(
            id=endpoint.code,
            attributes=endpoint
        )
    )

@endpoints_router.post("/")
async def create_endpoint() -> EndpointResponse:
    """
    Create an endpoint
    """
    endpoint_code = await generate_code()
    endpoint = await EndpointRepository.create_new_endpoint(endpoint_code)

    return EndpointResponse(
        data=EndpointResponse.resource_object(
            id=endpoint.code,
            attributes=endpoint
        )
    )

@endpoints_router.websocket("/requests/{endpoint_code}/ws")
async def websocket_endpoint(websocket: WebSocket, endpoint_code: str):
    """
    Send messages to the client for the nominated endpoint
    """
    await websocket.accept()

    while True:
        # Find new messages and send them on
        await asyncio.sleep(5)
        await websocket.send_text("New message!")
