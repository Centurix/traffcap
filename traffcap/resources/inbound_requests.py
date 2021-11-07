from typing import (
    List,
    Dict
)
from fastapi import (
    APIRouter,
    HTTPException
)
from traffcap.repositories import InboundRequestRepository
from traffcap.libs.pydantic_jsonapi import JsonApiModel  # Factory
from traffcap.dto import InboundRequest


inbound_requests_router = APIRouter(prefix="/requests", tags=["Inbound Requests Management"])

InboundRequestRequest, InboundRequestResponse = JsonApiModel("requests", InboundRequest)
InboundRequestRequestList, InboundRequestResponseList = JsonApiModel("requests", InboundRequest, list_response=True)


@inbound_requests_router.get("/", response_model=InboundRequestResponseList)
async def get_all_requests() -> List[Dict[str, object]]:
    """
    Return requests from the database
    """
    inbound_requests = await InboundRequestRepository.list_requests()

    return InboundRequestResponseList(
        data=[InboundRequestResponseList.resource_object(
            id=inbound_request.id,
            attributes=inbound_request
        ) for inbound_request in inbound_requests]
    )
