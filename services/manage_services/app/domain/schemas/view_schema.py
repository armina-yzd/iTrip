from datetime import date,time
from pydantic import BaseModel

class ViewTicket(BaseModel):
    company_name: str
    from_location: str
    vehicle_type: str
    vehicle_num: int
    to_location: str
    start_date: date
    start_time: time
    price: int
