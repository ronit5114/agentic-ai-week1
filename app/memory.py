import json

MEMORY_FILE = "agent_memory.json"


def load_memory(goal: str) -> dict:
    print("[MEMORY] Initializing fresh memory")
    return {
        "goal": goal,
        "steps": [],
        "completed": False
    }


def save_memory(memory: dict):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
    print("[MEMORY] Memory saved to file")
