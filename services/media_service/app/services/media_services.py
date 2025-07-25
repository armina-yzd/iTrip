from app.domain.models.media import MediaFile
from app.infrastructure.repositories.media_repo import MediaRepository
from typing import Tuple

class MediaService:
    def __init__(self, repository: MediaRepository):
        self.repository = repository
    
    async def upload_media(self, media: MediaFile, file_data: bytes) -> MediaFile:
        """Upload media file to storage"""
        if not media.filename or not file_data:
            raise ValueError("Filename and file data are required")
        return await self.repository.save(media, file_data)
    
    async def download_media(self, file_id: str) -> Tuple[MediaFile, bytes]:
        """Download media file by ID"""
        if not file_id:
            raise ValueError("File ID is required")
        return await self.repository.get_by_id(file_id)
    
    async def delete_media(self, file_id: str) -> bool:
        """Delete media file by ID"""
        if not file_id:
            raise ValueError("File ID is required")
        return await self.repository.delete(file_id)