import os
import requests
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Secure API key from environment variables
GEMANAI_API_KEY = os.getenv("GEMANAI_API_KEY")
GEMANAI_API_URL = "https://api.gemanai.com/v1/completions"  # Replace with the actual GemanAI API URL

if not GEMANAI_API_KEY:
    raise ValueError("GEMANAI_API_KEY not found in environment variables.")

# Set up HuggingFace embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Set up Chroma vector store for document embeddings
vector_db = Chroma(persist_directory="data/chroma", embedding_function=embedding_model)


def get_gemanai_response(prompt: str):
    """
    Send a prompt to GemanAI API and get a response.
    """
    headers = {
        "Authorization": f"Bearer {GEMANAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "text-davinci-003",  # Update to your preferred model
        "prompt": prompt,
        "max_tokens": 100,
    }

    try:
        response = requests.post(GEMANAI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("choices", [])[0].get("text", "No response text available")
    except requests.RequestException as e:
        return f"Error: {e}"


def generate_embeddings(text: str):
    """
    Generate embeddings for the provided text using HuggingFace model.
    """
    try:
        return embedding_model.embed_query(text)
    except Exception as e:
        return f"Error generating embeddings: {e}"


def similarity_search(query: str):
    """
    Perform a similarity search in the vector database.
    """
    try:
        results = vector_db.similarity_search(query)
        if results:
            return results[0].metadata.get("chunk", "No metadata chunk available")
        return "No similar documents found."
    except Exception as e:
        return f"Error in similarity search: {e}"
