from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.bus_service import BusService

class BusServiceRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def add_bus_service(self, service: BusService) -> BusService:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service

    # def get_user_by_email(self, email: str) -> User:
    #     return self.db.query(User).filter(User.email == email).first()
    
    # def get_user_by_username(self, username: str) -> User:
    #     return self.db.query(User).filter(User.username == username).first()
    
    # def get_banned_user(self, email: str) -> User:
    #     return self.db.query(User).filter(User.email == email, User.is_banned).first()