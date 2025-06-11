from typing import Annotated
from fastapi import Depends
from decouple import config

from app.core.config import get_settings, Settings
from app.domain.schemas.token_schema import TokenData
from app.infrastructure.clients.http_client import HTTPClient

class MSClient:
    def __init__(
        self,
        http_client: Annotated[HTTPClient, Depends()],
        config: Settings = Depends(get_settings),
    ):
        self.config = config
        self.http_client = http_client
        
    async def get_price(self, service_type: str, service_id: int) -> int:
        async with self.http_client as client:
            response = await client.post(
                f"{self.config.MANAGE_SERVICES_URL}/api/serviceInfo/servicePrice",
                data={"id": service_id, "service_type": service_type} 
            )
            response.raise_for_status()
            return int(response.json())
        
    async def get_remain(self, service_type: str, service_id: int) -> int:
        async with self.http_client as client:
            response = await client.post(
                f"{self.config.MANAGE_SERVICES_URL}/api/serviceInfo/serviceRemain",
                data={"id": service_id, "service_type": service_type} 
            )
            response.raise_for_status()
            return int(response.json())

