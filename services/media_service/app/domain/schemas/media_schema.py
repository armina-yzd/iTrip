from pydantic import BaseModel
from datetime import datetime

class MediaBase(BaseModel):
    filename: str
    content_type: str
    size: int

class MediaCreate(MediaBase):
    owner_id: str

class MediaResponse(MediaBase):
    id: str

class MediaDetails(MediaResponse):
    upload_date: datetime
    owner_id: str
    metadata: dict = {}