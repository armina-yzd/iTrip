from sqlalchemy import Column, Integer, Date, Time
from sqlalchemy.dialects.postgresql import ENUM
from app.core.db.database import get_entitybase

EntityBase = get_entitybase()

purchase_method_enum = ENUM('wallet', 'bank', name='purchase_method_enum')
service_type_enum = ENUM('bus', 'train', 'tour', 'airplane', name='service_type_enum')

class Pay(EntityBase):
    __tablename__ = "paymentTicket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, nullable=False)
    service_type = Column(service_type_enum, nullable=False)
    discount_id = Column(Integer)
    paid = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    ticket_num = Column(Integer, nullable=False)
    purchase_method = Column(purchase_method_enum, nullable=False)