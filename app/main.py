from fastapi import FastAPI
from app.api.routes import auth, chat, bots

app = FastAPI(title="AI Cognitive System")

app.include_router(auth.router, prefix="/auth")
app.include_router(chat.router, prefix="/chat")
app.include_router(bots.router, prefix="/bots")

@app.get("/")
def root():
    return {"message": "AI Cognitive System Running 🚀"}