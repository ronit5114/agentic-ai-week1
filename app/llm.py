import requests
 
RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"


def call_llm(prompt: str, context: str) -> str:
    full_prompt = f"""
Use ONLY the information below to answer.

INFORMATION:
{context}

QUESTION:
{prompt}
"""

    response = requests.post(
        RENDER_API_URL,
        json={"prompt": full_prompt},
        timeout=20
    )

    return response.json()["response"]
