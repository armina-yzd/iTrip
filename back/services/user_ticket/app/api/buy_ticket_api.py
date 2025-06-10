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

@router.post("/buyTicket/{service_id}",response_model=list[BuyTicketResponse])
async def buy_passenger(
    current_user: Annotated[TokenData, Depends(get_current_user)], 
    payment_id: int,
    buy_ticket_create: list[BuyTicketCreate],
    passenger_service: Annotated[PassengerService, Depends()], 
    payment_service: Annotated[PaymentService, Depends()],
    ticket_service: Annotated[TicketService, Depends()], 
):
    ticket_count:int = await payment_service.get_ticket_count(payment_id)
    if not ticket_count:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="this payment doesnt exist"
            )
    if len(buy_ticket_create) != ticket_count:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="the count in the payment doesnt match count "
            )
    passengers_tickets: list[BuyTicketResponse] = []
    for passenger_ticket in buy_ticket_create:
        passenger_db = await passenger_service.create_passenger(passenger_ticket.passenger_create)
        ticket_db = await ticket_service.create_ticket(passenger_ticket.ticket_create,
                                                                   current_user.id,passenger_db.id,payment_id)
        passenger = PassengerResponse(
            id=passenger_db.id,
            gender=passenger_db.gender,
            first_name=passenger_db.first_name,
            last_name=passenger_db.last_name,
            national_id=passenger_db.national_id
        )

        ticket = TicketResponse(
            id=ticket_db.id,
            user_id=ticket_db.user_id,
            passenger_id=ticket_db.passenger_id,
            pay_id=ticket_db.pay_id,
            ticket_serial=ticket_db.ticket_serial,
            tracking_code=ticket_db.tracking_code,
            seat_num=ticket_db.seat_num
        )
        
        passenger_ticket_done= BuyTicketResponse(ticket_response=ticket,passenger_response=passenger)    
        passengers_tickets.append(passenger_ticket_done)

    return passengers_tickets