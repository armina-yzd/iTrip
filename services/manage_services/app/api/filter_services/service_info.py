from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException,status

from app.domain.schemas.services_schema import GetInfo
from app.services.bus_service import BusSService
from app.services.train_service import TrainSService
from app.services.tour_service import TourSService
from app.services.airplane_service import AirplaneSService
from app.domain.schemas.view_schema import ViewTicket

router = APIRouter(prefix="/serviceInfo", tags=["Info"])

@router.get("/servicePrice",response_model=int)
async def service_price(
    service_info: GetInfo,
    bus_service: Annotated[BusSService, Depends()],
    airplane_service: Annotated[AirplaneSService, Depends()],
    train_service: Annotated[TrainSService, Depends()],
    tour_service: Annotated[TourSService, Depends()],
):
    
    if service_info.service_type == "bus":
        return await bus_service.get_price_by_id(service_info.id)
    elif service_info.service_type == "airplane":
        return await airplane_service.get_price_by_id(service_info.id)
    elif service_info.service_type == "train":
        return await train_service.get_price_by_id(service_info.id)
    elif service_info.service_type == "tour":
        return await tour_service.get_price_by_id(service_info.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Service Type Does Not Exist"
        )
    

@router.get("/serviceRemain",response_model=int)
async def service_remain(
    service_info: GetInfo,
    bus_service: Annotated[BusSService, Depends()],
    airplane_service: Annotated[AirplaneSService, Depends()],
    train_service: Annotated[TrainSService, Depends()],
    tour_service: Annotated[TourSService, Depends()],
):
    
    if service_info.service_type == "bus":
        return await bus_service.get_remain_by_id(service_info.id)
    elif service_info.service_type == "airplane":
        return await airplane_service.get_remain_by_id(service_info.id)
    elif service_info.service_type == "train":
        return await train_service.get_remain_by_id(service_info.id)
    elif service_info.service_type == "tour":
        return await tour_service.get_remain_by_id(service_info.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Service Type Does Not Exist"
        )
    
@router.get("/serviceViewInfo",response_model=list[ViewTicket])
async def service_info(
    service_info: list[GetInfo],
    bus_service: Annotated[BusSService, Depends()],
    airplane_service: Annotated[AirplaneSService, Depends()],
    train_service: Annotated[TrainSService, Depends()],
    tour_service: Annotated[TourSService, Depends()],
):
    view_services: list[ViewTicket] = []
    for service in service_info:
        if service.service_type == "bus":
            bus = await bus_service.get_info_by_id(service.id)
            view_services.append(bus)
        elif service.service_type == "airplane":
            airplane = await airplane_service.get_info_by_id(service.id)
            view_services.append(airplane)
        elif service.service_type == "train":
            train = await train_service.get_info_by_id(service.id)
            view_services.append(train)
        elif service.service_type == "tour":
            tour = await tour_service.get_info_by_id(service.id)
            view_services.append(tour)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Service Type Does Not Exist"
            )
    return view_services

@router.get("/serviceViewInfoo",response_model=ViewTicket)
async def service_infoo(
    service_info: GetInfo,
    bus_service: Annotated[BusSService, Depends()],
    airplane_service: Annotated[AirplaneSService, Depends()],
    train_service: Annotated[TrainSService, Depends()],
    tour_service: Annotated[TourSService, Depends()],
):

    if service_info.service_type == "bus":
        service = await bus_service.get_info_by_id(service_info.id)    
    elif service_info.service_type == "airplane":
        service = await airplane_service.get_info_by_id(service_info.id)       
    elif service_info.service_type == "train":
        service = await train_service.get_info_by_id(service_info.id)    
    elif service_info.service_type == "tour":
        service = await tour_service.get_info_by_id(service_info.id)  
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Service Type Does Not Exist"
        )
    return service
