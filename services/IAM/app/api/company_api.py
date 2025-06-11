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
from app.services.auth.auth import AuthService , get_current_company
from app.services.company.company_register import CompanyRegister
from app.services.company.company_service import CompanyService

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

@router.post("/creatCompany/", response_model=VerifyOtpResponse)
async def create_company(
    company: VerifyOtp, 
    verify_company: Annotated[CompanyRegister, Depends()]
):
    return await verify_company.verify_company(company)

@router.post("/companyName/{id}", response_model=str)
async def company_name(
    id: int,  company_service: Annotated[CompanyService, Depends()]
):
    return await company_service.get_company_name(id)

# Get all users
@router.get("/companies/", response_model=List[CompanyResponse])
def get_companiess(db: Session = Depends(get_db)):
    return db.query(Company).all()

# Delete a user
@router.delete("/companies/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    db.delete(company)
    db.commit()
    return {"message": "Company deleted successfully"}


@router.post(
    "/verify-email",
    response_model=VerifyEmailResponse
)
async def verify_company_email(
    email: str,
    company_service: Annotated[CompanyService, Depends()],
    db: Session = Depends(get_db),
):
    current_company = await company_service.get_company_by_email(email)
    current_company.is_verified = True
    db.commit()
    db.refresh(current_company)
    
    return {
        "message": "Company email verified successfully",
        "company": current_company
    }