from abc import ABC, abstractmethod
from typing import List
from app.domain.models.media import MediaFile

class MediaRepository(ABC):
    @abstractmethod
    async def save(self, media: MediaFile, file_data: bytes) -> MediaFile:
        pass
    
    @abstractmethod
    async def get_by_id(self, file_id: str) -> tuple[MediaFile, bytes]:
        pass
    
    @abstractmethod
    async def delete(self, file_id: str) -> bool:
        pass

    @abstractmethod
    async def get_by_ticket_id(self, ticket_id: int) -> List[MediaFile]:
        pass