"""
Handles the initialization and basic operations for the ChromaDB vector store.
"""

import chromadb
from config import CHROMA_PATH, COLLECTION_NAME

def get_chroma_collection():
    """Initializes and returns the ChromaDB collection."""
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    return collection