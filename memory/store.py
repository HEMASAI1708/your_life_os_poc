import os
import json

MEMORY_FILE = "memory.json"

def save_to_memory(item):
    memory = load_memory()
    if any(existing.get("type") == item.get("type") and existing.get("content") == item.get("content") for existing in memory):
        return False  # duplicate
    memory.append(item)
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)
    return True

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def delete_task_by_content(task_text):
    memory = load_memory()
    memory = [item for item in memory if item.get("content") != task_text]
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

def clear_all_tasks():
    memory = load_memory()
    memory = [item for item in memory if item.get("type") != "task"]
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)
