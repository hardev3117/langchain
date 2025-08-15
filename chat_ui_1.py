# streamlit_app.py
import streamlit as st
from chat_prompt_template_5 import chat_with_llm
import sys
import os

# Add root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
st.title("IntelliChat for Your Domain")

# Input fields
domain = st.text_input("Enter Domain Name")
topic = st.text_input("Enter Topic")

# Submit button
if st.button("Submit"):
    # Backend logic here
    result = chat_with_llm(domain, topic)
    st.success(f"{result}")
    
    #
