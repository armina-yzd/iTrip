from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ENUM
from app.core.db.database import get_entitybase

EntityBase = get_entitybase()


class Ticket(EntityBase):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    passenger_id = Column(Integer, unique=True, nullable=False)
    pay_id = Column(Integer, nullable=False)
    ticket_serial = Column(Integer, nullable=False)
    tracking_code = Column(Integer, nullable=False)
    seat_num = Column(Integer, nullable=False)