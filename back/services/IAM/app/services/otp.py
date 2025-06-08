import random
import json
from typing import Annotated
from fastapi import Depends
from redis import Redis
from decouple import config
from dotenv import load_dotenv
from pathlib import Path
from app.core.redis.redis import get_redis
from app.services.base import BaseService

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

OTP_EXPIRE_TIME: str = config("OTP_EXPIRE_TIME", default=300)

class OTPService(BaseService):
    def __init__(
        self, redis: Annotated[Redis, Depends(get_redis)]
    ) -> None:
        super().__init__()
        self.redis = redis

    @staticmethod
    def __generate_otp() -> str:
        return str(random.randint(100000, 999999))

    def send_otp(self, email: str, user_data: dict) -> str:
        otp = self.__generate_otp()
        data = {
            'otp': otp,
            'user_data': user_data
        }
        self.redis.setex(email, OTP_EXPIRE_TIME, json.dumps(data))
        return otp

    def verify_otp(self, email: str, otp: str) -> bool:
        stored_data = self.redis.get(email)
        if stored_data is None:
            return False
        data = json.loads(stored_data)
        return data['otp'] == otp

    def get_user_data(self, email: str) -> dict:
        stored_data = self.redis.get(email)
        if stored_data is None:
            return None
        return json.loads(stored_data)['user_data']