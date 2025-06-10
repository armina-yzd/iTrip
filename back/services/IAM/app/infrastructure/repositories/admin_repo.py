from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.admin import Admin

class AdminRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def get_admin_by_email(self, email: str) -> Admin:
        return self.db.query(Admin).filter(Admin.email == email).first()
    