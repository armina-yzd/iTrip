from typing import Annotated, List
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
from app.services.auth import get_current_user
from app.services.passenger_service import PassengerService
from app.services.payment_service import PaymentService
from app.services.ticket_service import TicketService

router = APIRouter(prefix="/Ticket", tags=["Ticket"])

@router.post("/payment/{service_id}",response_model=PaymentResponse)
async def create_payment(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    payment_create: PaymentCreate,
    service_id: int,
    payment_service: Annotated[PaymentService, Depends()]
):
    return await payment_service.create_payment(payment_create,current_user.wallet,
                                                current_user.id,service_id,
                                                payment_create.service_type)

@router.post("/buyTicket/{service_id}",response_model=List[BuyTicketResponse])
async def buy_passenger(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    payment_id: int,
    buy_ticket_create: List[BuyTicketCreate],
    ticket_service: Annotated[TicketService, Depends()], 
):
    return await ticket_service.buy_ticket(payment_id,buy_ticket_create,current_user.id)
    