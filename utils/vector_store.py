from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

def create_chroma_vectorstore(folder_path="data/docs"):
    loader = TextLoader(os.path.join(folder_path, "market_risks.txt"))
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="./chroma_index")
    vectorstore.persist()
    return vectorstore

def search_risks(query):
    vectorstore = Chroma(persist_directory="./chroma_index", embedding_function=OpenAIEmbeddings())
    result = vectorstore.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in result])
