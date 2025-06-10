from sqlalchemy import Column, String, Boolean,Integer

from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

class Admin(EntityBase):
    __tablename__ = "admins" 

    id = Column(Integer,primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)  
    email = Column(String , unique=True, nullable=False)
    password = Column(String, nullable=False)


