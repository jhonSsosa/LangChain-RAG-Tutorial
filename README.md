# RAG Project - LangChain

Este repositorio contiene la implementación de un sistema RAG (Retrieval-Augmented Generation) con LangChain y FAISS.

## Descripción
El proyecto implementa una arquitectura RAG utilizando embeddings para indexar y recuperar información relevante antes de generar una respuesta.

## Estructura del Proyecto
```
📁 rag-project/
│── 📄 index_rag.py
│── 📄 query_rag.py
│── 📄 requirements.txt
│── 📄 .env
│── 📄 README.md
```

## Instalación y Configuración

1. Clonar el repositorio
   ```
   git clone https://github.com/jhonSsosa/LangChain-RAG-Tutorial.git
   cd rag-project
   ```

2. Crear un entorno virtual y activarlo
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instalar dependencias
   ```
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno  
   Reemplaza en el archivo .env la clave OpenAI generada del siguiente modo:
   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```

## Uso
Ejecuta el proceso de indexación:
```
python index_rag.py
```
Luego, realiza consultas usando:
```
python query_rag.py
```