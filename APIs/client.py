import streamlit as st
import requests

def use_first_model(input_text):
    response=requests.post("http://localhost:8080/essay/invoke",
    json={'input':{'topic':input_text}})
    print(response.text)
    if response.status_code==200:
        try:
            print(response)
            return response.json()['output']['content']
        except:
            print("Data is not in valid json",response.text)
    else:
        print("Error",response.status_code,response.text)
def use_second_model(input_text):
    response=requests.post("http://localhost:8080/poem/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']

st.title("Client APIs")
input_text1=st.text_input("write an essay here.")
input_text2=st.text_input("write an poem here.")
if input_text1:
    st.write(use_first_model(input_text1))
if input_text2:
    st.write(use_second_model(input_text2))
