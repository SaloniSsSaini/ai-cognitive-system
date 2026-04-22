from fastapi import WebSocket

connections = []

async def connect(ws: WebSocket):
    await ws.accept()
    connections.append(ws)

async def broadcast(msg: str):
    for conn in connections:
        await conn.send_text(msg)