from app.services.llm import call_groq

def mock_search(query):
    if "AI" in query:
        return "OpenAI releases GPT-5"
    if "crypto" in query:
        return "Bitcoin hits ATH"
    return "Tech news"

def generate_post(bot_persona: str):
    topic = call_groq(f"Suggest a topic for: {bot_persona}")

    news = mock_search(topic)

    prompt = f"""
    Persona: {bot_persona}
    News: {news}

    Generate a strong opinion tweet under 280 chars.

    Output JSON:
    {{"bot_id":"", "topic":"", "post_content":""}}
    """

    return call_groq(prompt)