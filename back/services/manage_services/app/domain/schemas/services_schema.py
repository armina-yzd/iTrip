from pydantic import BaseModel
from datetime import date, time

class BusCreate(BaseModel):
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    is_canceled: bool
    capacity: int

class AirplainCreate(BaseModel):
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    capacity: int

class TourCreate(BaseModel):
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    end_date: date
    end_time: time
    capacity: int

class TrainCreate(BaseModel):
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    compartment_num: int
    compart_person_num: int

class BusResponse(BaseModel):
    id: int
    company_id: int
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    is_canceled: bool
    capacity: int

class AirplainResponse(BaseModel):
    id: int
    company_id: int
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    is_canceled: bool
    capacity: int

class TourResponse(BaseModel):
    id: int
    company_id: int
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    is_canceled: bool
    end_date: date
    end_time: time
    capacity: int

class TrainResponse(BaseModel):
    id: int
    company_id: int
    from_location: str
    to_location: str
    start_date: date
    start_time: time
    detail: str
    vehicle_type: str
    vehicle_num: int
    price: int
    is_canceled: bool
    compartment_num: int
    compart_person_num: int

class FilterService(BaseModel):
    from_location: str
    to_location: str
    start_date: date