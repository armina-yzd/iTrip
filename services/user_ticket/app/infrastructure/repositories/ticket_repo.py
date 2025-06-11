from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db.database import get_db
from app.domain.models.ticket import Ticket
from app.domain.models.pay import Pay

class TicketRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_ticket(self, ticket: Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
    
    def ticket_count(self, service_id: int,service_type:str) -> int:
        return self.db.query(Ticket).join(Pay, Ticket.pay_id == Pay.id).filter(Pay.service_id == service_id, Pay.service_type == service_type).count()
    
    def payment_count(self, pay_id: int) -> int:
        return self.db.query(Ticket).join(Pay, Ticket.pay_id == Pay.id).filter(Pay.id == pay_id).count()
    
    def user_tickets(self, user_id: int) -> list[Ticket]:
        return self.db.query(Ticket).filter(Ticket.user_id == user_id)