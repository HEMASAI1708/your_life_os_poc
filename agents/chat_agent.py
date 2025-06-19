from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def handle_chat(query):
    return llm.invoke(f"Answer this like a helpful assistant: {query}")
