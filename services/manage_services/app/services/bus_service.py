from datetime import date
from typing import Annotated, Dict, List
from fastapi import Depends

from app.domain.schemas.services_schema import (
    BusCreate,
    BusResponse
)
from app.domain.models.bus_service import BusService
from app.infrastructure.repositories.bus_repo import BusServiceRepository
from app.infrastructure.clients.user_ticket_client import UTClient
from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.view_schema import ViewTicket


class BusSService():
    def __init__(
        self,
        bus_service_repository: Annotated[BusServiceRepository, Depends()],
        ut_client: Annotated[UTClient, Depends()],
        iam_client: Annotated[IAMClient, Depends()],
    ) -> None:
        super().__init__()
        self.bus_service_repository = bus_service_repository
        self.ut_client = ut_client
        self.iam_client = iam_client

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

    async def get_service_by_company_id(self, id: int) -> list[BusResponse]:
        bus_d = self.bus_service_repository.get_service_by_company_id(id)
        return await self.change_to_response_format(bus_d)
    
    async def get_service_admin(self) -> list[BusResponse]:
        bus_d = self.bus_service_repository.get_service_admin()
        return await self.change_to_response_format(bus_d)
    
    async def get_price_by_id(self, id: int) -> int:
        return self.bus_service_repository.get_price_by_id(id)
    
    async def get_remain_by_id(self, id: int) -> int:
        ticket_count:int = await self.ut_client.ticket_count(id,"bus")
        capacity = self.bus_service_repository.get_capacity_by_id(id)
        return capacity - ticket_count
    
    async def get_info_by_id(self, id: int) -> ViewTicket:
        service = self.bus_service_repository.get_info_by_id(id)
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
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> list[BusService]:
        return self.bus_service_repository.filter_service_by_place_and_date(from_location,
                                                                            to_location,
                                                                            start_date)
    
    async def get_filtered_services(self,from_location:str,to_location:str, start_date:date) -> list[BusResponse]:
        bus_d = await self.filter_service_by_place_and_date(from_location,
                                                              to_location,
                                                              start_date)
        return await self.change_to_response_format(bus_d)
        
    async def change_to_response_format(self, bus_d:list[BusService]) -> list[BusResponse]:
        bus_services : List[BusResponse] = []
        for bus in bus_d:
            company_name = await self.iam_client.company_name(bus.company_id)
            ticket_count:int = await self.ut_client.ticket_count(bus.id,"bus")
            bus_response = BusResponse(
                id= bus.id,
                company_name= company_name,
                from_location= bus.from_location,
                to_location= bus.to_location,
                start_date= bus.start_date,
                start_time= bus.start_time,
                detail= bus.detail,
                vehicle_type= bus.vehicle_type,
                vehicle_num= bus.vehicle_num,
                price= bus.price,
                is_canceled= bus.is_canceled,
                capacity= bus.capacity,
                remain= bus.capacity - ticket_count
            )
            bus_services.append(bus_response)
        return bus_services