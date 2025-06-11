from typing import Annotated, Dict
from fastapi import Depends

from app.domain.models.company import Company
from app.domain.schemas.company_schema import VerifyOtp
from app.infrastructure.repositories.company_repo import CompanyRepository
from app.services.auth.hash import HashPassword

class CompanyService():
    def __init__(
        self,
        company_repository: Annotated[CompanyRepository, Depends()],
        hash_password: Annotated[HashPassword, Depends()],
    ) -> None:
        super().__init__()
        self.company_repository = company_repository
        self.hash_password = hash_password

    async def create_company(self, company: VerifyOtp) -> Company:
        return self.company_repository.create_company(
            Company(
                name=company.name,
                email=company.email,
                password=self.hash_password.get_password_hash(company.password),
            )
        )

    async def get_company_by_email(self, email: str) -> Company:
        return self.company_repository.get_company_by_email(email)
    
    async def get_company_name(self, id: int) -> Company:
        return self.company_repository.get_company_name(id)
    
    async def get_company_by_name(self, name: str) -> Company:
        return self.company_repository.get_company_by_name(name)

    async def get_banned_company(self, email: str) -> Company:
        return self.company_repository.get_banned_company(email)

    async def get_verified_company(self, email: str) -> Company:
        return self.company_repository.get_verified_company(email)
    