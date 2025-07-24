from fastapi import APIRouter, Depends, HTTPException,status
from typing import Annotated
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from decouple import config

from app.domain.models.user import User
from app.domain.models.admin import Admin
from app.domain.schemas.user_schema import (
    UserResponse,
    UserLogIn,
    UserResponseOtp,
    UserOtp,
    VerifyOtp,
    VerifyOtpResponse,
    WalletUpdateRequest
)
from app.domain.schemas.token_schema import Token
from app.core.db.database import get_db
from app.services.auth.auth import AuthService , get_current_user, get_current_admin
from app.services.user.register_service import RegisterService
from app.services.user.user_service import UserService

router = APIRouter(prefix="/user", tags=["User"])
SECRET : str = config("SECRET")

@router.post("/login", response_model=Token)
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

@router.post("/wallet/{user_id}", response_model=UserResponse)
async def change_wallet(
    user_id: int,
    request: WalletUpdateRequest,
    user_service: Annotated[UserService, Depends()]
    ):
    if request.secret_code != SECRET:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Not Allowed"
        )
    return await user_service.change_user_wallet(user_id,request.new_wallet)

@router.get("/get_users_admin/", response_model=List[UserResponse])
async def get_users(
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    user_service: Annotated[UserService, Depends()]):
    return await user_service.get_users_admin()

@router.post("/ban_user/{user_email}", response_model=UserResponse)
async def ban_user(
    user_email: str,
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    user_service: Annotated[UserService, Depends()]):
    return await user_service.ban_user_admin(user_email)

@router.post("/unban_user/{user_email}", response_model=UserResponse)
async def unban_user(
    user_email: str,
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    user_service: Annotated[UserService, Depends()]):
    return await user_service.unban_user_admin(user_email)