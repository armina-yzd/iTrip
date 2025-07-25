from pydantic import BaseModel
from decouple import config

class Settings(BaseModel):
    DATABASE_URL : str = config("DATABASE_URL")
    REDIS_URL: str = config("REDIS_URL", default="redis://redis:6379/0")

def get_settings() -> Settings:
    return Settings()