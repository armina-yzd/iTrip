from typing import Annotated
from fastapi import Depends
from app.core.config import get_settings, Settings
from app.domain.schemas.token_schema import TokenData,TokenDataAdmin
from app.infrastructure.clients.http_client import HTTPClient


class IAMClient:
    def __init__(
        self,
        http_client: Annotated[HTTPClient, Depends()],
        config: Settings = Depends(get_settings),
    ):
        self.config = config
        self.http_client = http_client

    async def validate_token(self, token: str) -> TokenData:
        headers = {"Authorization": f"Bearer {token}"}
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.IAM_URL}/api/company/me", headers=headers
            )
            response.raise_for_status()
            return TokenData(**response.json())
    
    async def company_name(self, company_id: int) -> str:
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.IAM_URL}/api/company/companyName/{company_id}"
            )
            response.raise_for_status()
            return str(response.json())
        
    async def validate_token_admin(self, token: str) -> TokenDataAdmin:
        headers = {"Authorization": f"Bearer {token}"}
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.IAM_URL}/api/admin/me", headers=headers
            )
            response.raise_for_status()
            return TokenDataAdmin(**response.json())