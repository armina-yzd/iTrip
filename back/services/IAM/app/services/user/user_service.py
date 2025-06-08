from typing import Annotated, Dict
from fastapi import Depends

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