from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFaceHub
import os
import streamlit as st
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
hugging_face_api=os.getenv('HUGGING_FACE_KEY')


os.environ['HUGGINGFACEHUB_API_TOKEN']=hugging_face_api
embedding=HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize_embeddings':True}

)

if "vector" not in st.session_state:
    st.session_state.loader_content=RecursiveUrlLoader(url="https://www.uoh.edu.pk",
                                   max_depth=2,
                                   headers={"User-Agent":"Mozilla/5.0"})

    st.session_state.loaded_document=st.session_state.loader_content.load()
    st.session_state.splitted_text=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    st.session_state.text_document=st.session_state.splitted_text.split_documents(st.session_state.loaded_document)
    st.session_state.db_data=FAISS.from_documents(documents=st.session_state.text_document[:120],embedding=embedding)
    retrieval=st.session_state.db_data.as_retriever()


prompt_template="""
please provide most relavent and accuracte result based on the data you recived

{context}

Question:{question}
"""
prompt=PromptTemplate(template=prompt_template,input_variables=['context','question'])


hf=HuggingFaceHub(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    model_kwargs={"temperature":0.1,"max_length":500}

)


from langchain.chains import RetrievalQA
RetrievalQA_chain=RetrievalQA.from_chain_type(
    llm=hf,
    chain_type="stuff",
    retriever=retrieval,
    chain_type_kwargs={"prompt":prompt},
    return_source_documents=False
)

st.title("RAG APP USING DEEPSEEKR1")
input_text=st.text_input("Enter about UOH")

if input_text:
    response=RetrievalQA_chain.invoke({"query":input_text})
    st.write(response['result'].split("Answer:")[1])



