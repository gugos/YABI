from pydantic import BaseModel
from datetime import datetime


class FilterFieldsRequest(BaseModel):
    field_list: list = []
