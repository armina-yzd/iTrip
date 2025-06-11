from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.domain.models.bus_service import BusService
from app.domain.models.train_service import TrainService
from app.domain.models.tour_service import TourService
from app.domain.models.airplane_service import AirplaneService
from app.domain.schemas.services_schema import (
    BusResponse2,
    TourResponse2,
    TrainResponse2,
    AirplainResponse2
)
from app.core.db.database import get_db

router = APIRouter(prefix="/test", tags=["Test"])

# Get all bus services
@router.get("/busServices/", response_model=List[BusResponse2])
def get_bus_services(
    db: Session = Depends(get_db)):
    return db.query(BusService).all()

# Get all train services
@router.get("/trainServices/", response_model=List[TrainResponse2])
def get_train_services(
    db: Session = Depends(get_db)):
    return db.query(TrainService).all()

# # Get all tour services
@router.get("/tourServices/", response_model=List[TourResponse2])
def get_tour_services(
    db: Session = Depends(get_db)):
    return db.query(TourService).all()

# # Get all airplane services
@router.get("/airplaneServices/", response_model=List[AirplainResponse2])
def get_airplane_services(
    db: Session = Depends(get_db)):
    return db.query(AirplaneService).all()