from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent.parent.parent / ".env")

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

def get_settings() -> Settings:
    return Settings()