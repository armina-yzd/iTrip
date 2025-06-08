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
from app.services.auth.auth import AuthService, get_current_admin
from app.services.auth.hash import HashPassword

router = APIRouter()

@router.post("/adminlogin", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
):
    return await auth_service.authenticate_admin(
        AdminLogIn(email=form_data.username, password=form_data.password)
    )

@router.get("/adminme", response_model=AdminResponse)
async def get_me(user: Admin = Depends(get_current_admin)):
    return user

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

# Get all admins
@router.get("/admins/", response_model=List[AdminResponse])
def get_Admins(db: Session = Depends(get_db)):
    return db.query(Admin).all()


# Delete admin
@router.delete("/adminsDel/{admin_id}")
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="admin not found")
    
    db.delete(admin)
    db.commit()
    return {"message": "admin deleted successfully"}