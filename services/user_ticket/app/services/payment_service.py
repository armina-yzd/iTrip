from typing import Annotated, Dict
from fastapi import Depends, HTTPException,status
from datetime import datetime

from app.domain.models.pay import Pay
from app.domain.schemas.buy_ticket_schema import PaymentCreate
from app.infrastructure.repositories.payment_repo import PaymentRepository
from app.infrastructure.clients.iam_client import IAMClient
from app.infrastructure.clients.manage_service_client import MSClient

class PaymentService():
    def __init__(
        self,
        payment_repository: Annotated[PaymentRepository, Depends()],
        client: Annotated[IAMClient, Depends()],
        manageSclient: Annotated[MSClient, Depends()],
    ) -> None:
        super().__init__()
        self.payment_repository = payment_repository
        self.client = client
        self.manageSclient = manageSclient

    async def create_payment(self, payment: PaymentCreate,wallet: int,user_id: int,service_id:int,service_type:str) -> Pay:
        remain = await self.manageSclient.get_remain(service_type,service_id)

        if payment.purchase_method == "wallet" and payment.paid > wallet:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Not Enough Money In Your Wallet"
            )
        new_wallet = wallet-payment.paid
        await self.client.reduce_wallet(new_wallet,user_id)
        price: int = await self.manageSclient.get_price(service_type,service_id)
        total_price = price * payment.ticket_num
        if total_price != payment.paid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="payment and service price does not match"
            )
        if payment.ticket_num > remain:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="not enough tickets"
                )
        now = datetime.now()
        return self.payment_repository.create_payment(
            Pay(
                ticket_num=payment.ticket_num,
                service_id=service_id,
                service_type=payment.service_type,
                discount_id=payment.discount_id,
                paid=payment.paid,
                purchase_method=payment.purchase_method,
                date=now.date(),
                time=now.time()
            )
        )
    
    async def get_ticket_count(self, id: int) -> int:
        return self.payment_repository.get_ticket_count(id)
    
    async def get_service_id_and_type(self, id: int) -> Pay:
        return self.payment_repository.get_service_id_and_type(id)