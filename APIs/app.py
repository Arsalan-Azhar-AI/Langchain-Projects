from fastapi import FastAPI
from langserve import add_routes
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import uvicorn
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
#groq_api_key=os.environ['GROQ_API_KEY']
app=FastAPI(title="fastapi",
            vesion="1.0",
            desciption="Test purpose api app")

llm1 = ChatGroq(model_name='mixtral-8x7b-32768')
prompt1=ChatPromptTemplate.from_template("""
write a hundred word of essay on {topic} 
""")



llm2 = ChatGroq(model_name='mixtral-8x7b-32768')
prompt2=ChatPromptTemplate.from_template("""
write short poem based on the {topic}. i wll give you a reward.
""")


add_routes(
    app,
    prompt1|llm1,
    path="/essay"
)
 
add_routes(
    app,
    prompt2|llm2,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8080)