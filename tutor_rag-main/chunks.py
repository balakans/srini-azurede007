
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from database import get_chroma_collection

#Read from PDF document
reader = PdfReader("pdfs/01_Inceptez_Python.pdf")
text = ""
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        text += extracted

splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

chunks = splitter.split_text(text)
collection = get_chroma_collection()
client = genai.Client(api_key="xxx")
for idx, chunk in enumerate(chunks):
    response =  client.models.embed_content(model="gemini-embedding-001",contents=chunk)
    embedding = response.embeddings[0].values

    collection.add(ids=[f"python_{idx}"],
                    documents=[chunk],
                    embeddings=[embedding],
                    metadatas=[{"source": "pythondoc","topic":"python"}]
                )
    print(f"Chunks {idx}  stored in Chorma Vector Database")

    """
    Step 1: Read the pdf file and extract text from it
    Step 2: Split text into chunks
    Step 3: Convert the chunks to embeddings
    Step 4: Ingest embeddings into vector database
    """










