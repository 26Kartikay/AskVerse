# agent.py

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# === Step 1: PDF Loading ===
PDF_PATH = "arch.pdf"
if not os.path.exists("chroma_db"):
    print("Loading and splitting PDF...")
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    documents = splitter.split_documents(docs)

    print(f"🔗 Total Chunks: {len(documents)}")

    # Embedding and saving vector DB
    db = Chroma.from_documents(documents, OllamaEmbeddings(), persist_directory="chroma_db")
    db.persist()
    print(" Vector DB created and saved.")
else:
    print("Loading existing vector DB...")
    db = Chroma(persist_directory="chroma_db", embedding_function=OllamaEmbeddings())

# === Step 2: Retrieval Setup ===
retriever = db.as_retriever()

# === Step 3: LLM + Prompt ===
llm = OllamaLLM(model="llama3")  # Make sure this is pulled using `ollama pull llama3`

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """Answer the following question based only on provided context. 
Think step by step before providing a detailed answer.
<context>
{context}
</context>
Question: {input}""")
])

# === Step 4: Create Chains ===
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# === Step 5: Interactive Q&A ===
print("\n💬 Ask me anything from the PDF. Type 'exit' to quit.")
while True:
    query = input("\nYou: ")
    if query.strip().lower() in ['exit', 'quit']:
        print(" Bye!")
        break

    response = retrieval_chain.invoke({"input": query})
    answer = response.get("answer", response)
    print("\n Answer:", answer)
