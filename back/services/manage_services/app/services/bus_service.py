from datetime import date
from typing import Annotated, Dict
from fastapi import Depends

from app.domain.schemas.services_schema import (
    BusCreate
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


    async def get_service_by_company_id(self, id: int) -> list[BusService]:
        return self.bus_service_repository.get_service_by_company_id(id)
    
    async def get_price_by_id(self, id: int) -> int:
        return self.bus_service_repository.get_price_by_id(id)
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> list[BusService]:
        return self.bus_service_repository.filter_service_by_place_and_date(from_location,to_location,start_date)
