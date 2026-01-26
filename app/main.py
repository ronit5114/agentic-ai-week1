from app.agent import run_agent

def read_notice():
    with open("notice.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    notice_text = read_notice()
    goal = f"Explain the following college notice in very simple language:\n\n{notice_text}"
    run_agent(goal)