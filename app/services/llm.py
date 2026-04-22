import requests
from app.config import settings

def call_groq(prompt: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    res = requests.post(url, json=data, headers=headers)
    return res.json()["choices"][0]["message"]["content"]