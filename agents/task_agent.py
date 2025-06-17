from memory.store import save_to_memory

def handle_task(query):
    save_to_memory({"type": "task", "content": query})
    return f"✅ Task noted: '{query}'"