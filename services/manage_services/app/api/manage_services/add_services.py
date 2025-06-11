from typing import Annotated
from fastapi import APIRouter, Depends

from app.domain.schemas.token_schema import TokenData
from app.domain.schemas.services_schema import (
    BusCreate,
    TourCreate,
    TrainCreate,
    AirplainCreate,
    BusResponse2,
    TourResponse2,
    TrainResponse2,
    AirplainResponse2
)
from app.services.auth import get_current_company
from app.services.bus_service import BusSService
from app.services.train_service import TrainSService
from app.services.tour_service import TourSService
from app.services.airplane_service import AirplaneSService

router = APIRouter(prefix="/addServices", tags=["Add"])

@router.post("/addBusService/",response_model=BusResponse2)
async def add_bus_service(
    current_company: Annotated[TokenData, Depends(get_current_company)], 
    bus_create: BusCreate,
    bus_service: Annotated[BusSService, Depends()], 
):
    return await bus_service.add_bus_service(bus_create,current_company.id)

@router.post("/addTrainService/",response_model=TrainResponse2)
async def add_train_service(
    current_company: Annotated[TokenData, Depends(get_current_company)], 
    train_create: TrainCreate,
    train_service: Annotated[TrainSService, Depends()], 
):
    return await train_service.add_train_service(train_create,current_company.id)

@router.post("/addTourService/",response_model=TourResponse2)
async def add_train_service(
    current_company: Annotated[TokenData, Depends(get_current_company)], 
    tour_create: TourCreate,
    tour_service: Annotated[TourSService, Depends()], 
):
    return await tour_service.add_tour_service(tour_create,current_company.id)

@router.post("/addAirplaneService/",response_model=AirplainResponse2)
async def add_airplane_service(
    current_company: Annotated[TokenData, Depends(get_current_company)], 
    airplane_create: AirplainCreate,
    airplane_service: Annotated[AirplaneSService, Depends()], 
):
    return await airplane_service.add_airplane_service(airplane_create,current_company.id)
