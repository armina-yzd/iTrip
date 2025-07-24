from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.passenger import Passenger

class PassengerRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_passenger(self, passenger: Passenger) -> Passenger:
        self.db.add(passenger)
        self.db.commit()
        self.db.refresh(passenger)
        return passenger
    
    def get_passenger_by_id(self, passenger_id: int) -> Passenger:
        passenger:Passenger = self.db.query(Passenger).filter(Passenger.id == passenger_id).first()
        return passenger