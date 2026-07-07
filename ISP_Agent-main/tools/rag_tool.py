# tools/rag_tool.py
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from pinecone import Pinecone
from config.settings import settings
from google import genai
from google.genai import types

ai_client = genai.Client()
llm = ChatGoogleGenerativeAI(model=settings.MODEL_NAME, temperature=0)
#embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-001")
# Set the configuration to match your index size
config = types.EmbedContentConfig(output_dimensionality=1024)

def get_embedding(text: str, model: str = "gemini-embedding-001") -> list:
    """Generates vector embedding for the query text using Gemini."""
    #print("Method:get_embedding")
    response = ai_client.models.embed_content(
        model=model,
        contents=text,
        config=config
    )
    return response.embeddings[0].values

# EXPLICIT CLEAN NAME ASSIGNED HERE
@tool("rag_ticket_resolution_search")
def rag_ticket_resolution_search(query: str) -> str:
    """Useful when the user asks questions about ticket resolutions, how a ticket was fixed,
    troubleshooting details, or descriptions of problems."""
    try:
        #print("Step: rag_ticket_resolution_search")
        pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        index = pc.Index(host=settings.PINECONE_HOST)

        query_vector = get_embedding(query)
        #print("Step: converted the query into embedding")
        response = index.query(
            namespace="isptickets",
            vector=query_vector,
            top_k=3,
            include_metadata=True
        )
        context_chunks = []
        for match in response.get('matches', []):
            metadata = match.get('metadata', {})
            text = metadata.get('text', str(metadata))
            context_chunks.append(text)

        context = "\n---\n".join(context_chunks)
        if not context:
            return "No relevant resolution logs or matching ticket descriptions found in the knowledge base."

        rag_prompt = f"""
                   You are an expert ISP (Internet Service Provider) support agent. 
                   Use the following relevant past tickets to help diagnose and resolve the user's issue. 
                   Pay close attention to the 'Resolution' fields of similar past tickets.

                   User Query: "{query}"

                   Relevant Past Tickets:
                   {context}

                   Based on the historical data above, please provide a helpful, step-by-step brief resolution for the user's current query at the max of 10 lines
                   """
        res = llm.invoke(rag_prompt)
        return res.content

    except Exception as e:
        return f"Error executing Vector Search: {str(e)}"