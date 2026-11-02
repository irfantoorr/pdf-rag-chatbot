# PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about the contents of PDF documents.

## Features

- PDF text extraction and chunking
- Vector embeddings with similarity search (FAISS)
- LLM-powered question answering grounded in document content
- Streamlit-based chat interface

## Tech Stack

- [LangChain](https://www.langchain.com/) / [LangGraph](https://www.langchain.com/langgraph) for orchestration
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search
- [Sentence Transformers](https://www.sbert.net/) for embeddings
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF parsing
- [Streamlit](https://streamlit.io/) for the UI
- [OpenAI](https://openai.com/) for the LLM backend

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/irfantoorr/pdf-rag-chatbot.git
   cd pdf-rag-chatbot
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set your API keys (e.g. in a `.env` file):
   ```
   OPENAI_API_KEY=your_key_here
   ```

## Usage

```bash
streamlit run ragchatbot.py
```

Upload a PDF in the sidebar, then ask questions about its contents in the main panel.

Note: this app uses [Ollama](https://ollama.com/) (`llama3.2`) as the LLM backend, so make sure Ollama is installed and running locally with that model pulled (`ollama pull llama3.2`).

## License

MIT
