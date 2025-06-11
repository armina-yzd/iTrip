from typing import Annotated
from fastapi import APIRouter, Depends
from app.domain.schemas.buy_ticket_schema import TicketResponse

from app.services.ticket_service import TicketService
from app.domain.schemas.token_schema import TokenData, TokenDataAdmin
from app.services.auth import get_current_admin, get_current_user

router = APIRouter(prefix="/ViewTicket", tags=["ViewTicket"])

@router.post("/userTickets",response_model=list[TicketResponse])
async def ticket_count(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    ticket_service: Annotated[TicketService, Depends()]
):
    return await ticket_service.user_tickets(current_user.id)

@router.post("/adminTickets",response_model=list[TicketResponse])
async def ticket_count(
    current_admin: Annotated[TokenDataAdmin, Depends(get_current_admin)], 
    ticket_service: Annotated[TicketService, Depends()]
):
    return await ticket_service.all_tickets()
