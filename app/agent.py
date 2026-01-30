from app.control import decide_next_step
from app.llm import call_llm
from app.memory import load_memory, save_memory
from app.retriever import retrieve_context


def run_agent(goal: str):
    memory = load_memory(goal)

    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)

    while True:
        print("\n[AGENT] Loop iteration")
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)

        if step == "call_llm":
            context = retrieve_context(goal)
            response = call_llm(goal, context)
            memory["steps"].append(response)

            print("\n[AGENT] FINAL ANSWER:")
            print(response)

        elif step == "stop":
            save_memory(memory)
            print("[AGENT] Agent stopped cleanly")
            break
