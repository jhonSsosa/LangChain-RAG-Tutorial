from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/documento.txt", encoding="utf-8")
documents = loader.load()
