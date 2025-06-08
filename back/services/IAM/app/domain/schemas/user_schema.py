from pydantic import BaseModel

class UserLogIn(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True 

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str
    wallet: int
    is_banned: bool

    class Config:
        orm_mode = True 

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True 

class UserResponseOtp(BaseModel):
    email: str
    otp: str

class UserOtp(BaseModel):
    email: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True 

class VerifyOtp(BaseModel):
    username: str
    email: str
    password: str
    otp: str

    class Config:
        orm_mode = True 

    

class VerifyOtpResponse(BaseModel):
    verify: bool
    message: str


