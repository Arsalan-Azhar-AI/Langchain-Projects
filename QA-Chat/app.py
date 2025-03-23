from groq import Groq
from langchain_core.prompts import ChatPromptTemplate
import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
Groq_api_key=os.getenv("GROQ_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']='true'
prompts=ChatPromptTemplate.from_messages([
    ("system","Please read the question carefully and answer based on exact data"),
    ("user","Question:{question}")
])

groq_llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=Groq_api_key,temperature=0.9)

st.title("Arsalan Chatbot")
input_text=st.text_input("Enter you want to search here")

str_output_parser=StrOutputParser()

chain=prompts|groq_llm|str_output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
