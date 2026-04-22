from fastapi import APIRouter
from app.core.router import route_post
from app.core.langgraph_flow import generate_post

router = APIRouter()

@router.post("/route")
def route(post: str):
    return {"bots": route_post(post)}

@router.post("/generate")
def generate():
    return {"post": generate_post("Tech Maximalist")}