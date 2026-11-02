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
- [Ollama](https://ollama.com/) (`llama3.2`) for the LLM backend — runs locally, free, no API key needed

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

3. Install [Ollama](https://ollama.com/) and pull the model:
   ```bash
   ollama pull llama3.2
   ```

## Usage

```bash
streamlit run ragchatbot.py
```

Make sure Ollama is running, then upload a PDF in the sidebar and ask questions about its contents in the main panel.

## License

MIT
