from api.router import route_query

def test_route_task():
    result = route_query("add task buy milk")
    assert "✅ Task noted" in result

def test_route_health():
    result = route_query("check my health")
    assert "🩺" in result

def test_route_summarize():
    result = route_query("summarize this: Python is great")
    assert isinstance(result, str)  # Output from Ollama

def test_fallback():
    result = route_query("xyz nothing here")
    assert "I'm not sure" in result
