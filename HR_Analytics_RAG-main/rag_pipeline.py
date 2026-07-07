"""
Description: This module encapsulates the RAG logic. It connects to the saved database,
searches for the most relevant text chunks when a question is asked, and constructs a prompt for Gemini to answer.

"""
from config import CHROMA_DB_DIR, EMBEDDING_MODEL, LLM_MODEL, RETRIEVER_K
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


class HR_RAG_Pipeline:
    """
    Connects to the vector DB, retrieves relevant HR policy chunks,
    and generates an answer using Gemini.
    """

    def __init__(self):
        # Adding the provided API key
        api_key = "AIzaSyDWeE3S5xm0TXk_IQz1Trn9kxnVYfGbfjo"

        # 1. Setup Embeddings (Must match the model used during ingestion)
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            google_api_key=api_key
        )

        # 2. Connect to the local Chroma Vector DB
        self.vector_store = Chroma(
            persist_directory=CHROMA_DB_DIR,
            embedding_function=self.embeddings
        )

        # 3. Setup the Retriever (fetch top K most relevant chunks)
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K})

        # 4. Initialize Gemini Chat Model
        # Temperature is set low (0.1) so the model remains factual and strictly adheres to the HR policy
        self.llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL,
            google_api_key=api_key,
            temperature=0.1
        )

        # 5. Define the Custom Prompt Template
        system_prompt = """
        You are a professional HR assistant for the company. 
        Use the following pieces of retrieved context from the official HR policy to answer the employee's question. 
        If you cannot find the answer in the provided context, politely state that you do not know based on the current policy. 
        Do not make up or guess information.

        Context: {context}

        Question: {input}

        Helpful Answer:
        """
        self.prompt = PromptTemplate.from_template(system_prompt)

        # 6. Construct the RAG Chain
        self.combine_docs_chain = create_stuff_documents_chain(self.llm, self.prompt)
        self.rag_chain = create_retrieval_chain(self.retriever, self.combine_docs_chain)

    def query(self, user_question: str) -> str:
        """Runs the question through the RAG chain and returns the answer."""
        response = self.rag_chain.invoke({"input": user_question})
        return response["answer"]