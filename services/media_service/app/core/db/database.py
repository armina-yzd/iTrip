from app.services.media_services import MediaService
from app.infrastructure.repositories.mongodb_repository import MongoDBMediaRepository
from app.core.config import get_mongo_client, settings
from fastapi import Depends

from app.infrastructure.clients.user_ticket_client import UTClient

async def get_media_service( ut_client: UTClient = Depends()) -> MediaService:
    client = get_mongo_client()
    repository = MongoDBMediaRepository(client, settings.mongo_db_name)
    return MediaService(media_repository=repository, ut_client=ut_client)