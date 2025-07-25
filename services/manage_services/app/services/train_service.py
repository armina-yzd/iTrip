from datetime import date
from typing import Annotated, Dict, List
from fastapi import Depends

from app.domain.schemas.services_schema import (
    TrainCreate,
    TrainResponse
)
from app.domain.models.train_service import TrainService
from app.infrastructure.repositories.train_repo import TrainServiceRepository
from app.infrastructure.clients.user_ticket_client import UTClient
from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.view_schema import ViewTicket

class TrainSService():
    def __init__(
        self,
        train_service_repository: Annotated[TrainServiceRepository, Depends()],
        ut_client: Annotated[UTClient, Depends()],
        iam_client: Annotated[IAMClient, Depends()],
    ) -> None:
        super().__init__()
        self.train_service_repository = train_service_repository
        self.ut_client = ut_client
        self.iam_client = iam_client

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
    
    async def get_service_by_company_id(self, id: int) -> List[TrainResponse]:
        train_d = self.train_service_repository.get_service_by_company_id(id)
        return await self.change_to_response_format(train_d)
    
    async def get_service_admin(self) -> List[TrainResponse]:
        train_d = self.train_service_repository.get_service_admin()
        return await self.change_to_response_format(train_d)
    
    async def get_price_by_id(self, id: int) -> int:
        return self.train_service_repository.get_price_by_id(id)
    
    async def get_remain_by_id(self, id: int) -> int:
        ticket_count:int = await self.ut_client.ticket_count(id,"train")
        capacity = self.train_service_repository.get_capacity_by_id(id)
        return capacity - ticket_count
    
    async def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> List[TrainService]:
        return self.train_service_repository.filter_service_by_place_and_date(from_location,to_location,start_date)
    
    async def get_filtered_services(self,from_location:str,to_location:str, start_date:date) -> List[TrainResponse]:
        train_d = await self.filter_service_by_place_and_date(from_location,
                                                              to_location,
                                                              start_date)
        return await self.change_to_response_format(train_d)
        
    async def get_info_by_id(self, id: int) -> ViewTicket:
        service = self.train_service_repository.get_info_by_id(id)
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
    
    async def change_to_response_format(self, train_d:List[TrainService]) -> List[TrainResponse]:
        train_services : List[TrainResponse] = []
        for train in train_d:
            company_name = await self.iam_client.company_name(train.company_id)
            ticket_count:int = await self.ut_client.ticket_count(train.id,"train")
            train_response = TrainResponse(
                id= train.id,
                company_name= company_name,
                from_location= train.from_location,
                to_location= train.to_location,
                start_date= train.start_date,
                start_time= train.start_time,
                detail= train.detail,
                vehicle_type= train.vehicle_type,
                vehicle_num= train.vehicle_num,
                price= train.price,
                is_canceled= train.is_canceled,
                compartment_num= train.compartment_num,
                compart_person_num=train.compart_person_num,
                remain= (train.compartment_num * train.compart_person_num) - ticket_count
            )
            train_services.append(train_response)
        return train_services

