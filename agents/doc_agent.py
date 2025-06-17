from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def handle_doc_summary(query):
    prompt = f"Summarize the following text:\n\n{query}"
    return llm.invoke(prompt)
