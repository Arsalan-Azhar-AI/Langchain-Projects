# RAG App using DeepSeek-R1

## Overview
The **RAG App (Retrieval-Augmented Generation)** is a powerful application built using **LangChain**, **Hugging Face Hub**, and **Streamlit**. It leverages **DeepSeek-R1** as an LLM model and **FAISS** as a vector database to perform efficient and accurate retrieval-augmented generation of answers from a specified URL. In this project, the chatbot is trained to answer questions specifically related to the **University of Haripur (UOH)** website.

## Features
- Uses **Recursive URL Loader** to scrape and load website data.
- Implements **FAISS** for fast and efficient document search and retrieval.
- Integrates **Hugging Face Hub** to utilize the **DeepSeek-R1** language model.
- Interactive and user-friendly interface built with **Streamlit**.
- Processes questions with prompt templates for accurate responses.
- Efficient text splitting and document embedding using **Hugging Face Bge Embeddings**.

## Architecture
The application follows these main stages:
1. **Data Extraction:** Loads data from the specified URL (UOH website).
2. **Text Splitting:** Splits the extracted data into manageable chunks.
3. **Vector Embedding:** Uses **Hugging Face Bge Embeddings** to embed textual data.
4. **Database Creation:** Stores embedded documents in **FAISS** for fast retrieval.
5. **Response Generation:** Uses **DeepSeek-R1** to generate responses based on the retrieved context.

## Workflow Diagram
```
+-------------------+     +-------------------+     +-------------------------+
| Website Data Load  | --> | Text Splitting      | --> | Embedding with HF Models |
+-------------------+     +-------------------+     +-------------------------+
                                                          |
                     +----------------+     +------------------------+
                     | Vector Storage | --> | RAG Generation (LLM)    |
                     +----------------+     +------------------------+
                                                 |
                                           +----------------+
                                           | User Interface |
                                           +----------------+
```

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rag-app-deepseek.git
   cd rag-app-deepseek
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file and add your Hugging Face API key:
     ```bash
     HUGGING_FACE_KEY=your_hugging_face_api_key
     ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open the app in your browser using the URL provided by Streamlit.
- Enter a query about UOH in the input box.
- The app will generate an accurate and relevant response.

## Example Interaction
```
User: What programs are offered by UOH?
Bot: The University of Haripur offers various undergraduate and graduate programs in diverse fields.
```

## License
This project is licensed under the MIT License.

## Acknowledgements
- **LangChain** for seamless integration of models and chains.
- **Hugging Face Hub** for access to the DeepSeek-R1 model.
- **FAISS** for efficient vector storage and retrieval.
- **Streamlit** for the interactive user interface.

