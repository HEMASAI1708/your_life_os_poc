from agents.task_agent import handle_task
from memory.store import load_memory

def test_handle_task():
    task_query = "remind me to call Alice"
    response = handle_task(task_query)
    assert "✅ Task noted" in response

    memory = load_memory()
    assert any("call Alice" in t["content"] for t in memory)
