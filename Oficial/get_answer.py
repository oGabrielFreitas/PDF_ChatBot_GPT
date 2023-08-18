# Imports
import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import chromadb


# Constants
MODEL_NAME = 'gpt-3.5-turbo'
PERSIST_DIRECTORY = './VectorStore/'
# PERSIST_DIRECTORY = '../../Oficial/VectorStore/'

os.environ["OPENAI_API_KEY"] = "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"



def Answer_Bot(query):
    llm = OpenAI(model=MODEL_NAME)
    embeddings = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])

    persistent_client = chromadb.PersistentClient(path=PERSIST_DIRECTORY)

    vectordb = Chroma(client=persistent_client, embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":2})

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
    
    result = qa({"query": query})

    return result['result']
    # return result