from app.agent import run_agent
import os

if __name__ == "__main__":
    # 🔴 DEMO RESET (IMPORTANT FOR CLASS)
    if os.path.exists("agent_memory.json"):
        os.remove("agent_memory.json")
        print("[MAIN] Demo reset: old memory deleted")

    goal = "Explain the Aurangabad college notice in simple words"
    run_agent(goal)
