import redis
from app.config import settings

r = redis.Redis.from_url(settings.REDIS_URL)

def get_cache(key):
    return r.get(key)

def set_cache(key, value):
    r.set(key, value, ex=300)