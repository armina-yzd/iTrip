from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from bson import ObjectId

class MediaFile(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    filename: str
    content_type: str
    size: int
    upload_date: datetime = Field(default_factory=datetime.utcnow)
    # blog_id: int
    metadata: dict = {}

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}