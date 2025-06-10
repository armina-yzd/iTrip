from typing import Annotated, Dict
from fastapi import Depends, HTTPException,status
from datetime import datetime

from app.domain.models.pay import Pay
from app.domain.schemas.buy_ticket_schema import PaymentCreate
from app.infrastructure.repositories.payment_repo import PaymentRepository
from app.infrastructure.clients.iam_client import IAMClient

class PaymentService():
    def __init__(
        self,
        payment_repository: Annotated[PaymentRepository, Depends()],
        client: Annotated[IAMClient, Depends()]
    ) -> None:
        super().__init__()
        self.payment_repository = payment_repository
        self.client = client

    async def create_payment(self, payment: PaymentCreate,wallet: int,user_id: int) -> Pay:
        if payment.purchase_method == "wallet" and payment.paid > wallet:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Not Enough Money In Your Wallet"
            )
        new_wallet = wallet-payment.paid
        await self.client.reduce_wallet(new_wallet,user_id)
        now = datetime.now()
        return self.payment_repository.create_payment(
            Pay(
                ticket_num=payment.ticket_num,
                discount_id=payment.discount_id,
                paid=payment.paid,
                purchase_method=payment.purchase_method,
                date=now.date(),
                time=now.time()
            )
        )