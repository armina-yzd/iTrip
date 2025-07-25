from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    user_id: int
    passenger_id: int
    pay_id: int
    ticket_serial: int
    tracking_code: int
    seat_num: int