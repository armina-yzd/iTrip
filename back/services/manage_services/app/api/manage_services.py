from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.domain.models.bus_service import BusService
from app.domain.schemas.token_schema import TokenData
from app.domain.schemas.services_schema import (
    BusCreate,
    TourCreate,
    TrainCreate,
    AirplainCreate,
    BusResponse
)
from app.services.auth import get_current_company
from app.services.bus_service import BusSService
from app.core.db.database import get_db

router = APIRouter(prefix="/manageServices", tags=["Manage"])

@router.post("/addBusService/",response_model=BusResponse)
async def add_bus_service(
    current_company: Annotated[TokenData, Depends(get_current_company)], 
    bus_create: BusCreate,
    bus_service: Annotated[BusSService, Depends()], 
):
    return await bus_service.add_bus_service(bus_create,current_company.id)

# Get all bus services
@router.get("/busServices/", response_model=List[BusResponse])
def get_bus_services(
    db: Session = Depends(get_db)):
    return db.query(BusService).all()