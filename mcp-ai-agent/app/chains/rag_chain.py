from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


def build_rag_chain(documents):
    vector_store = FAISS.from_documents(documents, OpenAIEmbeddings())
    chain = RetrievalQA.from_chain_type(llm=None, chain_type="stuff", retriever=vector_store.as_retriever())
    return chain
