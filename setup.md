# 🛠 SETUP GUIDE — Your Life OS POC

This document guides you through setting up the project locally with virtual environments, running the application, and executing tests.

---

## Project Requirements

- Python 3.11+
- pip (Python package manager)
- Git
- Ollama (with `mistral` model downloaded)

---

## 1. Clone the Repository

```bash
git clone https://github.com/HEMASAI1708/your_life_os_poc.git
cd your_life_os_poc
```

## 2. Setup Virtual Environment

- python -m venv venv
- venv\Scripts\activate   # On Windows
- pip install -r requirements.txt

## 3. Start Ollama & App

- ollama run mistral (in a different terminal)
- streamlit run main.py (in a different terminal)

## 4. Run Tests (Optional)

- set PYTHONPATH=.
- pytest --cov=your_life_os_poc --cov-config=.coveragerc tests/