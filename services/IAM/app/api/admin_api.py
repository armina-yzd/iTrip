from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.models.admin import Admin
from app.domain.schemas.admin_schema import (
    AdminLogIn,
    AdminResponse,
    AdminCreate
)
from app.domain.schemas.token_schema import Token
from app.core.db.database import get_db
from app.services.auth.auth import AuthService , get_current_admin
from app.services.auth.hash import HashPassword

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
):
    return await auth_service.authenticate_admin(
        AdminLogIn(email=form_data.username, password=form_data.password)
    )

@router.get("/me", response_model=AdminResponse)
async def get_me(user: Admin = Depends(get_current_admin)):
    return user

# create admin
@router.post("/admin/", response_model=AdminResponse)
def create_admin(
    user: AdminCreate, 
    hash_service: Annotated[HashPassword, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    admin_data = user.dict()
    hashed_password = hash_service.get_password_hash(admin_data.pop('password'))

    db_admin = Admin(
        **admin_data,
        password = hashed_password 
    )
    
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin