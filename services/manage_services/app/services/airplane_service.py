from datetime import date
from typing import Annotated, Dict, List
from fastapi import Depends

from app.domain.schemas.services_schema import (
    AirplainCreate,
    AirplainResponse
)
from app.domain.models.airplane_service import AirplaneService
from app.infrastructure.repositories.airplane_repo import AirplaneServiceRepository
from app.infrastructure.clients.user_ticket_client import UTClient
from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.view_schema import ViewTicket

class AirplaneSService():
    def __init__(
        self,
        airplane_service_repository: Annotated[AirplaneServiceRepository, Depends()],
        ut_client: Annotated[UTClient, Depends()],
        iam_client: Annotated[IAMClient, Depends()],
    ) -> None:
        super().__init__()
        self.airplane_service_repository = airplane_service_repository
        self.ut_client = ut_client
        self.iam_client = iam_client

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
    
    async def get_service_by_company_id(self, id: int) -> List[AirplainResponse]:
        airplane_d = self.airplane_service_repository.get_service_by_company_id(id)
        return await self.change_to_response_format(airplane_d)
    
    async def get_service_admin(self) -> List[AirplainResponse]:
        airplane_d = self.airplane_service_repository.get_service_admin()
        return await self.change_to_response_format(airplane_d)

    async def get_price_by_id(self, id: int) -> int:
        return self.airplane_service_repository.get_price_by_id(id)
    
    async def get_remain_by_id(self, id: int) -> int:
        ticket_count:int = await self.ut_client.ticket_count(id,"airplane")
        capacity = self.airplane_service_repository.get_capacity_by_id(id)
        return capacity - ticket_count
    
    async def get_info_by_id(self, id: int) -> ViewTicket:
        service = self.airplane_service_repository.get_info_by_id(id)
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
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> List[AirplaneService]:
        return self.airplane_service_repository.filter_service_by_place_and_date(from_location,to_location,start_date)

    async def get_filtered_services(self,from_location:str,to_location:str, start_date:date) -> List[AirplainResponse]:
        airplane_d = await self.filter_service_by_place_and_date(from_location,
                                                              to_location,
                                                              start_date)
        return await self.change_to_response_format(airplane_d)
        
    async def change_to_response_format(self, airplane_d:List[AirplaneService]) -> List[AirplainResponse]:
        airplane_services : List[AirplainResponse] = []
        for airplane in airplane_d:
            company_name = await self.iam_client.company_name(airplane.company_id)
            ticket_count:int = await self.ut_client.ticket_count(airplane.id,"airplane")
            airplane_response = AirplainResponse(
                id= airplane.id,
                company_name= company_name,
                from_location= airplane.from_location,
                to_location= airplane.to_location,
                start_date= airplane.start_date,
                start_time= airplane.start_time,
                detail= airplane.detail,
                vehicle_type= airplane.vehicle_type,
                vehicle_num= airplane.vehicle_num,
                price= airplane.price,
                is_canceled= airplane.is_canceled,
                capacity= airplane.capacity,
                remain= airplane.capacity - ticket_count
            )
            airplane_services.append(airplane_response)
        return airplane_services