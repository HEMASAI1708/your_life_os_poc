def route_query(query):
    query_lower = query.lower()

    if any(word in query_lower for word in ["task", "todo", "reminder", "remind", "note"]):
        from agents.task_agent import handle_task
        return handle_task(query)

    elif any(word in query_lower for word in ["health", "checkup"]):
        from agents.health_agent import handle_health
        return handle_health(query)

    elif any(word in query_lower for word in ["summarize", "summary", "tl;dr"]):
        from agents.doc_agent import handle_doc_summary
        return handle_doc_summary(query)

    return "I'm not sure which agent should handle that."
