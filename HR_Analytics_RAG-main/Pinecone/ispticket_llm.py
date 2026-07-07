import os
import pandas as pd
from pinecone import Pinecone
from google import genai

# ==========================================
# Configuration
# ==========================================
PINECONE_API_KEY = "pcsk_4wWYPf_CCeut52SGVLv4z9jQ23rSde12Dczp3jQgFg2giR8Tsm32Tr3FLKbF7cLYdMdCSY"
INDEX_HOST = "https://inceptezdb-nzq5bbi.svc.aped-4627-b74a.pinecone.io"
NAMESPACE = "isp-tickets"

# Initialize Gemini Client (Picks up GEMINI_API_KEY from environment variables)
# Set it via: export GEMINI_API_KEY="your-api-key"
ai_client = genai.Client()

# Initialize Pinecone Client
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(host=INDEX_HOST)


# ==========================================
# Helper Function: Query Gemini Embedding
# ==========================================
def get_embedding(text: str, model: str = "text-embedding-004") -> list:
    """Generates vector embedding for the query text using Gemini."""
    response = ai_client.models.embed_content(
        model=model,
        contents=text
    )
    return response.embeddings[0].values


# ==========================================
# RAG: Retrieve & Generate
# ==========================================
def query_tickets_and_answer(query_question: str, top_k: int = 3):
    print(f"\n--- User Query: {query_question} ---")

    # 1. Convert the user question to a vector embedding
    # (Ensure you use the same embedding model used during your upsert process)
    query_vector = get_embedding(query_question)

    # 2. Query Pinecone Vector DB
    try:
        query_response = index.query(
            namespace=NAMESPACE,
            vector=query_vector,
            top_k=top_k,
            include_metadata=True,  # Set to True if metadata was stored, otherwise rely on 'text' field in matches
            include_values=False
        )
    except Exception as e:
        print(f"Error querying Pinecone: {e}")
        return

    # 3. Extract and concatenate the retrieved context
    retrieved_texts = []
    print(f"\nFound {len(query_response.matches)} relevant tickets:")

    for match in query_response.matches:
        # If you stored the raw text in the 'text' field (as done in your upsert code)
        # Note: Depending on how `upsert_records` stores payload, you might fetch it from metadata.
        # Assuming standard text payload retrieval:
        ticket_info = match.get('metadata', {}).get('text', 'Ticket details not found in metadata')
        retrieved_texts.append(ticket_info)
        print(f"- Ticket ID: {match.id} (Score: {match.score:.4f})")

    context = "\n\n====================================\n".join(retrieved_texts)

    # 4. Construct the prompt for Gemini
    prompt = f"""
    You are an AI assistant for an ISP helpdesk. Use the retrieved tickets below to answer the user's question accurately. 
    If the answer cannot be found in the context, clearly state that you don't know based on the available tickets.

    Retrieved Tickets Context:
    {context}

    User Question: {query_question}
    Answer:
    """

    # 5. Call Gemini LLM (using gemini-2.5-flash as the standard fast/smart model)
    try:
        response = ai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        print("\n### Gemini Response ###")
        print(response.text)

    except Exception as e:
        print(f"Error generating content from Gemini: {e}")


# ==========================================
# Example Execution
# ==========================================
if __name__ == "__main__":
    # Example question that should trigger retrieval from your ISP tickets database
    sample_question = "What was the resolution for the network outage in the South region?"
    query_tickets_and_answer(sample_question, top_k=2)