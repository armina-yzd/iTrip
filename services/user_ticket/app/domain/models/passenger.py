from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import ENUM
from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

gender_enum = ENUM('male', 'female', name='gender_enum')

class Passenger(EntityBase):
    __tablename__ = "passenger"

    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(gender_enum, nullable=False)
    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)
    national_id= Column(String, nullable=False)