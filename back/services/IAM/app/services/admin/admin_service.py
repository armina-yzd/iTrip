from typing import Annotated
from fastapi import Depends

from app.domain.models.admin import Admin
from app.infrastructure.repositories.admin_repo import AdminRepository

class AdminService():
    def __init__(
        self,
        admin_repository: Annotated[AdminRepository, Depends()]
    ) -> None:
        super().__init__()
        self.admin_repository = admin_repository


    async def get_admin_by_email(self, email: str) -> Admin:
        return self.admin_repository.get_admin_by_email(email)
    