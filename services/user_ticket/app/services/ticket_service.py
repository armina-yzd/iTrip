from typing import Annotated, Dict
from fastapi import Depends, HTTPException, status

from app.domain.models.ticket import Ticket
from app.domain.schemas.buy_ticket_schema import BuyTicketCreate, BuyTicketResponse, PassengerResponse, TicketCreate, TicketResponse
from app.infrastructure.repositories.ticket_repo import TicketRepository
from app.services.passenger_service import PassengerService
from app.services.payment_service import PaymentService
from app.infrastructure.clients.manage_service_client import MSClient

class TicketService():
    def __init__(
        self,
        ticket_repository: Annotated[TicketRepository, Depends()],
        passenger_service: Annotated[PassengerService, Depends()], 
        payment_service: Annotated[PaymentService, Depends()],
        manages_client: Annotated[MSClient, Depends()],
    ) -> None:
        super().__init__()
        self.ticket_repository = ticket_repository
        self.passenger_service = passenger_service
        self.payment_service = payment_service
        self.manages_client = manages_client

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
    
    async def ticket_count(self, service_id: int,service_type:str) -> int:
        if service_type not in {"train", "tour", "bus", "airplane"}:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="service type does not exist"
            )
        return self.ticket_repository.ticket_count(service_id,service_type)
    
    async def buy_ticket(self, payment_id:int,buy_ticket_create: list[BuyTicketCreate],user_id:int) -> list[BuyTicketResponse]:

        ticket_count:int = await self.payment_service.get_ticket_count(payment_id)
        payment = await self.payment_service.get_service_id_and_type(payment_id)
        remain = await self.manages_client.get_remain(payment.service_type,payment.service_id)
        payment_count = self.ticket_repository.payment_count(payment_id)
        
        if ticket_count <= payment_count:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="already bought tickets with this payment"
                )
        if not (ticket_count or remain):
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="this payment doesnt exist"
                )
        if ticket_count > remain:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="not enough tickets"
                )
        if len(buy_ticket_create) != ticket_count:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="the count in the payment doesnt match count "
                )
        passengers_tickets: list[BuyTicketResponse] = []

        for passenger_ticket in buy_ticket_create:
            passenger_db = await self.passenger_service.create_passenger(passenger_ticket.passenger_create)
            ticket_db = await self.create_ticket(passenger_ticket.ticket_create,
                                                user_id,passenger_db.id,payment_id)
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
    
