from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from app.core.config import get_settings

config = get_settings() 
DATABASE_URL = config.DATABASE_URL
EntityBase = declarative_base()

engine = create_engine(DATABASE_URL,echo=True)
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def in_db():
    if not database_exists(engine.url):
        create_database(engine.url)
    EntityBase.metadata.create_all(bind=engine)

def get_entitybase():
    return EntityBase

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()