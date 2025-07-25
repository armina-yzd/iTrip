from typing import Annotated
from fastapi import Depends
from app.core.config import get_settings, Settings
from app.infrastructure.clients.http_client import HTTPClient


class UTClient:
    def __init__(
        self,
        http_client: Annotated[HTTPClient, Depends()],
        config: Settings = Depends(get_settings),
    ):
        self.config = config
        self.http_client = http_client

    async def ticket_user(self, ticket_id: int) -> int:
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.USER_TICKET_URL}/api/TicketInfo/ticketUser/{ticket_id}"
            )
            response.raise_for_status()
            return int(response.json())
        