from datetime import date,time
from pydantic import BaseModel

class ViewTicketAdmin(BaseModel):
    company_name: str
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    vehicle_type: str
    vehicle_num: int
    price: int

class ViewTicketUser(BaseModel):
    company_name: str
    passenger: str
    service_type: str
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    price: int
    seat_num: int
    vehicle_type: str
    vehicle_num: int
    book_date: date
    book_time: time
    ticket_serial: int
    tracking_code: int

