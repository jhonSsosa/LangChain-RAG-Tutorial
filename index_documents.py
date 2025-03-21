from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from load_documents import documents

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(documents, embeddings)

vectorstore.save_local("faiss_index")
print("Índice FAISS guardado correctamente.")

