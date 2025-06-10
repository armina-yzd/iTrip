from datetime import date
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.bus_service import BusService

class BusServiceRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def add_bus_service(self, service: BusService) -> BusService:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service

    def get_service_by_company_id(self, id: int) -> list[BusService]:
        return self.db.query(BusService).filter(BusService.company_id == id).all()
    
    def filter_service_by_place_and_date(self,from_location:str,to_location:str, start_date:date) -> list[BusService]:
        return self.db.query(BusService).filter(BusService.from_location == from_location,
                                                BusService.to_location==to_location,
                                                BusService.start_date==start_date).all()