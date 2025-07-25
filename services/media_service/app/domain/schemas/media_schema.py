from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class MediaBase(BaseModel):
    filename: str
    content_type: str
    size: int

class MediaCreate(MediaBase):
    ticket_id: int

class MediaResponse(MediaBase):
    id: str

class MediaDetails(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    filename: str
    content_type: str
    size: int
    upload_date: datetime
    ticket_id: int
    metadata: dict = {}

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}