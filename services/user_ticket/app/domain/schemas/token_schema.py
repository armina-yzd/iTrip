from pydantic import BaseModel

class TokenData(BaseModel):
    id: int
    username: str
    email: str
    password: str
    wallet: int
    is_banned: bool
