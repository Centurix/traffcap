from typing import (
    List,
    Optional
)
from .repository import Repository
from traffcap.dto import Endpoint


class EndpointRepository(Repository):
    @classmethod
    async def create_new_endpoint(cls, code: str) -> Optional[Endpoint]:
        await cls.execute(f"""
INSERT INTO endpoints (
    code,
    created,
    modified
) VALUES (
    ?,
    datetime('now'),
    datetime('now')
)
""", (code,))
        return await cls.get_endpoint(code)

    @classmethod
    async def list_endpoints(cls) -> Optional[List[Endpoint]]:
        return await cls.execute(
            """
SELECT
    code,
    created,
    modified,
    description
FROM
    endpoints
""",
            row_factory=Endpoint
        )

    @classmethod
    async def get_endpoint(cls, endpoint_code: str) -> Optional[Endpoint]:
        endpoints = await cls.execute(
            f"""
SELECT
    code,
    created,
    modified,
    description
FROM
    endpoints
WHERE code=?
""",
            (endpoint_code,),
            row_factory=Endpoint
        )
        if len(endpoints) == 0:
            return None

        return endpoints[0]