from typing import Annotated
from fastapi import APIRouter, Depends
from typing import List

from app.domain.schemas.token_schema import TokenData
from app.domain.schemas.services_schema import (
    BusResponse,
    TourResponse,
    TrainResponse,
    AirplainResponse
)
from app.services.auth import get_current_company, get_current_admin
from app.services.bus_service import BusSService
from app.services.train_service import TrainSService
from app.services.tour_service import TourSService
from app.services.airplane_service import AirplaneSService

router = APIRouter(prefix="/getServices", tags=["Get"])

@router.get("/BusServiceCompany/",response_model=List[BusResponse])
async def get_bus_service(
    current_company: Annotated[TokenData, Depends(get_current_company)],
    bus_service: Annotated[BusSService, Depends()]
):
    return await bus_service.get_service_by_company_id(current_company.id)

@router.get("/TrainServiceCompany/",response_model=List[TrainResponse])
async def get_train_service(
    current_company: Annotated[TokenData, Depends(get_current_company)],
    train_service: Annotated[TrainSService, Depends()]
):
    return await train_service.get_service_by_company_id(current_company.id)

@router.get("/TourServiceCompany/",response_model=List[TourResponse])
async def get_tour_service(
    current_company: Annotated[TokenData, Depends(get_current_company)],
    tour_service: Annotated[TourSService, Depends()]
):
    return await tour_service.get_service_by_company_id(current_company.id)

@router.get("/AirplaneServiceCompany/",response_model=List[AirplainResponse])
async def get_airplane_service(
    current_company: Annotated[TokenData, Depends(get_current_company)],
    airplane_service: Annotated[AirplaneSService, Depends()]
):
    return await airplane_service.get_service_by_company_id(current_company.id)


# admin

@router.get("/BusServiceAdmin/",response_model=List[BusResponse])
async def get_bus_service(
    current_admin: Annotated[TokenData, Depends(get_current_admin)],
    bus_service: Annotated[BusSService, Depends()]
):
    return await bus_service.get_service_admin()

@router.get("/TrainServiceAdmin/",response_model=List[TrainResponse])
async def get_train_service(
    current_admin: Annotated[TokenData, Depends(get_current_admin)],
    train_service: Annotated[TrainSService, Depends()]
):
    return await train_service.get_service_admin()

@router.get("/TourServiceAdmin/",response_model=List[TourResponse])
async def get_tour_service(
    current_admin: Annotated[TokenData, Depends(get_current_admin)],
    tour_service: Annotated[TourSService, Depends()]
):
    return await tour_service.get_service_admin()

@router.get("/AirplaneServiceAdmin/",response_model=List[AirplainResponse])
async def get_airplane_service(
    current_admin: Annotated[TokenData, Depends(get_current_admin)],
    airplane_service: Annotated[AirplaneSService, Depends()]
):
    return await airplane_service.get_service_admin()
