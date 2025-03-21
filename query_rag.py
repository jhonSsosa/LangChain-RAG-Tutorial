import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("⚠️ No se encontró la clave de API de OpenAI. Configúrala en un archivo .env o como variable de entorno.")

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.load_local("vectorstore/", embeddings, allow_dangerous_deserialization=True)

def query_rag(query):
    results = vectorstore.similarity_search(query, k=3)
    for idx, doc in enumerate(results):
        print(f"\n🔹 Resultado {idx+1}:")
        print(doc.page_content)

if __name__ == "__main__":
    user_query = input("🔎 Ingresa tu pregunta: ")
    query_rag(user_query)

