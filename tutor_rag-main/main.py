from ingestion import process_and_ingest_documents
from rag_engine import ask_tutor
from logger import log_question


def main():
    # 1. (Optional) Run Ingestion
    # Uncomment the line below to process PDFs in the ./data folder on first run
    # process_and_ingest_documents()

    # 2. Define the Learner Profile
    student_profile = {
        "name": "Raj",
        "skill_level": "Advanced",  # Changed to Advanced for complex topics
        "focus_area": "Data Engineering"
    }

    # 3. Sample Data Engineering Questions
    sample_questions = [
        "SCD Types"
    ]

    # 4. Interactive or Batch Querying
    print(f"--- Starting Tutor Session for {student_profile['name']} ---\n")

    for question in sample_questions:
        print(f"Q: {question}")

        # Log it
        log_question(question)

        # Get Answer
        answer = ask_tutor(question, student_profile)
        print(f"A: {answer}\n")
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()