from redis import Redis
from app.core.config import get_settings
import logging

config = get_settings()

def create_redis_connection():
    try:
        redis = Redis.from_url(
            config.REDIS_URL,
            decode_responses=True
        )
            
        return redis
        
    except RedisError as e:
        return None

redis = create_redis_connection()

def get_redis():
    if redis is None:
        raise RuntimeError("Redis connection is not available")
    return redis