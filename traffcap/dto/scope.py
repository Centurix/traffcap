from typing import (
    Tuple,
    List,
    Dict
)
from pydantic import BaseModel


class Scope(BaseModel):
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
