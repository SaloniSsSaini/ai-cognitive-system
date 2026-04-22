import os

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    REDIS_URL = os.getenv("REDIS_URL")
    JWT_SECRET = os.getenv("JWT_SECRET", "secret")

settings = Settings()