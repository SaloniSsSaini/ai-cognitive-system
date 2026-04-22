from fastapi import APIRouter
from app.services.auth_service import create_token

router = APIRouter()

@router.post("/login")
def login():
    token = create_token({"user": "test"})
    return {"token": token}