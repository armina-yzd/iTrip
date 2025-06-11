from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException,status

from app.domain.schemas.services_schema import GetInfo
from app.services.bus_service import BusSService
from app.services.train_service import TrainSService
from app.services.tour_service import TourSService
from app.services.airplane_service import AirplaneSService

router = APIRouter(prefix="/serviceInfo", tags=["Info"])

@router.post("/servicePrice",response_model=int)
async def service_info(
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
    

@router.post("/serviceRemain",response_model=int)
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

