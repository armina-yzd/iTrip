from sqlalchemy import Column, String, Boolean, Integer, Date, Time, ForeignKey
from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

class TrainService(EntityBase):
    __tablename__ = "train_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)
    from_location = Column(String, nullable=False) 
    to_location = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    detail = Column(String)
    vehicle_type = Column(String, nullable=False)
    vehicle_num = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    compartment_num = Column(Integer, nullable=False)
    compart_person_num = Column(Integer, nullable=False)
    is_canceled = Column(Boolean, default=False, nullable=False)   