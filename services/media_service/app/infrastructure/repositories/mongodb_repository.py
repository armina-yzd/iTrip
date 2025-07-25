from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from bson import ObjectId
from app.domain.models.media import MediaFile
from app.infrastructure.repositories.media_repo import MediaRepository
from datetime import datetime

class MongoDBMediaRepository(MediaRepository):
    def __init__(self, client: AsyncIOMotorClient, db_name: str):
        self.client = client
        self.db = self.client[db_name]
        self.fs = AsyncIOMotorGridFSBucket(self.db)
    
    async def save(self, media: MediaFile, file_data: bytes) -> MediaFile:
        metadata = media.dict(exclude={"id"})
        file_id = await self.fs.upload_from_stream(
            media.filename,
            file_data,
            metadata=metadata
        )
        media.id = str(file_id)
        return media
    
    async def get_by_id(self, file_id: str) -> tuple[MediaFile, bytes]:
        try:
            file_object = await self.fs.open_download_stream(ObjectId(file_id))
            file_data = await file_object.read()
            metadata = file_object.metadata
            media = MediaFile(
                id=file_id,
                filename=metadata["filename"],
                content_type=metadata["content_type"],
                size=metadata["size"],
                upload_date=metadata["upload_date"],
                owner_id=metadata.get("owner_id"),
                metadata=metadata.get("metadata")
            )
            return media, file_data
        except:
            raise FileNotFoundError(f"File with id {file_id} not found")
    
    async def delete(self, file_id: str) -> bool:
        try:
            await self.fs.delete(ObjectId(file_id))
            return True
        except:
            return False