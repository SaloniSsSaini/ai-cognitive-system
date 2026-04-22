# Phase 1
from app.db.vector_store import model
from app.db.postgres import cur

def route_post(post: str, threshold=0.7):
    emb = model.encode(post).tolist()

    cur.execute("""
        SELECT id, 1 - (embedding <=> %s) AS similarity
        FROM personas
        ORDER BY similarity DESC
    """, (emb,))

    results = cur.fetchall()

    return [r[0] for r in results if r[1] > threshold]