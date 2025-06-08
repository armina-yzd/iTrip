from pydantic import BaseModel

class AdminLogIn(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True 

class AdminResponse(BaseModel):
    id : int
    username : str
    email: str
    password: str
    
    class Config:
        orm_mode = True 

class AdminCreate(BaseModel):
    username : str
    email: str
    password: str
    
    class Config:
        orm_mode = True 