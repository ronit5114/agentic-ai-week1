def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Memory state:", memory)

    if memory["completed"]:
        return "stop"

    if len(memory["steps"]) == 0:
        return "call_llm"        # 1st loop: REASON → ACT

    if "observed" not in memory["steps"]:
        return "observe"         # 2nd loop: OBSERVE

    memory["completed"] = True  # Stop ONLY if observation happened
    return "stop"