from pydantic import BaseModel
from decouple import config

class Settings(BaseModel):
    DATABASE_URL : str = config("DATABASE_URL")
    IAM_URL : str = config("IAM_URL")
    MANAGE_SERVICES_URL: str = config("MANAGE_SERVICES_URL")

def get_settings() -> Settings:
    return Settings()