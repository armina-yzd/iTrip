from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

class Settings(BaseSettings):
    mongo_url: str = "mongodb://mongo:27017"
    mongo_db_name: str = "Itrip"
    file_storage_path: str = "app/media"
    IAM_URL : str = config("IAM_URL")
    USER_TICKET_URL : str = config("USER_TICKET_URL")
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()

def get_mongo_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(settings.mongo_url)

def get_settings() -> Settings:
    return settings