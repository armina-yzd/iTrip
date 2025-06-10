from typing import Annotated
from fastapi import APIRouter, Depends

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

router = APIRouter(prefix="/Ticket", tags=["Ticket"])

# @router.post("/createPassenger/",response_model=PassengerResponse)
# async def create_passenger(
#     current_user: Annotated[TokenData, Depends(get_current_user)], 
#     passenger_create: PassengerCreate,
#     passenger_service: Annotated[PassengerService, Depends()], 
# ):
#     return await passenger_service.create_passenger(passenger_create)

@router.post("/payment/",response_model=PaymentResponse)
async def create_payment(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    payment_create: PaymentCreate,
    payment_service: Annotated[PaymentService, Depends()]
):
    return await payment_service.create_payment(payment_create,current_user.wallet,current_user.id)

# @router.post("/buyTicket/",response_model=BuyTicketResponse)
# async def buy_passenger(
#     current_user: Annotated[TokenData, Depends(get_current_user)], 
#     buy_ticket_create: BuyTicketCreate,
#     passenger_service: Annotated[PassengerService, Depends()], 
# ):
#     passenger:PassengerResponse = await passenger_service.create_passenger(buy_ticket_create.passenger_create)


