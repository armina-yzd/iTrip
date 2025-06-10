from pydantic import BaseModel
from enum import Enum
from datetime import date,time

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class ServiceType(str, Enum):
    BUS = "bus"
    TRAIN = "train"
    TOUR = "tour"
    AIRPLANE = "airplane"

class PurchaseMethod(str, Enum):
    WALLET = "wallet"
    BANK = "bank"

class PassengerCreate(BaseModel):
    gender: Gender
    first_name: str
    last_name: str
    national_id: str

class PassengerResponse(BaseModel):
    id: int
    gender: Gender
    first_name: str
    last_name: str
    national_id: str

class PaymentCreate(BaseModel):
    discount_id: int
    service_type: ServiceType
    paid: int 
    ticket_num : int
    purchase_method: PurchaseMethod

class PaymentResponse(BaseModel):
    id: int
    service_id: int
    service_type: ServiceType
    discount_id: int
    paid: int 
    ticket_num: int
    date: date
    time: time
    purchase_method: PurchaseMethod

class TicketCreate(BaseModel):
    ticket_serial: int
    tracking_code: int
    seat_num: int

class TicketResponse(BaseModel):
    id: int
    user_id: int
    passenger_id: int
    pay_id: int
    ticket_serial: int
    tracking_code: int
    seat_num: int

class BuyTicketCreate(BaseModel):
    ticket_create: TicketCreate
    passenger_create: PassengerCreate

class BuyTicketResponse(BaseModel):
    ticket_response: TicketResponse
    passenger_response: PassengerResponse