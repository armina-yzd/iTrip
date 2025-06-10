from pydantic import BaseModel

class TokenData(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_verified: bool
    is_banned: bool
