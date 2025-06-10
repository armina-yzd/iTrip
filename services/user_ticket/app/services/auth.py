from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.token_schema import TokenData
from app.core.config import get_settings


config = get_settings()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"http://iam.localhost/api/user/login",
    scheme_name="user_oauth2_schema"
)

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    client: Annotated[IAMClient, Depends()],
) -> TokenData:

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
    return await client.validate_token(token)