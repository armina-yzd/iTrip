from typing import Annotated, Dict
from fastapi import Depends

from app.domain.schemas.services_schema import (
    BusCreate,
    TrainCreate,
    TourCreate,
    AirplainCreate
)
from app.domain.models.bus_service import BusService
from app.infrastructure.repositories.bus_repo import BusServiceRepository


class BusSService():
    def __init__(
        self,
        bus_service_repository: Annotated[BusServiceRepository, Depends()]
    ) -> None:
        super().__init__()
        self.bus_service_repository = bus_service_repository

    async def add_bus_service(self, service: BusCreate, company_id: int) -> BusService:
        return self.bus_service_repository.add_bus_service(
            BusService(
                company_id=company_id,
                from_location=service.from_location,
                to_location=service.to_location,
                start_date=service.start_date,
                start_time=service.start_time,
                detail=service.detail,
                vehicle_type=service.vehicle_type,
                vehicle_num=service.vehicle_num,
                price=service.price,
                capacity=service.capacity
            )
        )


    # async def get_user_by_email(self, email: str) -> User:
    #     return self.user_repository.get_user_by_email(email)
    
    # async def get_user_by_username(self, username: str) -> User:
    #     return self.user_repository.get_user_by_username(username)
    
    # async def get_banned_user(self, email: str) -> User:
    #     return self.user_repository.get_banned_user(email)