from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException,status

from app.domain.schemas.token_schema import TokenData
from app.domain.schemas.buy_ticket_schema import (
    PassengerCreate,
    PassengerResponse,
    PaymentCreate,
    PaymentResponse,
    TicketCreate,
    TicketResponse,
    BuyTicketCreate,
    BuyTicketResponse
)
from app.services.ticket_service import TicketService

router = APIRouter(prefix="/TicketInfo", tags=["TicketInfo"])

@router.post("/ticketCount/{service_id}",response_model=int)
async def ticket_count(
    ticket_service: Annotated[TicketService, Depends()],
    service_id: int
):
    return await ticket_service.ticket_count(service_id)
