import os
import json

MEMORY_FILE = "memory.json"

def save_to_memory(item):
    memory = load_memory()
    if item in memory:
        return  # Skip duplicate
    memory.append(item)
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

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
