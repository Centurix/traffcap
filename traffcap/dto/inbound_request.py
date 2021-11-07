from typing import (
    Optional,
    TypeVar
)
from .row_factory import RowFactory
from pydantic import BaseModel
from .scope import Scope
from datetime import datetime
from fastapi import Request
from traffcap.dto import Scope


class InboundRequest(BaseModel, RowFactory):
    id: Optional[int]
    code: str
    created: datetime = None
    modified: datetime = None
    scope: Scope = None
    body: bytes = None

    @classmethod
    async def from_request(cls, code: str, request: Request) -> TypeVar("T", bound="InboundRequest"):
        return cls(
            code=code,
            scope=Scope(**request.scope),
            body=await request.body()
        )
