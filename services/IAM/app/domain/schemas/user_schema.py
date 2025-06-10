from pydantic import BaseModel

class UserLogIn(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str
    wallet: int
    is_banned: bool

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponseOtp(BaseModel):
    email: str
    message: str

class UserOtp(BaseModel):
    username: str
    email: str
    password: str

class VerifyOtp(BaseModel):
    username: str
    email: str
    password: str
    otp: str

class VerifyOtpResponse(BaseModel):
    verify: bool
    message: str

class WalletUpdateRequest(BaseModel):
    new_wallet: int
    secret_code: str