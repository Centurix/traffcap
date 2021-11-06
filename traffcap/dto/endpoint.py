from .row_factory import RowFactory
from pydantic import BaseModel
from datetime import datetime


class Endpoint(BaseModel, RowFactory):
    code: str
    created: datetime
    modified: datetime
    description: str = ""
