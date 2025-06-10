import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import json
from typing import Annotated
from fastapi import Depends, HTTPException
from redis import Redis
from decouple import config
from dotenv import load_dotenv
from pathlib import Path
from app.core.redis.redis import get_redis
from fastapi import status


OTP_EXPIRE_TIME: str = config("OTP_EXPIRE_TIME")
SMTP_SERVER: str = config("SMTP_SERVER")  
SMTP_PORT: int = config("SMTP_PORT")  
SMTP_USERNAME: str = config("SMTP_USERNAME") 
SMTP_PASSWORD: str = config("SMTP_PASSWORD") 

class OTPService():
    def __init__(
        self, redis: Annotated[Redis, Depends(get_redis)]
    ) -> None:
        super().__init__()
        self.redis = redis

    @staticmethod
    def __generate_otp() -> str:
        return str(random.randint(100000, 999999))
    
    def __send_email(self, email: str, otp: str) -> bool:
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = SMTP_USERNAME
            msg["To"] = email
            msg["Subject"] = "Your OTP Code"

            body = f"Your OTP code is: {otp}. It will expire in 5 minutes."
            msg.attach(MIMEText(body, "plain"))

            # Connect to SMTP server and send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Enable TLS
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False


    def send_otp(self, email: str, user_data: dict) -> str:
        otp = self.__generate_otp()
        if not self.__send_email(email, otp):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to send OTP email"
            )
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