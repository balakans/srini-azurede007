from google import genai
from database import get_chroma_collection
import chromadb

def rag_tutor(question):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="data_engineering_tutor")

    client = genai.Client(api_key="AIzaSyDWeE3S5xm0TXk_IQz1Trn9kxnVYfGbfjo")

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question
    )

    query_embedding = response.embeddings[0].values

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=4
    )

    contexts = results['documents'][0]

    # send it to llm and get the data formatted and rephrased

    client = genai.Client(api_key="AIzaSyDWeE3S5xm0TXk_IQz1Trn9kxnVYfGbfjo")
    context_text = "\n\n".join(contexts)

    prompt = f"""
        You are an expert Python Tutor.

        Use ONLY the provided context to answer the question.

        Retrieved Context:
        {context_text}

        Question:    
        {question}

        Rules:
        Answer strictly from the provided context.
        Do not use external knowledge or assumptions.
        If the context is insufficient, clearly state that the answer is not available in the provided materials.
        Provide concise and accurate explanations.
        Include examples only when available in the context.

        Answer:
        """
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    print("================LLM Output==============")
    print(response.text)

if __name__ == "__main__":
    q = input("Enter question: ")
    rag_tutor(q)
"""
1. Get the question from user
2. 
"""