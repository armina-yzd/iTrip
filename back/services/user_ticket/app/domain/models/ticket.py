from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ENUM
from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

service_type_enum = ENUM('bus', 'train', 'tour', 'airplane', name='service_type_enum')

class Ticket(EntityBase):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    passenger_id = Column(Integer, unique=True, nullable=False)
    pay_id = Column(Integer, nullable=False)
    ticket_serial = Column(Integer, nullable=False)
    tracking_code = Column(Integer, nullable=False)
    service_type = Column(service_type_enum, nullable=False)
    seat_num = Column(Integer, nullable=False)