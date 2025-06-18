from memory.store import save_to_memory, delete_task_by_content, clear_all_tasks
from agents.chat_agent import handle_chat

def handle_task(query):
    query_clean = query.strip()
    query_lower = query_clean.lower()

    # Handle clear commands
    if any(cmd in query_lower for cmd in ["remove all tasks", "clear all tasks", "delete all tasks", "refresh all the tasks"]):
        clear_all_tasks()
        return "🗑️ All tasks have been deleted."

    # Handle specific delete command
    if "remove the task" in query_lower:
        task_text = query_lower.replace("remove the task", "").strip().strip('"')
        delete_task_by_content(task_text)
        return f"🗑️ Task deleted: '{task_text}'"

    # Reject questions as tasks and route to chat agent
    if query_clean.endswith("?") or query_lower.startswith("who ") or query_lower.startswith("what ") or query_lower.startswith("why "):
        return handle_chat(query)

    # Save if it's a unique task
    task_data = {"type": "task", "content": query_clean}
    saved = save_to_memory(task_data)

    if saved:
        return f"✅ Task noted: '{query_clean}'"
    else:
        return f"⚠️ That task already exists."
