from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.train_service import TrainService

class TrainServiceRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def add_train_service(self, service: TrainService) -> TrainService:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service
    
    def get_service_by_company_id(self, id: int) -> list[TrainService]:
        return self.db.query(TrainService).filter(TrainService.company_id == id).all()
