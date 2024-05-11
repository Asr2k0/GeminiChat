from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st


import os

from dotenv import load_dotenv
load_dotenv()
# print(os.getenv("GOOGLE_API_KEY"))
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
# ## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Your a bot and your name is Askme"),
        ("user","Question:{question}")
    ]
)
st.title('Langchain Demo With Google Gemini API')
input_text=st.text_input("Ask me anything ! ")


llm = ChatGoogleGenerativeAI(model="gemini-pro")

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
