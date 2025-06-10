from datetime import date
from typing import Annotated, Dict
from fastapi import Depends

from app.domain.schemas.services_schema import (
    TrainCreate
)
from app.domain.models.train_service import TrainService
from app.infrastructure.repositories.train_repo import TrainServiceRepository


class TrainSService():
    def __init__(
        self,
        train_service_repository: Annotated[TrainServiceRepository, Depends()]
    ) -> None:
        super().__init__()
        self.train_service_repository = train_service_repository

    async def add_train_service(self, service: TrainCreate, company_id: int) -> TrainService:
        return self.train_service_repository.add_train_service(
            TrainService(
                company_id=company_id,
                from_location=service.from_location,
                to_location=service.to_location,
                start_date=service.start_date,
                start_time=service.start_time,
                detail=service.detail,
                vehicle_type=service.vehicle_type,
                vehicle_num=service.vehicle_num,
                price=service.price,
                compartment_num=service.compartment_num,
                compart_person_num=service.compart_person_num
            )
        )
    
    async def get_service_by_company_id(self, id: int) -> list[TrainService]:
        return self.train_service_repository.get_service_by_company_id(id)
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> list[TrainService]:
        return self.train_service_repository.filter_service_by_place_and_date(from_location,to_location,start_date)

