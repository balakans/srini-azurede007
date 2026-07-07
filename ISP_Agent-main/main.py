import sys
from dotenv import load_dotenv
from agent.ticket_agent import create_isp_agent
# Import HumanMessage and AIMessage to track history structure properly
from langchain_core.messages import HumanMessage, AIMessage


def main():
    print("==================================================")
    print("Initializing Agentic ISP Ticket System...")
    print("==================================================")

    try:
        # Load the unified Agent Executor (the brains of our system)
        agent_executor = create_isp_agent()

        print("\nISP Agentic System is online and ready!")
        print("Type 'exit' or 'quit' to terminate the session.\n")
        print("==================================================")
    except Exception as e:
        print(f"\n[FATAL] System Initialization Failed: {e}")
        sys.exit(1)

    # --- FIX 1: Initialize an empty list to track conversation history ---
    chat_history = []

    while True:
        try:
            # Gather user query from the command prompt
            user_input = input("\nUser: ").strip()

            # Check for exit instructions
            if user_input.lower() in ['exit', 'quit']:
                print("Shutting down ISP Agent. Goodbye!")
                break

            if not user_input:
                continue

            # --- FIX 2: Pass both the user input AND the running chat_history ---
            response = agent_executor.invoke({
                "input": user_input,
                "chat_history": chat_history
            })

            agent_output = response['output']
            # DOUBLE SANITIZATION: If the output still looks like a raw string representation of a list, clean it
            if isinstance(agent_output, str) and agent_output.startswith("[{'type':"):
                try:
                    import ast
                    parsed_list = ast.literal_eval(agent_output)
                    agent_output = "".join([item.get('text', '') for item in parsed_list if isinstance(item, dict)])
                except:
                    pass

            print(f"\nAgent: {agent_output}")

            # --- FIX 3: Record the turn into memory for the next loop execution ---
            chat_history.append(HumanMessage(content=user_input))
            chat_history.append(AIMessage(content=agent_output))

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Shutting down ISP Agent safely.")
            break
        except Exception as e:
            print(f"\n[ERROR] An execution error occurred: {e}")


if __name__ == "__main__":
    # Ensure environment variables are loaded from the filesystem
    load_dotenv()
    main()