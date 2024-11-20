import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embedding model and vector database
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory="data/chroma", embedding_function=embedding_model)

def add_document_to_chroma(file_path: str):
    """
    Read a document and add its embeddings to the vector database.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            vector_db.add_texts([content])
            print(f"Document '{file_path}' added to vector database.")
    except Exception as e:
        print(f"Error adding document '{file_path}': {e}")

def add_documents_from_directory(directory: str):
    """
    Add all text documents from a directory to the Chroma vector database.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # You can extend this to support PDFs or other formats
            file_path = os.path.join(directory, filename)
            add_document_to_chroma(file_path)

def search_similar_embeddings(query: str):
    """
    Perform a similarity search on the vector database.
    """
    try:
        results = vector_db.similarity_search(query)
        if results:
            return results[0].metadata.get("chunk", "No metadata chunk found")
        return "No similar documents found."
    except Exception as e:
        return f"Error in similarity search: {e}"
