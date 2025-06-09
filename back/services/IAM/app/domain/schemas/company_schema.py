from pydantic import BaseModel

class CompanyLogIn(BaseModel):
    email: str
    password: str

class CompanyResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_verified: bool
    is_banned: bool

class CompanyCreate(BaseModel):
    name: str
    email: str
    password: str

class VerifyOtp(BaseModel):
    name: str
    email: str
    password: str
    otp: str

class CompanyOtp(BaseModel):
    name: str
    email: str
    password: str

class CompanyResponseOtp(BaseModel):
    email: str
    message: str

class VerifyOtpResponse(BaseModel):
    verify: bool
    message: str

class VerifyEmailResponse(BaseModel):
    message: str
    company: CompanyResponse

