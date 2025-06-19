from langchain_ollama import OllamaLLM
from agents.task_agent import handle_task
from agents.health_agent import handle_health
from agents.doc_agent import handle_doc_summary
from agents.chat_agent import handle_chat
from utils.logger import get_logger

logger = get_logger()

# Initialize local LLM
llm = OllamaLLM(model="mistral")

# Prompt template to classify the user's intent
INTENT_PROMPT = """
You are an intent classifier for a personal assistant.

Classify the following user query into one of these categories:
- task
- health
- summarize
- unknown

Examples:
- "remind me to book a doctor appointment" → task
- "check my heart rate data" → health
- "summarize this: LangChain is a framework..." → summarize
- "what is photosynthesis?" → summarize
- "I need help" → unknown

Query: "{query}"

Respond with just one word: task, health, summarize, or unknown.
"""

def fallback_router(query_lower: str) -> str:
    if any(word in query_lower for word in ["task", "remind", "todo", "note"]):
        return "task"
    elif any(word in query_lower for word in ["health", "sleep", "heartbeat", "wellness"]):
        return "health"
    elif any(word in query_lower for word in ["summarize", "summary", "tl;dr", "what is"]):
        return "summarize"
    return "unknown"

def route_query(query: str) -> str:
    query_lower = query.lower()
    classification_prompt = INTENT_PROMPT.format(query=query)
    intent = llm.invoke(classification_prompt).strip().lower()

    if intent == "unknown":
        logger.info("LLM returned 'unknown', falling back to keyword match.")
        intent = fallback_router(query_lower)

    # Log the final intent classification
    logger.info(f"Classified intent: {intent} for query: {query}")

    if intent == "task":
        return handle_task(query)
    elif intent == "health":
        return handle_health(query)
    elif intent == "summarize":
        return handle_doc_summary(query)
    else:
        return handle_chat(query)
