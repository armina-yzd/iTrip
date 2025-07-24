from typing import Annotated
from fastapi import APIRouter, Depends
from app.domain.schemas.buy_ticket_schema import TicketResponse
from app.domain.schemas.view_ticket_schema import ViewTicketUser
from app.services.ticket_service import TicketService
from app.domain.schemas.token_schema import TokenData, TokenDataAdmin
from app.services.auth import get_current_admin, get_current_user

router = APIRouter(prefix="/ViewTicket", tags=["ViewTicket"])

@router.get("/userTickets",response_model=list[ViewTicketUser])
async def ticket_count(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    ticket_service: Annotated[TicketService, Depends()]
):
    return await ticket_service.user_tickets(current_user.id)
