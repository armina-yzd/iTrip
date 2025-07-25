from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.models.company import Company
from app.domain.schemas.company_schema import (
    CompanyResponse,
    CompanyLogIn,
    CompanyResponseOtp,
    CompanyOtp,
    VerifyOtp,
    VerifyOtpResponse,
    VerifyEmailResponse
)
from app.domain.schemas.token_schema import Token
from app.core.db.database import get_db
from app.services.auth.auth import AuthService, get_current_admin , get_current_company
from app.services.company.company_register import CompanyRegister
from app.services.company.company_service import CompanyService
from app.domain.models.admin import Admin

router = APIRouter(prefix="/company", tags=["Company"])

@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
):
    return await auth_service.authenticate_company(
        CompanyLogIn(email=form_data.username, password=form_data.password)
    )

@router.get("/me", response_model=CompanyResponse)
async def get_me(company: Company = Depends(get_current_company)):
    return company

@router.post("/sendOtp/", response_model=CompanyResponseOtp)
async def send_otp(
    company: CompanyOtp,  company_otp: Annotated[CompanyRegister, Depends()]
):
    return await company_otp.company_otp(company)

@router.post("/creatCompany/", response_model=Token)
async def create_company(
    company: VerifyOtp, 
    verify_company: Annotated[CompanyRegister, Depends()],
    auth_service: Annotated[AuthService, Depends()],
):
    verify_company_otp = await verify_company.verify_company(company)
    return auth_service.create_tokens(company.email,"company")

@router.get("/companyName/{id}", response_model=str)
async def company_name(
    id: int,  company_service: Annotated[CompanyService, Depends()]
):
    return await company_service.get_company_name(id)

@router.get("/verified_companies_admin/", response_model=List[CompanyResponse])
async def get_verified_companiess(
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    company_service: Annotated[CompanyService, Depends()]):
    return await company_service.get_verified_companies_admin()

@router.get("/unverified_companies_admin/", response_model=List[CompanyResponse])
async def get_unverified_companiess(
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    company_service: Annotated[CompanyService, Depends()]):
    return await company_service.get_unverified_companies_admin()

@router.post("/verify_email_admin",response_model=CompanyResponse)
async def verify_company_email(
    email: str,
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    company_service: Annotated[CompanyService, Depends()]
):
    return await company_service.verify_company_admin(email)

@router.post("/ban_company_admin",response_model=CompanyResponse)
async def ban_company(
    email: str,
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    company_service: Annotated[CompanyService, Depends()]
):
    return await company_service.ban_company_admin(email)

@router.post("/unban_company_admin",response_model=CompanyResponse)
async def unban_company(
    email: str,
    current_admin: Annotated[Admin, Depends(get_current_admin)],
    company_service: Annotated[CompanyService, Depends()]
):
    return await company_service.unban_company_admin(email)