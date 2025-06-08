from typing import Annotated
from fastapi import Depends, HTTPException, status

from app.domain.schemas.user_schema import (
    UserCreate,
    UserOtp,
    UserResponseOtp,
    VerifyOtp,
    VerifyOtpResponse
)
from app.services.auth import AuthService
from app.services.otp import OTPService
from app.services.base import BaseService
from app.services.user_service import UserService


class RegisterService(BaseService):
    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
        auth_service: Annotated[AuthService, Depends()],
    ) -> None:
        super().__init__()
        self.user_service = user_service
        self.otp_service = otp_service
        self.auth_service = auth_service

    async def user_otp(self, user: UserOtp) -> UserResponseOtp:
        existing_email = await self.user_service.get_user_by_email(user.email)
        existing_username = await self.user_service.get_user_by_username(user.username)
        
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="User already exists"
            )
        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Username already exists"
            )
        
        user_data = {
            'username': user.username,
            'email': user.email,
            'password': user.password
        }
        otp = self.otp_service.send_otp(user.email, user_data)

        return UserResponseOtp(
            email=user.email,
            message="OTP Send",
        )

    async def verify_user(self, verify_user: VerifyOtp) -> VerifyOtpResponse:
        if not self.otp_service.verify_otp(verify_user.email, verify_user.otp):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Invalid Input"
            )
        
        user_data = self.otp_service.get_user_data(verify_user.email)
        if not user_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="OTP expired or invalid"
            )
        
        await self.user_service.create_user(
            UserCreate(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
        )
        
        return VerifyOtpResponse(
            verify=True, 
            message="User verified"
        )