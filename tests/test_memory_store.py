import os
import json
import memory.store as store

def test_save_and_load_task(tmp_path, monkeypatch):
    test_file = tmp_path / "memory.json"
    
    # Patch MEMORY_FILE in the store module
    monkeypatch.setattr(store, "MEMORY_FILE", str(test_file))

    task = {"type": "task", "content": "test task"}
    store.save_to_memory(task)
    data = store.load_memory()
    assert len(data) == 1
    assert data[0]["content"] == "test task"

    store.delete_task_by_content("test task")
    data = store.load_memory()
    assert len(data) == 0
