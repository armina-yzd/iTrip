
from sqlalchemy import Column, String, Boolean,Integer

from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

class User(EntityBase):
    __tablename__ = "users" 

    id = Column(Integer,primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)  
    email = Column(String , unique=True, nullable=False)
    password = Column(String, nullable=False)
    wallet = Column(Integer,nullable=False, default=0)  
    is_banned = Column(Boolean,default=False, nullable=False) 


