from groq import Groq
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
Groq_api_key=os.getenv("GROQ_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='true'
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
'''
prompts=ChatPromptTemplate.from_messages([
    ("system","Please read the question carefully and answer based on exact data.{chat_history}"),
    ("user","Question:{question}")
])
'''
prompt_template = PromptTemplate(
    input_variables=["chat_history", "question"],  # Include chat history
    template="""You are an AI assistant. Here is the conversation history:  
    {chat_history}  

    Now, answer the following question based on the above context:  
    {question}
    """
)
groq_llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=Groq_api_key,temperature=0.9)

st.title("Arsalan Chatbot")
input_text=st.text_input("Enter you want to search here")

str_output_parser=StrOutputParser()

#chain=prompts|groq_llm|memory|str_output_parser
chain=LLMChain(llm=groq_llm,
    prompt=prompt_template,
    memory=memory)
if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response['text'])
