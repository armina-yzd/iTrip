from datetime import date,time
from pydantic import BaseModel

class ViewTicketUser(BaseModel):
    passenger_name: str
    service_type: str
    company_name: str
    from_location: str
    to_location: str
    vehicle_type: str
    vehicle_num: int
    start_date: date
    start_time: time
    price: int
    seat_num: int
    book_date: date
    book_time: time
    ticket_serial: int
    tracking_code: int

class ViewTicket(BaseModel):
    company_name: str
    from_location: str
    vehicle_type: str
    vehicle_num: int
    to_location: str
    start_date: date
    start_time: time
    price: int
