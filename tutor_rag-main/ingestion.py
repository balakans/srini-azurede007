"""
Contains all functions related to reading PDFs, chunking text, generating embeddings, and loading them into the vector database.
   Step 1: Read each pdf file in the folder pdfs
   step 2: Extract text from pdf file
   Step 3: Split text into chunks
   Step 4: Convert the chunks to embeddings
   Step 5: Ingest embeddings into vector database

"""

import os
from google import genai # <--- 1. Updated import
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import GEMINI_API_KEY, PDF_FOLDER, EMBEDDING_MODEL
from database import get_chroma_collection

# 2. Initialize the new Client instead of configuring a global state
client = genai.Client(api_key=GEMINI_API_KEY)


def read_pdf(pdf_path):
    """Extracts text from a single PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text


def generate_embedding(text):
    """Generates a vector embedding for a given string using the new Gemini SDK."""
    # 3. Call embed_content on client.models and use 'contents' parameter
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    # 4. Extract the list of floats from the new response object structure
    return response.embeddings[0].values


def process_and_ingest_documents():
    """Reads all PDFs in the data folder, chunks them, and stores them in ChromaDB."""
    if not os.path.exists(PDF_FOLDER):
        print(f"Directory {PDF_FOLDER} not found. Please create it and add PDFs.")
        return

    collection = get_chroma_collection()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, file)
            print(f"Processing: {file}...")

            text = read_pdf(pdf_path)
            if not text:
                continue

            chunks = splitter.split_text(text)

            for idx, chunk in enumerate(chunks):
                embedding = generate_embedding(chunk)

                collection.add(
                    ids=[f"{file}_{idx}"],
                    documents=[chunk],
                    embeddings=[embedding],
                    metadatas=[{"source": file}]
                )

    print(f"Ingestion complete. Total documents in DB: {collection.count()}")

if __name__ == "__main__":
    process_and_ingest_documents()