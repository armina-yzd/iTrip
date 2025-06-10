from typing import Annotated, Dict
from fastapi import Depends

from app.domain.models.ticket import Ticket
from app.domain.schemas.buy_ticket_schema import TicketCreate
from app.infrastructure.repositories.ticket_repo import TicketRepository

class TicketService():
    def __init__(
        self,
        ticket_repository: Annotated[TicketRepository, Depends()]
    ) -> None:
        super().__init__()
        self.ticket_repository = ticket_repository

    async def create_ticket(self, ticket: TicketCreate,user_id: int,passenger_id: int,pay_id: int) -> Ticket:
        return self.ticket_repository.create_ticket(
            Ticket(
                user_id=user_id,
                passenger_id=passenger_id,
                pay_id=pay_id,
                ticket_serial=ticket.ticket_serial,
                tracking_code=ticket.tracking_code,
                seat_num=ticket.seat_num
            )
        )