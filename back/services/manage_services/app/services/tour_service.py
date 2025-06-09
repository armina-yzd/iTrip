from typing import Annotated, Dict
from fastapi import Depends

from app.domain.schemas.services_schema import (
    TourCreate
)
from app.domain.models.tour_service import TourService
from app.infrastructure.repositories.tour_repo import TourServiceRepository


class TourSService():
    def __init__(
        self,
        tour_service_repository: Annotated[TourServiceRepository, Depends()]
    ) -> None:
        super().__init__()
        self.tour_service_repository = tour_service_repository

    async def add_tour_service(self, service: TourCreate, company_id: int) -> TourService:
        return self.tour_service_repository.add_tour_service(
            TourService(
                company_id=company_id,
                from_location=service.from_location,
                to_location=service.to_location,
                start_date=service.start_date,
                start_time=service.start_time,
                end_date=service.end_date,
                end_time=service.end_time,
                detail=service.detail,
                vehicle_type=service.vehicle_type,
                vehicle_num=service.vehicle_num,
                price=service.price,
                capacity=service.capacity
            )
        )
    
    async def get_service_by_company_id(self, id: int) -> list[TourService]:
        return self.tour_service_repository.get_service_by_company_id(id)
