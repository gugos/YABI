from pydantic import BaseModel
from datetime import datetime


class HealthCheckResponse(BaseModel):
    status: str
    message: str
    timestamp: datetime
    version: str
    service: str
