import streamlit as st
from scripts import get_answer
import os
os.environ["OPENAI_API_KEY"] = "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"

from pathlib import Path
from langchain.document_loaders import PyPDFLoader
import io


UPLOADS_DIR = './uploads'


st.title('Market AI')



# ---------------------------------------------------------------------------


# Formulário para enviar arquivo PDF
with st.form(key="Form :", clear_on_submit = True):
    File = st.file_uploader("Faça upload do seu arquivo PDF", type=['pdf', 'csv'])
    Submit = st.form_submit_button(label='Enviar e Processar')
    

# Botão enviar
if Submit :
    save_path = Path(UPLOADS_DIR, File.name)

    # Se o arquivo já existir, emite um alerta
    if save_path.exists():
        st.info('Este arquivo é repetido e já foi processado uma vez! Por favor escolha outro arquivo!', icon="ℹ️")
        st.info(f'Path: {save_path}', icon="ℹ️")

    # Se o arquivo ainda não existir, salva ele no ChromaDB
    else:
        # Salva o arquivo
        with open(save_path, mode='wb') as w:
            w.write(File.getvalue())

        # Chama a função da API do ChromaDB
        processed = get_answer.pdf_page_splitter(f'{save_path}')
                
        # 
        if save_path.exists():
            st.success(f'O arquivo {File.name} foi enviado com sucesso!', icon="✅")

        if processed:
            st.success(f'O arquivo {File.name} foi processado com sucesso!', icon="✅")
        else:
            st.error('Ocorreu um erro ao processar o arquivo', icon="🚨")


# ---------------------------------------------------------------------------


prompt = st.text_input('Entre a pergunta')

if prompt:
    answer = get_answer.easy_answer(prompt)
    st.write(answer['result'])
    
    with st.expander('JSON Response'):
        st.write(answer)