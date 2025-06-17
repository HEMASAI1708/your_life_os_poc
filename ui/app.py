import streamlit as st
from api.router import route_query
from memory.store import load_memory, delete_task_by_content

def run_app():
    st.title("🧠 Your Life OS POC")
    st.write("Ask me to add tasks, summarize things, or check your health.")
    st.write("✅ UI Loaded")
    user_input = st.text_input("What would you like to do?")

    if st.button("Submit") and user_input:
        response = route_query(user_input)
        st.write("🤖", response)

    st.markdown("---")
    st.subheader("📋 Your Tasks")

    tasks = load_memory()
    tasks = [t for t in tasks if t.get("type") == "task"]

    if not tasks:
        st.info("No tasks saved yet.")
    else:
        for task in tasks:
            task_text = task.get("content")
            if st.checkbox(task_text, key=task_text):
                delete_task_by_content(task_text)
                st.rerun()

