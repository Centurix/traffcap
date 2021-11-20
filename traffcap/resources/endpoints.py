from typing import (
    List,
    Dict
)
from fastapi import (
    APIRouter,
    HTTPException,
    WebSocket
)
from fastapi.encoders import jsonable_encoder
from traffcap.endpoints import generate_code
from traffcap.repositories import EndpointRepository
from traffcap.libs.pydantic_jsonapi import JsonApiModel  # Factory
from traffcap.dto import (
    Endpoint,
    InboundRequest
)
from asyncio import sleep
from traffcap.repositories.inbound_request_repository import InboundRequestRepository
from websockets.exceptions import (
    ConnectionClosedError,
    ConnectionClosedOK
)


POLL_TIME = 5


endpoints_router = APIRouter(prefix="/endpoints", tags=["Endpoint Management"])
EndpointRequest, EndpointResponse = JsonApiModel("endpoints", Endpoint)
EndpointRequestList, EndpointResponseList = JsonApiModel("endpoints", Endpoint, list_response=True)
_, InboundRequestResponse = JsonApiModel("requests", InboundRequest)
_, InboundRequestResponseList = JsonApiModel("requests", InboundRequest, list_response=True)


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
    try:
        await websocket.accept()

        last_request = None

        # Sit in a loop waiting for messages
        while True:
            inbound_requests = await InboundRequestRepository.list_latest_requests_by_endpoint_code(endpoint_code, last_request)

            # Now send the results back to the consumer
            await websocket.send_json(
                jsonable_encoder(InboundRequestResponseList(
                    data=[InboundRequestResponseList.resource_object(
                        id=inbound_request.id,
                        attributes=inbound_request
                    ) for inbound_request in inbound_requests]
                )
            ))

            # Fetch the date/time of the last request
            if inbound_requests:
                # datetime from the last request
                last_request = inbound_requests[-1].created

            await sleep(POLL_TIME)
    except (ConnectionClosedError, ConnectionClosedOK):
        pass  # This is hit when a connection is closed
