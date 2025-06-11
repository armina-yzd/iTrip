from typing import Annotated
from fastapi import APIRouter, Depends
from app.domain.schemas.buy_ticket_schema import TicketResponse

from app.services.ticket_service import TicketService
from app.domain.schemas.token_schema import TokenData
from app.services.auth import get_current_user

router = APIRouter(prefix="/ViewTicket", tags=["ViewTicket"])

@router.post("/userTickets/{service_id}",response_model=list[TicketResponse])
async def ticket_count(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    ticket_service: Annotated[TicketService, Depends()]
):
    return await ticket_service.user_tickets(current_user.id)
