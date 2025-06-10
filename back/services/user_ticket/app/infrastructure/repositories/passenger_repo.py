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