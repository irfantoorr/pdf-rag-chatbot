import pdfplumber
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.header("My First RAG Chatbot")

# Sidebar
with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload PDF", type=["pdf"])


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# Main page
if file is not None:

    # Extract PDF text
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    st.subheader("Extracted PDF Content")
    # st.write(text)

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ",", ""],
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)
    st.write("Total chunks:", len(chunks))

    # Generate embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store vectors in FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)
    st.success("PDF embeddings stored successfully!")

    # Retriever
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4}
    )

    # Define the LLM
    llm = ChatOllama(
        model="llama3.2",
        temperature=0.3,
        num_predict=100
    )

    # Provide the prompts
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful assistant answering questions about a PDF document.\n\n"
         "Guidelines:\n"
         "1. Provide complete, well-explained answers using the context below.\n"
         "2. Include relevant details, numbers, and explanations to give a thorough response.\n"
         "3. If the context mentions related information, include it to give fuller picture.\n"
         "4. Only use information from the provided context - do not use outside knowledge.\n"
         "5. Summarize long information, ideally in bullets where needed\n"
         "6. If the information is not in the context, say so politely.\n\n"
         "Context:\n{context}"),
        ("human", "{question}")
    ])

    # Generate answer
    # question -> embeddings -> similarity search -> result to LLM -> response (CHAIN)
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # Get user question
    user_question = st.text_input("Type your question here")

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)