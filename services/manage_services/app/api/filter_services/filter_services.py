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

router = APIRouter(prefix="/filterServices", tags=["Filter"])

@router.post("/FilterBusService/",response_model=List[BusResponse])
async def filter_bus_service(
    bus_service: Annotated[BusSService, Depends()],
    filter_service: FilterService
):
    return await bus_service.filter_service_by_place_and_date(filter_service.from_location,
                                                              filter_service.to_location,
                                                              filter_service.start_date)

@router.post("/FilterTrainService/",response_model=List[TrainResponse])
async def filter_train_service(
    train_service: Annotated[TrainSService, Depends()],
    filter_service: FilterService
):
    return await train_service.filter_service_by_place_and_date(filter_service.from_location,
                                                                filter_service.to_location,
                                                                filter_service.start_date)

@router.post("/FilterTourService/",response_model=List[TourResponse])
async def filter_tour_service(
    tour_service: Annotated[TourSService, Depends()],
    filter_service: FilterService
):
    return await tour_service.filter_service_by_place_and_date(filter_service.from_location,
                                                               filter_service.to_location,
                                                               filter_service.start_date)

@router.post("/FilterAirplaneService/",response_model=List[AirplainResponse])
async def filter_airplane_service(
    airplane_service: Annotated[AirplaneSService, Depends()],
    filter_service: FilterService
):
    return await airplane_service.filter_service_by_place_and_date(filter_service.from_location,
                                                                   filter_service.to_location,
                                                                   filter_service.start_date)
