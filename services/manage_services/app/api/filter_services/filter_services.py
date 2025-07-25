from datetime import date
from typing import Annotated
from fastapi import APIRouter, Depends
from typing import List

from app.domain.schemas.services_schema import (
    BusResponse,
    TourResponse,
    TrainResponse,
    AirplainResponse,
    FilterService
)
from app.services.bus_service import BusSService
from app.services.train_service import TrainSService
from app.services.tour_service import TourSService
from app.services.airplane_service import AirplaneSService
from app.infrastructure.clients.user_ticket_client import UTClient

router = APIRouter(prefix="/filterServices", tags=["Filter"])

@router.get("/FilterBusService/",response_model=List[BusResponse])
async def filter_bus_service(
    bus_service: Annotated[BusSService, Depends()],
    from_location: str,
    to_location: str,
    start_date: date
):
    return await bus_service.get_filtered_services(from_location,
                                                   to_location,
                                                   start_date)
    
@router.get("/FilterTrainService/",response_model=List[TrainResponse])
async def filter_train_service(
    train_service: Annotated[TrainSService, Depends()],
    from_location: str,
    to_location: str,
    start_date: date
):
    return await train_service.get_filtered_services(from_location,
                                                    to_location,
                                                    start_date)

@router.get("/FilterTourService/",response_model=List[TourResponse])
async def filter_tour_service(
    tour_service: Annotated[TourSService, Depends()],
    from_location: str,
    to_location: str,
    start_date: date
):
    return await tour_service.get_filtered_services(from_location,
                                                               to_location,
                                                               start_date)

@router.get("/FilterAirplaneService/",response_model=List[AirplainResponse])
async def filter_airplane_service(
    airplane_service: Annotated[AirplaneSService, Depends()],
    from_location: str,
    to_location: str,
    start_date: date
):
    return await airplane_service.get_filtered_services(from_location,
                                                        to_location,
                                                        start_date)
