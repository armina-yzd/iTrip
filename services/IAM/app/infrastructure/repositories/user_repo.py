from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.user import User

class UserRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()
    
    def get_banned_user(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email, User.is_banned).first()
    
    def change_user_wallet(self, id: int, new_wallet: int) -> User:
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            user.wallet = new_wallet
            self.db.commit()
            self.db.refresh(user)
        return user

    