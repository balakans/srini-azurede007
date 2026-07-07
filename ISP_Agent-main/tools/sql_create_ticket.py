# tools/sql_tool.py
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from config.settings import settings
from sqlalchemy import text

llm = ChatGoogleGenerativeAI(model=settings.MODEL_NAME, temperature=0)

# --- NEW INSERT TICKET TOOL ---
@tool("mysql_insert_ticket")
def mysql_insert_ticket(
        customer_id: str,
        location: str,
        category: str,
        description: str,
        status: str = "Open",
        priority: str = "Medium",
        service_type: str = "Standard"
) -> str:
    """
    Useful to create, insert, or log a new support ticket into the MySQL database.
    Use this when a user wants to file a new complaint, issue, or request.

    Args:
        customer_id: The unique identifier of the customer.
        location: The physical or regional location related to the issue.
        category: The category of the issue (e.g., Billing, Connectivity, Hardware).
        description: A detailed description of the customer's issue.
        status: The initial status of the ticket. Defaults to 'Open'.
        priority: The priority level (e.g., Low, Medium, High, Critical). Defaults to 'Medium'.
        service_type: The type of service impacted. Defaults to 'Standard'.
    """
    try:
        # Initialize database connection
        db = SQLDatabase.from_uri(settings.MYSQL_URI)

        # 1. Define a parameterized SQL statement to prevent SQL Injection
        query = text("""
            INSERT INTO isp_ticket (
                customer_id, location, category, description, 
                status, priority, service_type, created_date
            ) VALUES (
                :customer_id, :location, :category, :description, 
                :status, :priority, :service_type, NOW()
            );
        """)

        # 2. Bind parameters tightly to the execution
        params = {
            "customer_id": customer_id,
            "location": location,
            "category": category,
            "description": description,
            "status": status,
            "priority": priority,
            "service_type": service_type
        }

        # 3. Execute using LangChain's underlying SQLAlchemy engine
        with db._engine.begin() as connection:
            result = connection.execute(query, params)
            # Capture the auto-generated ID from the cursor
            new_ticket_id = result.lastrowid

        return f"Success: New ticket successfully created. Ticket ID: {new_ticket_id}."

    except Exception as e:
        return f"Error creating new ticket in database: {str(e)}"