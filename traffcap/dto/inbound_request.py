from typing import (
    Optional,
    TypeVar
)
from .row_factory import RowFactory
from pydantic import BaseModel
from datetime import datetime
from fastapi import Request
from fastapi.encoders import jsonable_encoder
import json


class InboundRequest(BaseModel, RowFactory):
    id: Optional[int]
    code: str
    created: datetime = None
    modified: datetime = None
    scope: str = None
    body: bytes = None

    @classmethod
    async def from_request(cls, code: str, request: Request) -> TypeVar("T", bound="InboundRequest"):
        scope_data = {
            "http_version": request.scope.get("http_version", ""),
            "scheme": request.scope.get("scheme", ""),
            "method": request.scope.get("method", ""),
            "root_path": request.scope.get("root_path", ""),
            "path": request.scope.get("path", ""),
            "server": request.scope.get("server", ""),
            "client": request.scope.get("client", ""),
            "headers": request.scope.get("headers", ""),
            "path_params": request.scope.get("path_params", ""),
            "query_string": request.scope.get("query_string", "")
        }
        return cls(
            code=code,
            scope=json.dumps(jsonable_encoder(scope_data)),
            body=await request.body()
        )
