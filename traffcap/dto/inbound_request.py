from typing import (
    Tuple,
    List,
    Dict,
    Optional,
    TypeVar
)
from .row_factory import RowFactory
from pydantic import BaseModel
from datetime import datetime
from fastapi import Request
from traffcap.dto import Scope


class InboundRequest(BaseModel, RowFactory):
    id: Optional[int]
    code: str
    created: datetime = None
    modified: datetime = None
    http_version: str
    scheme: str
    method: str
    root_path: str
    path: str
    server: Tuple
    client: Tuple
    headers: List[Tuple]
    path_params: Dict
    query_string: str
    body: bytes = None

    @classmethod
    async def from_request(cls, code: str, request: Request) -> TypeVar("T", bound="InboundRequest"):
        return cls(
            code=code,
            http_version=request.scope.http_version,
            scheme=request.scope.scheme,
            method=request.scope.method,
            root_path=request.scope.root_path,
            path=request.scope.path,
            server=request.scope.server,
            client=request.scope.client,
            headers=request.scope.headers,
            path_params=request.scope.path_params,
            query_string=request.scope.query_string,
            body=await request.body()
        )
