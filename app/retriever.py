import os

def retrieve_context(query: str) -> str:
    print("[RETRIEVER] Reading knowledge.txt")

    # Get absolute path to this file's directory
    base_dir = os.path.dirname(__file__)

    # Build path to knowledge.txt inside app/
    kb_path = os.path.join(base_dir, "knowledge.txt")

    with open(kb_path, "r", encoding="utf-8") as f:
        data = f.read()

    print("[RETRIEVER] Context found:")
    print(data)

    return data
