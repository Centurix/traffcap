from .repository import Repository
from fastapi import Request
from traffcap.dto import Scope


class RequestRepository(Repository):
    @classmethod
    async def save_request(cls, code: str, request: Request) -> None:
        # HTTP information
        # * method
        # * Base URL
        # * Headers
        scope = Scope(**request.scope)

        # Now deal with the body
        body = await request.body()

        # Serialize and store
        print(scope)
        print(body)

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
""", (code,str(scope.json()),body))
