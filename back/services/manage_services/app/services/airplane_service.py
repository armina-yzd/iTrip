from datetime import date
from typing import Annotated, Dict
from fastapi import Depends

from app.domain.schemas.services_schema import (
    AirplainCreate
)
from app.domain.models.airplane_service import AirplaneService
from app.infrastructure.repositories.airplane_repo import AirplaneServiceRepository


class AirplaneSService():
    def __init__(
        self,
        airplane_service_repository: Annotated[AirplaneServiceRepository, Depends()]
    ) -> None:
        super().__init__()
        self.airplane_service_repository = airplane_service_repository

    async def add_airplane_service(self, service: AirplainCreate, company_id: int) -> AirplaneService:
        return self.airplane_service_repository.add_airplane_service(
            AirplaneService(
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
    
    async def get_service_by_company_id(self, id: int) -> list[AirplaneService]:
        return self.airplane_service_repository.get_service_by_company_id(id)
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> list[AirplaneService]:
        return self.airplane_service_repository.filter_service_by_place_and_date(from_location,to_location,start_date)
