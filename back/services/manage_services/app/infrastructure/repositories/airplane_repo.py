from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.airplane_service import AirplaneService

class AirplaneServiceRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def add_airplane_service(self, service: AirplaneService) -> AirplaneService:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service
    
    def get_service_by_company_id(self, id: int) -> list[AirplaneService]:
        return self.db.query(AirplaneService).filter(AirplaneService.company_id == id).all()
