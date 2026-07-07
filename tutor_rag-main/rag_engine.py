"""
Handles semantic retrieval, adaptive prompt engineering, and LLM generation.
"""
from google import genai  # <--- 1. Updated import
from config import GEMINI_API_KEY, LLM_MODEL, EMBEDDING_MODEL
from database import get_chroma_collection

# 2. Initialize the standard Client
client = genai.Client(api_key=GEMINI_API_KEY)


def retrieve_context(question, top_k=3):
    """Embeds the question and searches ChromaDB for the closest semantic chunks."""
    collection = get_chroma_collection()

    # 3. Updated to use the new SDK client syntax for embeddings
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=question
    )
    question_embedding = response.embeddings[0].values

    # Query ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )
    print("===========")
    print(results)
    print("===========")

    # Flatten and return the document chunks
    if results['documents']:
        return results['documents'][0]
    return []


def build_prompt(question, contexts, student_profile):
    """Builds a customized prompt based on the retrieved context and student profile."""
    context_text = "\n\n".join(contexts)

    prompt = f"""
    You are an expert Data Engineering Tutor.

    Use ONLY the provided context to answer the question.

    Context:
    {context_text}

    Question:
    {question}

    Answer:
    """
    return prompt


def ask_tutor(question, student_profile):
    """The main RAG pipeline: Retrieve -> Prompt -> Generate."""
    contexts = retrieve_context(question)

    if not contexts:
        return "I couldn't find any relevant information in the uploaded documents to answer that."

    prompt = build_prompt(question, contexts, student_profile)

    # 4. Corrected generation syntax using the client object directly
    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt
    )

    return response.text