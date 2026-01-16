def decide_next_step(memory: dict) -> str:
    if memory["completed"]:
        return "stop"

    if "steps" not in memory:
        memory["steps"] = 0

    if memory ["steps"] < 2:
        memory["steps"] +=1
        return "call llm"

    return "stop"