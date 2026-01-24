import requests
import random
 
def fetch_joke_tool() -> str:
    print("[TOOL] Calling external Joke API")
 
    # Simulate failure sometimes (for learning)
    if random.choice([True, False]):
        print("[TOOL] Simulated tool failure")
        return "TOOL_FAILED"
 
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke",
        timeout=5
    )
 
    if response.status_code != 200:
        print("[TOOL] API error")
        return "TOOL_FAILED"
 
    data = response.json()
    joke = f"{data['setup']} — {data['punchline']}"
    print("[TOOL] Joke fetched successfully")
    return joke
 
 