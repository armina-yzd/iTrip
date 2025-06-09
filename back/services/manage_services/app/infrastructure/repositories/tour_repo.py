from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.tour_service import TourService

class TourServiceRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def add_tour_service(self, service: TourService) -> TourService:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service
    
    def get_service_by_company_id(self, id: int) -> list[TourService]:
        return self.db.query(TourService).filter(TourService.company_id == id).all()
