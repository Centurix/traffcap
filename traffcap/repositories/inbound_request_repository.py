from typing import (
    List,
    Optional
)
from .repository import Repository
from fastapi import Request
from traffcap.dto import InboundRequest
from datetime import datetime


class InboundRequestRepository(Repository):
    @classmethod
    async def save_request(cls, code: str, request: Request) -> None:
        # HTTP information
        # * method
        # * Base URL
        # * Headers
        inbound_request = await InboundRequest.from_request(code, request)

        await cls.execute(f"""
INSERT INTO requests (
    code,
    created,
    modified,
    scope,
    body
) VALUES (
    ?,
    datetime('now'),
    datetime('now'),
    ?,
    ?
)
""",
    (
        code,
        inbound_request.scope,
        inbound_request.body
    ))

    @classmethod
    async def list_requests(cls) -> Optional[List[InboundRequest]]:
        return await cls.execute(
            """
SELECT
    id,
    code,
    created,
    modified,
    scope,
    body
FROM
    requests
""",
            row_factory=InboundRequest
        )

    @classmethod
    async def list_requests_by_endpoint_code(cls, endpoint_code: str) -> Optional[List[InboundRequest]]:
        return await cls.execute(
            """
SELECT
    id,
    code,
    created,
    modified,
    scope,
    body
FROM
    requests
WHERE
    code = ?
""",
            (endpoint_code,),
            row_factory=InboundRequest
        )

    @classmethod
    async def list_latest_requests_by_endpoint_code(cls, endpoint_code: str, last_request: datetime) -> Optional[List[InboundRequest]]:
        if not last_request:  # Send back everything
            return await cls.list_requests_by_endpoint_code(endpoint_code)

        return await cls.execute("""
SELECT
    id,
    code,
    created,
    modified,
    scope,
    body
FROM
    requests
WHERE
    code = ? AND
    created > ?
""",
            (endpoint_code, last_request),
            row_factory=InboundRequest
        )
