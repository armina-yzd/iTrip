from app.services.media_services import MediaService
from app.infrastructure.repositories.mongodb_repository import MongoDBMediaRepository
from app.core.config import get_mongo_client, settings
from fastapi import Depends

async def get_media_service() -> MediaService:
    client = get_mongo_client()
    repository = MongoDBMediaRepository(client, settings.mongo_db_name)
    return MediaService(repository)