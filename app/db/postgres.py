import psycopg2
from app.config import settings

conn = psycopg2.connect(settings.DATABASE_URL)
cur = conn.cursor()