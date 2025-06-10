from sqlalchemy import Column, String, Boolean,Integer
from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

class Company(EntityBase):
    __tablename__ = "company" 

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)  
    email = Column(String , unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean,default=False, nullable=False) 
    is_banned = Column(Boolean,default=False, nullable=False) 


