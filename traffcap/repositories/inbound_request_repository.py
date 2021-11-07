from .repository import Repository
from fastapi import Request
from traffcap.dto import InboundRequest


class InboundRequestRepository(Repository):
    @classmethod
    async def save_request(cls, code: str, request: Request) -> None:
        # HTTP information
        # * method
        # * Base URL
        # * Headers
        inbound_request = await InboundRequest.from_request(code, request)

        test = inbound_request.scope.json()

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
        inbound_request.scope.json(),
        inbound_request.body
    ))
