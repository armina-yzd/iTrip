from typing import Annotated, Dict
from fastapi import Depends

from app.domain.models.passenger import Passenger
from app.domain.schemas.buy_ticket_schema import PassengerCreate
from app.infrastructure.repositories.passenger_repo import PassengerRepository

class PassengerService():
    def __init__(
        self,
        passenger_repository: Annotated[PassengerRepository, Depends()]
    ) -> None:
        super().__init__()
        self.passenger_repository = passenger_repository

    async def create_passenger(self, passenger: PassengerCreate) -> Passenger:
        return self.passenger_repository.create_passenger(
            Passenger(
                gender=passenger.gender,
                first_name=passenger.first_name,
                last_name=passenger.last_name,
                national_id=passenger.national_id
            )
        )
    
    async def get_passenger_by_id(self, passenger_id: int) -> Passenger:
        return self.passenger_repository.get_passenger_by_id(passenger_id)