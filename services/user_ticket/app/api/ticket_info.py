from typing import Annotated
from fastapi import APIRouter, Depends
from app.domain.schemas.buy_ticket_schema import ServiceType

from app.services.ticket_service import TicketService

router = APIRouter(prefix="/TicketInfo", tags=["TicketInfo"])

@router.get("/ticketCount/{service_id}",response_model=int)
async def ticket_count(
    ticket_service: Annotated[TicketService, Depends()],
    service_id: int,
    service_type: str
):
    return await ticket_service.ticket_count(service_id,service_type)
