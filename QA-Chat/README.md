# Arsalan Chatbot - QA Chatbot using LLaMA3 and Groq

## Overview
Arsalan Chatbot is an AI-powered question-answering (QA) chatbot built using **LLaMA3** and **Groq**. It leverages the power of the **LLaMA 3.3-70B Versatile** model to generate accurate and context-aware responses. The chatbot is designed to handle complex questions by carefully reading and analyzing the input, providing precise answers based on available data.

## Features
- Utilizes **LLaMA3 70B Versatile** model for robust QA capabilities.
- Integrated with **Groq** for efficient inference and response generation.
- Interactive user interface built using **Streamlit**.
- Generates human-like responses with a high degree of accuracy.
- Adjustable response temperature for varied creativity.

## Architecture
The chatbot follows a three-stage pipeline:
1. **Input Handling:** The user enters a question through the Streamlit interface.
2. **Prompt Processing:** The question is formatted and structured using **LangChain's PromptTemplate**.
3. **Response Generation:** The **LLaMA3** model, powered by **Groq**, generates a response that is displayed on the interface.

## Workflow Diagram
Below is the visual representation of the chatbot architecture:

```
+-------------------+    +----------------+    +------------------------+
| User Input (Text) | -> | Prompt Template | -> | LLaMA3 Model (Groq API) |
+-------------------+    +----------------+    +------------------------+
                                       |
                                 +----------------+
                                 | Response Output |
                                 +----------------+
```

## Installation and Setup
1. Clone the repository:
   ```bash
     git clone https://github.com/Arsalan-Azhar-AI/Langchain-Projects.git
   cd QA-Chat
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
   - Create a `.env` file and add your Groq API key:
     ```bash
     GROQ_API_KEY=your_groq_api_key
     ```

5. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open the chatbot in your browser using the URL provided by Streamlit.
- Enter your query in the text input box.
- The chatbot will generate and display the response instantly.

## Code Explanation
The chatbot code follows a simple yet efficient design. The key components are:
- **Prompt Template:** Defines the message format.
- **Model Selection:** Uses the LLaMA3 model via Groq.
- **Response Generation:** Utilizes the `invoke` method to get responses.

## Example Interaction
```
User: What is the capital of France?
Bot: The capital of France is Paris.
```

## License
This project is licensed under the MIT License.

## Acknowledgements
- **LLaMA3 by Groq** for powerful model inference.
- **Streamlit** for the interactive frontend.
- **LangChain** for seamless prompt and response handling.

