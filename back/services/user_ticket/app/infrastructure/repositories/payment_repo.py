from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.pay import Pay

class PaymentRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_payment(self, payment: Pay) -> Pay:
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment