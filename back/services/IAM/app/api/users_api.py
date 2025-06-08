from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.models.user import User
from app.domain.schemas.user_schema import (
    UserResponse,
    UserCreate,
    UserLogIn,
    UserResponseOtp,
    UserOtp,
    VerifyOtp,
    VerifyOtpResponse
)
from app.domain.schemas.token_schema import Token
from app.core.db.database import get_db
from app.services.auth import AuthService, get_current_user
from app.services.hash import HashPassword
from app.services.register_service import RegisterService

router = APIRouter()

@router.post("/userlogin", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
):
    return await auth_service.authenticate_user(
        UserLogIn(email=form_data.username, password=form_data.password)
    )

@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends(get_current_user)):
    return user

@router.post("/sendOtp/", response_model=UserResponseOtp)
async def send_otp(
    user: UserOtp,  user_otp: Annotated[RegisterService, Depends()]
):
    return await user_otp.user_otp(user)

@router.post("/creatUser/", response_model=VerifyOtpResponse)
async def create_user(
    user: VerifyOtp, 
    verify_user: Annotated[RegisterService, Depends()]
):
    return await verify_user.verify_user(user)

@router.post("/users/", response_model=UserResponse)
def create_user1(
    user: UserCreate, 
    hash_service: Annotated[HashPassword, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    user_data = user.dict()
    hashed_password = hash_service.get_password_hash(user_data.pop('password'))

    db_user = User(
        **user_data,
        password = hashed_password 
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
@router.get("/users/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# Delete a user
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}