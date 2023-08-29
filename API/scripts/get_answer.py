# IMPORTS
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
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType


# CONSTANTS
MODEL_NAME = 'gpt-3.5-turbo'
# PERSIST_DIRECTORY = './VectorStore/'
PERSIST_DIRECTORY = '../Oficial/VectorStore/'

# os.environ["OPENAI_API_KEY"] = "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"


# --------------------------------------------------------------------
#       ___                                  _            
#      /   |  ____  ______      _____  _____(_)___  ____ _
#     / /| | / __ \/ ___/ | /| / / _ \/ ___/ / __ \/ __ `/
#    / ___ |/ / / (__  )| |/ |/ /  __/ /  / / / / / /_/ / 
#   /_/  |_/_/ /_/____/ |__/|__/\___/_/  /_/_/ /_/\__, /  
#                                                /____/   
#

# Creates an instance of the llm
def load_llm():
    return OpenAI()

# Opens a persisted vectored data base
def load_vectordb(persist_dir):
    
    embeddings = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])

    persistent_client = chromadb.PersistentClient(path=persist_dir)

    return Chroma(client=persistent_client, embedding_function=embeddings)

# Creates a similarity retriever, using lanchain RetrievalQA
def create_similarity_qa(vector_db, llm):
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k":2})

    return RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)


# DEFAULT ANSWER MODE
# This function just uses Langchain retriever
def easy_answer(query):

    llm = load_llm()
    vectordb = load_vectordb(PERSIST_DIRECTORY)  
    qa = create_similarity_qa(vectordb, llm)
    
    result = qa({"query": query})

    # return result['result']
    return result

# AGENT ANSWER
# This function uses LangChain agent to answer the question.
def agent_answer(query, verbose=False):

    llm = load_llm()
    vectordb = load_vectordb(PERSIST_DIRECTORY)  
    qa = create_similarity_qa(vectordb, llm)

    tools = [Tool(name="QA", func=qa, description="My RetrievalQA tool")] 
    agent = initialize_agent(tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    answer = agent.run(query)

    return answer


# DESCONTINUADO
def easy_answer_old(query):
    llm = OpenAI(model=MODEL_NAME)
    embeddings = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])

    persistent_client = chromadb.PersistentClient(path=PERSIST_DIRECTORY)

    vectordb = Chroma(client=persistent_client, embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":2})

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
    
    result = qa({"query": query})

    # return result['result']
    return result


# DESCONTINUADO
# PODE CONTER ERROS AS VEZES!
# USES LANG CHAIN AGENT TO ANSWER
def agent_answer_old(query):
    llm = OpenAI(model=MODEL_NAME)
    embeddings = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])

    persistent_client = chromadb.PersistentClient(path=PERSIST_DIRECTORY)

    vectordb = Chroma(client=persistent_client, embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":2})

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
    
    tools = [Tool(name="QA", func=qa, description="My RetrievalQA tool")] 
    agent = initialize_agent(tools, OpenAI(), agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    result = agent.run(query)

    return result





# --------------------------------------------------------------------
#       ____                                        __      
#      / __ \____  _______  ______ ___  ___  ____  / /______
#     / / / / __ \/ ___/ / / / __ `__ \/ _ \/ __ \/ __/ ___/
#    / /_/ / /_/ / /__/ /_/ / / / / / /  __/ / / / /_(__  ) 
#   /_____/\____/\___/\__,_/_/ /_/ /_/\___/_/ /_/\__/____/  
#



def pdf_page_splitter():

    return True

def pdf_chunk_splitter():

    return True

def csv_splitter():

    return True

