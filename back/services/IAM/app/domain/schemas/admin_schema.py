from pydantic import BaseModel

class AdminLogIn(BaseModel):
    email: str
    password: str

class AdminResponse(BaseModel):
    id : int
    username : str
    email: str
    password: str

class AdminCreate(BaseModel):
    username : str
    email: str
    password: str