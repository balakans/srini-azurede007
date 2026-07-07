"""

Description: This is your application's entry point, featuring a clean terminal interface for continuous chatting.

"""

import os
from rag_pipeline import HR_RAG_Pipeline


def main():
    """
    Entry point for the HR Q&A Chatbot.
    """
    # Safety Check: Ensure the database exists
    if not os.path.exists("vector_db"):
        print("Error: Vector DB not found. Please run 'ingest.py' first.")
        return

    print("⏳ Starting HR Assistant... Connecting to Database and AI.")
    hr_bot = HR_RAG_Pipeline()

    print("\n" + "=" * 50)
    print("Welcome to the HR Policy Chatbot!")
    print("Ask any question regarding company policy.")
    print("Type 'exit', 'quit', or 'q' to stop.")
    print("=" * 50 + "\n")

    while True:
        user_input = input("👤 Employee: ")

        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Goodbye!")
            break

        if not user_input.strip():
            continue

        print(" Processing...")
        try:
            # Get the answer from the RAG Pipeline
            answer = hr_bot.query(user_input)
            print(f"\n💼 HR Bot:\n{answer}\n")
        except Exception as e:
            print(f"\n An error occurred: {e}\n")

        print("-" * 50)


if __name__ == "__main__":
    main()