from typing import List
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

        # Upload the file to GridFS with metadata
        file_id = await self.fs.upload_from_stream(
            media.filename,
            file_data,
            metadata=metadata
        )

        # Convert the file_id to string and update the media object
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
                ticket_id=metadata["ticket_id"], 
                metadata=metadata.get("metadata", {})
            )
            return media, file_data
        except Exception as e:
            raise FileNotFoundError(f"File with id {file_id} not found")
    
    async def delete(self, file_id: str) -> bool:
        try:
            await self.fs.delete(ObjectId(file_id))
            return True
        except:
            return False
        
    async def get_by_ticket_id(self, ticket_id: int) -> List[MediaFile]:
        try:
            cursor = self.db.fs.files.find({"metadata.ticket_id": ticket_id})
            media_files = []
    
            async for document in cursor:
                media = MediaFile(
                    _id=str(document["_id"]),  # Explicitly set _id
                    filename=document["filename"],
                    content_type=document["metadata"]["content_type"],
                    size=document["length"],
                    upload_date=document["metadata"]["upload_date"],
                    ticket_id=document["metadata"]["ticket_id"],
                    metadata=document["metadata"].get("metadata", {})
                )
                media_files.append(media)
    
            return media_files
        except Exception as e:
            print(f"Error getting media by ticket_id {ticket_id}: {str(e)}")
            raise