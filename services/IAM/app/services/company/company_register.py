from typing import Annotated
from fastapi import Depends, HTTPException, status

from app.domain.schemas.company_schema import (
    CompanyResponseOtp,
    VerifyOtp,
    CompanyOtp,
    VerifyOtpResponse,
    CompanyCreate
)
from app.services.auth.auth import AuthService
from app.services.auth.otp import OTPService
from app.services.company.company_service import CompanyService


class CompanyRegister():
    def __init__(
        self,
        company_service: Annotated[CompanyService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
        auth_service: Annotated[AuthService, Depends()],
    ) -> None:
        super().__init__()
        self.company_service = company_service
        self.otp_service = otp_service
        self.auth_service = auth_service

    async def company_otp(self, company: CompanyOtp) -> CompanyResponseOtp:
        existing_email = await self.company_service.get_company_by_email(company.email)
        existing_name = await self.company_service.get_company_by_name(company.name)
        
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Company already exists"
            )
        if existing_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Name already exists"
            )
        
        company_data = {
            'name': company.name,
            'email': company.email,
            'password': company.password
        }
        otp = self.otp_service.send_otp(company.email, company_data)

        return CompanyResponseOtp(
            email=company.email,
            message="OTP Send",
        )

    async def verify_company(self, verify_company: VerifyOtp) -> VerifyOtpResponse:
        if not self.otp_service.verify_otp(verify_company.email, verify_company.otp):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Invalid Input"
            )
        
        company_data = self.otp_service.get_user_data(verify_company.email)
        if not company_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="OTP expired or invalid"
            )
        
        await self.company_service.create_company(
            CompanyCreate(
                name=company_data['name'],
                email=company_data['email'],
                password=company_data['password']
            )
        )
        
        return VerifyOtpResponse(
            verify=True, 
            message="Company verified"
        )