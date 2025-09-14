# LangChain

This project demonstrates two powerful applications of the LangChain library:

1.  **Conversational Q\&A with Documents**: An interactive chat application that allows you to "talk" to your documents. You can upload a PDF, and the application will answer your questions based on its content.
2.  **YouTube Video Summarization**: A tool that takes a YouTube video URL and generates a concise summary of its content.

This project is an excellent starting point for anyone looking to build applications with large language models and custom data sources.

-----

## 📜 Project Overview

This repository contains two Python scripts that showcase how to use LangChain for different purposes:

  * **`app.py`**: A conversational AI that uses a Retrieval-Augmented Generation (RAG) approach to answer questions from a PDF document. It processes the document, creates a searchable vector store, and uses a conversational retrieval chain to provide context-aware answers.
  * **`app2.py`**: A video summarizer that fetches the transcript of a YouTube video, splits it into manageable chunks, and uses a summarization chain to create a summary of the content.

-----

## 🚀 Features

  * **Document Q\&A**:
      * Load and process PDF documents.
      * Ask questions in natural language and get answers based on the document's content.
      * Maintains a conversation history to answer follow-up questions.
  * **YouTube Summarizer**:
      * Provide a YouTube URL and get a summary of the video.
      * Uses a map-reduce approach to handle long video transcripts.
  * **Powered by LangChain and OpenAI**: Leverages state-of-the-art language models for high-quality responses.

-----

## 🛠️ Technologies Used

  * **Python**: The core programming language for the project.
  * **LangChain**: A framework for developing applications powered by language models.
  * **OpenAI**: Used for generating text embeddings and powering the language models.
  * **FAISS**: A library for efficient similarity search and clustering of dense vectors.
  * **PyPDF**: A library for reading and extracting text from PDF files.
  * **YouTube Transcript API**: For fetching transcripts of YouTube videos.

-----

## ⚙️ Setup and Installation

To get a local copy up and running, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/langchain-project.git
    cd langchain-project
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your environment variables:**
      * Create a `.env` file in the root of the project.
      * Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        ```
4.  **For the Document Q\&A (`app.py`):**
      * Place the PDF file you want to use in the project directory.
      * Update the `pdf_path` variable in `app.py` to the name of your PDF file.
5.  **Run the application:**
      * To run the Document Q\&A app:
        ```bash
        python app.py
        ```
      * To run the YouTube Summarizer:
        ```bash
        python app2.py
        ```

-----

## 📂 File Structure

```
LangChain/
├── app.py              # Main script for the Document Q&A application
├── app2.py             # Script for the YouTube video summarizer
├── requirements.txt    # A list of all the Python packages required
└── README.md           # This file
```

-----

## 📄 License

This project is open source and available under the MIT License.
