from fastapi import Depends, HTTPException, status
from app.domain.models.media import MediaFile
from app.infrastructure.repositories.media_repo import MediaRepository
from typing import Annotated, List, Tuple

from app.infrastructure.clients.user_ticket_client import UTClient

class MediaService:
    def __init__(
            self, 
            media_repository: MediaRepository,
            ut_client: Annotated[UTClient, Depends()]
            ):
        self.ut_client = ut_client
        self.media_repository = media_repository
    
    async def upload_media(self, media: MediaFile, file_data: bytes,ticket_id: int, user_id: int) -> MediaFile:
        ticket_user:int = await self.ut_client.ticket_user(ticket_id)
        if ticket_user != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to upload photo"
            )
        if not media.filename or not file_data:
            raise ValueError("Filename and file data are required")
        return await self.media_repository.save(media, file_data)
    
    async def download_media(self, file_id: str) -> Tuple[MediaFile, bytes]:
        if not file_id:
            raise ValueError("File ID is required")
        return await self.media_repository.get_by_id(file_id)
    
    async def delete_media(self, file_id: str,ticket_id: int,user_id: int) -> bool:
        ticket_user:int = await self.ut_client.ticket_user(ticket_id)
        if ticket_user != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this file"
            )
        if not file_id:
            raise ValueError("File ID is required")
        return await self.media_repository.delete(file_id)
    
    async def get_media_by_ticket(self, ticket_id: int) -> List[MediaFile]:
        if not ticket_id:
            raise ValueError("Ticket ID is required")
        return await self.media_repository.get_by_ticket_id(ticket_id)