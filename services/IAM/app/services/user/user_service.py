from typing import Annotated, Dict
from fastapi import Depends, HTTPException,status

from app.domain.models.user import User
from app.domain.schemas.user_schema import VerifyOtp
from app.infrastructure.repositories.user_repo import UserRepository
from app.services.auth.hash import HashPassword

class UserService():
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        hash_password: Annotated[HashPassword, Depends()],
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.hash_password = hash_password

    async def create_user(self, user: VerifyOtp) -> User:
        return self.user_repository.create_user(
            User(
                username=user.username,
                email=user.email,
                password=self.hash_password.get_password_hash(user.password),
            )
        )


    async def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)
    
    async def get_user_by_username(self, username: str) -> User:
        return self.user_repository.get_user_by_username(username)
    
    async def get_banned_user(self, email: str) -> User:
        return self.user_repository.get_banned_user(email)
    
    async def get_users_admin(self) -> list[User]:
        return self.user_repository.get_users_admin()
    
    async def ban_user_admin(self,email: str) -> list[User]:
        user = await self.get_user_by_email(email)
        return self.user_repository.ban_user_admin(user)
    
    async def unban_user_admin(self,email: str) -> list[User]:
        user = await self.get_user_by_email(email)
        return self.user_repository.unban_user_admin(user)
    
    async def change_user_wallet(self, id:int, new_wallet:int) -> User:
        if new_wallet<0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="wallet cant be less than zero"
            )
        return self.user_repository.change_user_wallet(id,new_wallet)