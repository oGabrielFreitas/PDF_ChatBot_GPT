import streamlit as st
from scripts import get_answer
import os
os.environ["OPENAI_API_KEY"] = "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"


st.title('TESTE')

prompt = st.text_input('Entre a pergunta')

if prompt:
    answer = get_answer.easy_answer(prompt)
    st.write(answer['result'])
    
    with st.expander('JSON Response'):
        st.write(answer)