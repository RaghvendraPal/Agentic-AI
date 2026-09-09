# KrishLangChainPractice

A comprehensive repository for learning and practicing LangChain, LangSmith, LangServe, and Generative AI applications with OpenAI, Ollama, Groq, and Open-Source Models.

---

## 📁 Repository Structure

```
KrishLangChainPractice/
│
├── .env.example                # Template for required environment variables
├── pyproject.toml              # Project configuration and dependencies (uv / pip)
├── requirements_openai.txt     # Requirements file for pip installation
├── Note.txt                    # Quick reference notes for LangChain ecosystem
│
├── OpenAI/                     # OpenAI & LangChain foundational notebooks
│   ├── 1.1-GettingStarted.ipynb # Quickstart with LangChain, LangSmith, and OpenAI
│   └── 1.2-Simpleapp.ipynb      # Building simple LLM chains and apps
│
├── Ollama/                     # Local open-source models with Ollama
│   └── app.py                  # Streamlit application using Ollama (Gemma / LLaMA)
│
├── OpenSourceModel/            # Open-source LLMs and serving
│   ├── Groq.ipynb              # High-speed inference using Groq API
│   ├── chatbot.ipynb           # Interactive chatbot workflows & memory
│   ├── vectorretriver.ipynb    # Vector databases, embeddings, and RAG retrieval
│   └── serve.py                # FastAPI & LangServe deployment for LangChain runnables
│
└── src/
    └── krishlangchainpractice/ # Python package source files
        └── __init__.py
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or standard `pip` / `venv`
- [Ollama](https://ollama.ai/) installed locally (optional, for local LLMs)

### 2. Environment Setup

Clone the repository and configure your environment variables:

```bash
# Copy the example environment file
cp .env.example .env
```

Edit `.env` and fill in your API keys:
- `OPENAI_API_KEY`: OpenAI API key
- `LANGCHAIN_API_KEY`: LangSmith API key for monitoring & tracing
- `GROQ_API_KEY`: Groq Cloud API key
- `HF_TOKEN`: HuggingFace access token

### 3. Installation

#### Using `uv` (Recommended)
```bash
uv sync
```

#### Using `pip` & virtual environment
```bash
python -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements_openai.txt
```

---

## 🖥️ Running Applications

### 1. Streamlit Demo with Ollama
Make sure Ollama is running (`ollama run gemma3:1b` or your chosen model):
```bash
streamlit run Ollama/app.py
```

### 2. FastAPI & LangServe API Server
Run the LangServe translation runnable service:
```bash
python OpenSourceModel/serve.py
```
Access the interactive playground at `http://localhost:8000/chain/playground/`.

### 3. Jupyter Notebooks
Launch Jupyter Lab or VS Code Notebooks to explore the interactive tutorials:
```bash
jupyter lab
```
