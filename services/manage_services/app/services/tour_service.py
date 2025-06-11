from datetime import date
from typing import Annotated, Dict, List
from fastapi import Depends

from app.domain.schemas.services_schema import (
    TourCreate,
    TourResponse
)
from app.domain.models.tour_service import TourService
from app.infrastructure.repositories.tour_repo import TourServiceRepository
from app.infrastructure.clients.user_ticket_client import UTClient
from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.view_schema import ViewTicket

class TourSService():
    def __init__(
        self,
        tour_service_repository: Annotated[TourServiceRepository, Depends()],
        ut_client: Annotated[UTClient, Depends()],
        iam_client: Annotated[IAMClient, Depends()],
    ) -> None:
        super().__init__()
        self.tour_service_repository = tour_service_repository
        self.ut_client = ut_client
        self.iam_client = iam_client

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
    
    async def get_service_by_company_id(self, id: int) -> list[TourResponse]:
        tour_d =  self.tour_service_repository.get_service_by_company_id(id)
        return await self.change_to_response_format(tour_d)
    
    async def get_price_by_id(self, id: int) -> int:
        return self.tour_service_repository.get_price_by_id(id)
    
    async def get_remain_by_id(self, id: int) -> int:
        ticket_count:int = await self.ut_client.ticket_count(id,"tour")
        capacity = self.tour_service_repository.get_capacity_by_id(id)
        return capacity - ticket_count
    
    async def get_info_by_id(self, id: int) -> ViewTicket:
        service = self.tour_service_repository.get_info_by_id(id)
        company_name = await self.iam_client.company_name(service.company_id)
        view_ticket = ViewTicket(
            company_name=company_name,
            from_location= service.from_location,
            to_location= service.to_location,
            start_date= service.start_date,
            start_time= service.start_time,
            vehicle_type= service.vehicle_type,
            vehicle_num= service.vehicle_num,
            price= service.price,
            )
        return view_ticket
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> list[TourService]:
        return self.tour_service_repository.filter_service_by_place_and_date(from_location,to_location,start_date)
    
    async def get_filtered_services(self,from_location:str,to_location:str, start_date:date) -> list[TourResponse]:
        tour_d = await self.filter_service_by_place_and_date(from_location,
                                                              to_location,
                                                              start_date)
        return await self.change_to_response_format(tour_d)
        

    async def change_to_response_format(self, tour_d:list[TourService]) -> list[TourResponse]:
        tour_services : List[TourResponse] = []
        for tour in tour_d:
            company_name = await self.iam_client.company_name(tour.company_id)
            ticket_count:int = await self.ut_client.ticket_count(tour.id,"tour")
            tour_response = TourResponse(
                id= tour.id,
                company_name= company_name,
                from_location= tour.from_location,
                to_location= tour.to_location,
                start_date= tour.start_date,
                start_time= tour.start_time,
                end_date= tour.end_date,
                end_time= tour.end_time,
                detail= tour.detail,
                vehicle_type= tour.vehicle_type,
                vehicle_num= tour.vehicle_num,
                price= tour.price,
                is_canceled= tour.is_canceled,
                capacity= tour.capacity,
                remain= tour.capacity - ticket_count
            )
            tour_services.append(tour_response)
        return tour_services

