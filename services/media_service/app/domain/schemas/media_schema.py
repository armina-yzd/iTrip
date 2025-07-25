from pydantic import BaseModel
from datetime import datetime

class MediaBase(BaseModel):
    filename: str
    content_type: str
    size: int

class MediaCreate(MediaBase):
    ticket_id: int

class MediaResponse(MediaBase):
    id: str

class MediaDetails(MediaResponse):
    upload_date: datetime
    ticket_id: int
    metadata: dict = {}