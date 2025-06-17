from langchain_ollama import OllamaLLM
from agents.task_agent import handle_task
from agents.health_agent import handle_health
from agents.doc_agent import handle_doc_summary
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


def route_query(query: str) -> str:
    logger.info(f"Received query: {query}")
    classification_prompt = INTENT_PROMPT.format(query=query)
    intent = llm.invoke(classification_prompt).strip().lower()

    logger.info(f"Intent classified as: {intent}")

    if "task" in intent:
        return handle_task(query)
    elif "health" in intent:
        return handle_health(query)
    elif "summarize" in intent:
        return handle_doc_summary(query)
    else:
        return "🤖 I'm not sure how to handle that yet."
