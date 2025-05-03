from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_groq import ChatGroq

import os

from dotenv import load_dotenv
load_dotenv()
os.environ['HUGGING_FACE_KEY']=os.getenv("HUGGING_FACE_KEY")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")

embedding=HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize_embeddings':True}

)

doc=WebBaseLoader("https://scholar.google.com",header_template={"User-Agent":"Mozilla/5.0"})
doc_loader=doc.load()
doc_splite=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
split_text=doc_splite.split_documents(doc_loader)

db = FAISS.from_documents(split_text, embedding)

model=ChatGroq(model="llama-3.3-70b-versatile")

import chainlit as cl
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory


@cl.on_chat_start
async def on_chat_start():
    retriever = db.as_retriever()
    message_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )
    chain = ConversationalRetrievalChain.from_llm(
        model,
        chain_type="stuff",
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
    )
    cl.user_session.set("chain", chain)



@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")
    cb = cl.AsyncLangchainCallbackHandler()
    res = await chain.acall(message.content, callbacks=[cb])
    answer = res["answer"]
    source_documents = res["source_documents"]
    text_elements = []
    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name)
            )
        source_names = [text_el.name for text_el in text_elements]
        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"
    await cl.Message(content=answer, elements=text_elements).send()

