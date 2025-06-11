from pydantic import BaseModel
from decouple import config

class Settings(BaseModel):
    DATABASE_URL : str = config("DATABASE_URL")
    IAM_URL : str = config("IAM_URL")
    USER_TICKET_URL : str = config("USER_TICKET_URL")

def get_settings() -> Settings:
    return Settings()