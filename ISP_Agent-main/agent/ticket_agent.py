# agent/ticket_agent.py
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings
from tools.rag_tool import rag_ticket_resolution_search
# IMPORT THE NEW INSERT TOOL HERE
from tools.sql_tool import mysql_ticket_metrics_search
from tools.sql_create_ticket import mysql_insert_ticket


# Helper function to scrub structural leaks if they squeak by the parser
def clean_agent_output(output) -> str:
    if isinstance(output, list):
        # Extract the pure text string from the response chunks
        text_parts = [item.get('text', '') for item in output if isinstance(item, dict)]
        return "".join(text_parts).strip()
    return str(output).strip()


def create_isp_agent() -> AgentExecutor:
    # Initialize the core Google Gemini model configured in settings
    llm = ChatGoogleGenerativeAI(model=settings.MODEL_NAME, temperature=0)

    # ADD THE NEW TOOL TO THE ARRAY
    tools = [
        rag_ticket_resolution_search,
        mysql_ticket_metrics_search,
        mysql_insert_ticket
    ]

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an advanced, helpful ISP Ticket System Assistant. 
        You have access to exactly three tools:

        1. rag_ticket_resolution_search: Use this tool ONLY for unstructured or semantic text-based queries, such as:
           - Ticket resolution summaries and how issues were fixed.
           - Troubleshooting instructions or recommendations.
           - Textual descriptions of problems or logs.

        2. mysql_ticket_metrics_search: Use this tool ONLY for structured data queries, such as:
           - Counts of tickets (e.g., "How many tickets...")
           - Specific dates (e.g., "When was ticket 767 created...")
           - Durations, priorities, statuses of specific tickets or groups of tickets.
           - Location-specific or category-specific aggregate statistics.

        3. mysql_insert_ticket: Use this tool ONLY when a user explicitly wants to create, file, log, or open a new support ticket in the system.
           - Important: Before calling this tool, ensure you have collected the core required information from the user: customer_id, location, category, and a description of the issue. 
           - If any mandatory details are missing from the conversation, ask the user for them nicely before invoking the tool.

        Guidelines:
        - Analyze the user query carefully to determine which tool is best.
        - Do not guess if a tool can provide the answer; invoke the tool to get real database facts or perform actions.
        - If you encounter errors or cannot find an answer with either tool, politely inform the user.
        - Provide clean, friendly, natural answers. Do not mention SQL tables, keys, or technical elements.
        CRITICAL CONVERSATIONAL MANDATES:
        - YOU ARE FORBIDDEN FROM ASKING FOR MORE THAN ONE PIECE OF INFORMATION AT A TIME.
        - IF YOU NEED A CUSTOMER ID AND A LOCATION, ASK FOR THE CUSTOMER ID FIRST. 
        - DO NOT DISPLAY BULLETED LISTS OR NUMBERED LISTS TO THE USER WHEN GATHERING TICKET DETAILS.
        - ASK EXACTLY ONE QUESTION, THEN STOP AND WAIT FOR THE USER'S RESPONSE.


        Contextual temporal constraint: The current year is 2026."""),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # NATIVE TOOL-CALLING COMPATIBLE FACTORY
    agent = create_tool_calling_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True
    )