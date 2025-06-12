from typing import Annotated
from fastapi import Depends
from decouple import config

from app.core.config import get_settings, Settings
from app.domain.schemas.token_schema import TokenData, TokenDataAdmin
from app.infrastructure.clients.http_client import HTTPClient

SECRET : str = config("SECRET")
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
                f"{self.config.IAM_URL}/api/user/me", headers=headers
            )
            response.raise_for_status()
            return TokenData(**response.json())
        
    async def validate_token_admin(self, token: str) -> TokenDataAdmin:
        headers = {"Authorization": f"Bearer {token}"}
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.IAM_URL}/api/admin/me", headers=headers
            )
            response.raise_for_status()
            return TokenDataAdmin(**response.json())
        
    async def reduce_wallet(self, new_wallet: int, user_id: int):
        async with self.http_client as client:
            response = await client.post(
                f"{self.config.IAM_URL}/api/user/wallet/{user_id}",
                data={"new_wallet": new_wallet, "secret_code": SECRET} 
            )
            response.raise_for_status()
            return response.json()

