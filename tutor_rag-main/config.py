"""
Centralizes all your environment variables, model names, and file paths.
"""

import os

# API Keys
GEMINI_API_KEY ="xxxxxx"

# Paths & Directories
CHROMA_PATH = "./chroma_db"
PDF_FOLDER = "./pdfs"
COLLECTION_NAME = "data_engineering_tutor"

# Models
EMBEDDING_MODEL = "gemini-embedding-001"
LLM_MODEL = "gemini-2.5-flash-lite"