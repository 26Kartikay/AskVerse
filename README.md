# PDF Q&A System Core Logic (`agent.py`)

This file contains the core backend logic for the PDF Q&A system. It handles all the heavy lifting: from loading and processing a PDF document to using a local Large Language Model (LLM) to answer questions based on the document's content. It operates as a command-line interface (CLI) application for a quick and direct way to interact with your document.

---

## Features

* **PDF Processing:** Loads a PDF file (`arch.pdf`) and splits it into smaller, manageable chunks.
* **Vector Database Management:** Creates a persistent vector database (`chroma_db`) from the PDF chunks using Ollama embeddings. This allows for fast, efficient retrieval of relevant document sections.
* **Local LLM Integration:** Connects to a locally running Llama3 model via Ollama to generate answers.
* **Context-Aware Answering:** Ensures the LLM only provides answers based on the information found within the PDF, preventing hallucinations.
* **Interactive CLI:** Provides a simple command-line interface for real-time questioning and answering.

---

## Technologies Used

* **Python:** The core programming language.
* **LangChain:** Framework for orchestrating the document loading, splitting, and retrieval process.
* **Ollama:** Used for both generating text embeddings and running the Llama3 LLM locally.
* **ChromaDB:** The vector database where the document chunks are stored.
* **PyPDFLoader:** A LangChain utility for reading PDF files.

---

## Installation and Setup

Before running this script, you must have the required dependencies and local environment set up.

1.  **Install Ollama and Pull Llama3:**
    * First, install the Ollama application on your machine from the [official website](https://ollama.com/).
    * Then, pull the `llama3` model by running this command in your terminal:
        ```bash
        ollama pull llama3
        ```

2.  **Install Python Libraries:**
    * Make sure you have a `requirements.txt` file with the following packages:
        ```
        langchain
        langchain-community
        langchain-ollama
        langchain-chroma
        pypdf
        ```
    * Install them using pip:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Provide the PDF:**
    * Place your PDF file, named `arch.pdf`, in the same directory as this `agent.py` script.

---

## Usage

1.  **Run the Script:**
    * Open your terminal in the project's root directory and run the script:
        ```bash
        python agent.py
        ```
    * The first run will take some time to process the PDF and create the `chroma_db` folder. Subsequent runs will be much faster.

2.  **Start Asking Questions:**
    * Once you see the prompt, you can begin asking questions about the content of `arch.pdf`.
    * Type `exit` or `quit` to end the session.

---

## Future Integration

The `app.py` file, which is currently a placeholder, will be updated shortly. This update will introduce a web-based frontend that uses this `agent.py` logic to provide a more user-friendly, graphical chat experience.
