import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# File Paths
DOC_PATH = "data/hr_policy.pdf"
CHROMA_DB_DIR = "vector_db"

# Model Configurations
# Gemini 1.5 Flash is highly efficient and optimal for RAG tasks
LLM_MODEL = "gemini-3.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

# Vector Search Configurations
# k = number of documents to retrieve per query
RETRIEVER_K = 3