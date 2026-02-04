def planner_step(memory: dict) -> str:
    print("\n[PLANNER] Reviewing memory:", memory)

    # Step 1: Call LLM
    if not memory["plan"]:
        step = "call_llm"
        memory["plan"].append(step)
        print("[PLANNER] Plan created:", step)
        return step

    # Step 2: Review result
    if len(memory["plan"]) == 1:
        step = "review_result"
        memory["plan"].append(step)
        print("[PLANNER] Plan updated:", step)
        return step

    # Finish
    memory["completed"] = True
    print("[PLANNER] Plan complete → STOP")
    return "stop"
