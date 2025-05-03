

# 🧠 Scholar AI Agent using LLaMA 3 and FAISS

This project demonstrates the development of a **Conversational AI Agent** that can intelligently retrieve and summarize content from [Google Scholar](https://scholar.google.com) using **LangChain**, **Groq’s LLaMA3-70B**, **FAISS**, and **Hugging Face embeddings**. The agent is deployed using **Chainlit**, allowing real-time user interaction in a chatbot interface.

---

## 🚀 Features

* 💬 **Chat Interface**: Built with Chainlit for interactive conversational experience.
* 🔍 **Source-Based Retrieval**: Retrieves and references segments from Google Scholar.
* 🧠 **LLM Powered**: Uses **LLaMA3-70B** via **Groq** API for high-quality responses.
* 📚 **Embedding & Vector Store**: Utilizes **Hugging Face BAAI/bge-small-en-v1.5** and **FAISS** for fast semantic search.
* 🧩 **Memory Integration**: Uses LangChain’s `ConversationBufferMemory` for context-aware dialogue.

---

## 📦 Tech Stack

| Component       | Tool/Library                      |
| --------------- | --------------------------------- |
| LLM             | `Groq - LLaMA3-70B`               |
| Embedding Model | `HuggingFace - BGE Small English` |
| Document Loader | `LangChain WebBaseLoader`         |
| Vector Store    | `FAISS`                           |
| Framework       | `LangChain`, `Chainlit`           |
| Memory          | `ConversationBufferMemory`        |

---

## 🔧 How It Works

1. **Data Collection**: Scrapes the content of [Google Scholar](https://scholar.google.com) using `WebBaseLoader`.
2. **Preprocessing**: Text is split into smaller chunks using `RecursiveCharacterTextSplitter`.
3. **Vectorization**: Each chunk is embedded using Hugging Face’s BGE model and stored in FAISS.
4. **LLM Interaction**: User queries are handled by the Groq-hosted LLaMA3-70B model.
5. **Retrieval Chain**: A `ConversationalRetrievalChain` fetches the most relevant chunks and constructs context-aware responses.
6. **Frontend**: Real-time chatbot built using Chainlit.

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arsalan-Azhar-AI/Langchain-Projects/RAG_with_Memory.git
   cd app.py
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   Create a `.env` file and add:

   ```env
   HUGGING_FACE_KEY=your_huggingface_key
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the chatbot**

   ```bash
   chainlit run app.py -w
   ```

---


## 📌 Use Cases

* Academic Q\&A based on Google Scholar content
* Retrieval-augmented generation (RAG) demo
* Experimentation with Chainlit + LangChain + FAISS stack
* Real-time LLM-based document query systems

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/arsalanazhar) or check out more of my work on [GitHub](https://github.com/Arsalan-Azhar-AI).

















