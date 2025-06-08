from typing import Optional
from typing import Annotated
from datetime import datetime, timedelta
from decouple import config
from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv
from pathlib import Path
import jwt
from fastapi.security import OAuth2PasswordBearer
from app.services.base import BaseService
from app.domain.schemas.token_schema import Token,TokenData
from app.services.auth.hash import HashPassword
from app.services.user.user_service import UserService
from app.services.admin.admin_service import AdminService
from app.domain.schemas.user_schema import UserLogIn
from app.domain.schemas.admin_schema import AdminLogIn
from app.domain.models.user import User
from app.domain.models.admin import Admin

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

JWT_SECRET : str = config("SECRET_KEY")
JWT_ALGORITHM : str = config("ALGORITHM")
REFRESH_SECRET : str = config("REFRESH_SECRET")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/userlogin")


class AuthService(BaseService):
    def __init__(
            self,
            hash_service: Annotated[HashPassword, Depends()],
            user_service: Annotated[UserService, Depends()],
            admin_service:  Annotated[AdminService, Depends()],
            ) -> None:
        super().__init__()
        self.hash_service = hash_service
        self.user_service = user_service
        self.admin_service = admin_service
    
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    
    def create_refresh_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=7)
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, REFRESH_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    
    def refresh_access_token(self, refresh_token: str) -> str:

        try:
            payload = jwt.decode(refresh_token, REFRESH_SECRET, algorithms=[JWT_ALGORITHM])
            if payload.get("type") != "refresh":
                raise HTTPException(status_code=401, detail="Invalid token type")
            
            username = payload.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid token payload")
                
            return self.create_access_token(data={"sub": username})
        except:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    def create_tokens(self, email: str) -> Token:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        
        access_token = self.create_access_token(
            data={"sub": email},
            expires_delta=access_token_expires
        )
        
        refresh_token = self.create_refresh_token(
            data={"sub": email},
            expires_delta=refresh_token_expires
        )
        
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )
    
    async def authenticate_user(self, user: UserLogIn) -> Token:
        founded_user = await self.user_service.get_user_by_email(
            user.email
        )
        if not founded_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )
        
        if not self.hash_service.verify_password(
            user.password, founded_user.password
        ):
           raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return self.create_tokens(user.email)
    
    async def authenticate_admin(self, admin: AdminLogIn) -> Token:
        founded_admin = await self.admin_service.get_admin_by_email(
            admin.email
        )
        if not founded_admin:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Admin does not exist"
            )
        
        if not self.hash_service.verify_password(
            admin.password, founded_admin.password
        ):
           raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return self.create_tokens(admin.email)


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        user_service: Annotated[UserService, Depends()],
        ) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except :
        raise credentials_exception
        
    user = await user_service.get_user_by_email(token_data.email)
    if user is None:
        raise credentials_exception
        
    return user

async def get_current_admin(
        token: Annotated[str, Depends(oauth2_scheme)],
        admin_service: Annotated[AdminService, Depends()],
        ) -> Admin:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except :
        raise credentials_exception
        
    admin = await admin_service.get_admin_by_email(token_data.email)
    if admin is None:
        raise credentials_exception
        
    return admin
    
