import os
from index_documents import *
from query_rag import *

print("Sistema RAG Listo. Puedes hacer consultas.")
query = input("Pregunta: ")
response = qa_chain.run(query)
print("Respuesta:", response)
