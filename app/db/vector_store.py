from sentence_transformers import SentenceTransformer
from app.db.postgres import cur, conn

model = SentenceTransformer("all-MiniLM-L6-v2")

def insert_persona(id, text):
    emb = model.encode(text).tolist()
    cur.execute(
        "INSERT INTO personas (id, content, embedding) VALUES (%s,%s,%s)",
        (id, text, emb)
    )
    conn.commit()