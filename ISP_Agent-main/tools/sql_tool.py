# tools/sql_tool.py
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from config.settings import settings
from sqlalchemy import text

llm = ChatGoogleGenerativeAI(model=settings.MODEL_NAME, temperature=0)


# EXPLICIT CLEAN NAME ASSIGNED HERE
@tool("mysql_ticket_metrics_search")
def mysql_ticket_metrics_search(query: str) -> str:
    """Useful when the user asks about ticket metrics, counts, durations, created dates,
    or specific statuses of individual tickets."""
    try:
        #print("Step: mysql_ticket_metrics_search")


        sql_generation_prompt = f"""
        You are a MySQL expert. Given an input question, create a syntactically correct MySQL query to run.
        The primary table name is assumed to be `isp_ticket`. 

        Target Schema Reference:
        - ticket_id (INT)
        - customer_id (VARCHAR)
        - location (VARCHAR)
        - category (VARCHAR)
        - description (TEXT)
        - status (VARCHAR)
        - priority (VARCHAR)
        - service_type (VARCHAR)
        - escalation_category (VARCHAR)
        - created_date (DATE/DATETIME)
        - resolution (TEXT)

        Contextual temporal constraints: The current year is 2026.

        Question: {query}
        SQL Query (Return ONLY the raw SQL string. Do NOT wrap it in markdown code blocks, do not include line breaks inside the string, just return the raw SQL sentence):"""

        generated_sql = llm.invoke(sql_generation_prompt).content.strip()
        #print(generated_sql)
        #print(settings.MYSQL_URI)
        db = SQLDatabase.from_uri(settings.MYSQL_URI)

        if "```" in generated_sql:
            parts = generated_sql.split("```")
            if len(parts) >= 3:
                generated_sql = parts[1]
            else:
                generated_sql = parts[0]

        if generated_sql.lower().startswith("sql"):
            generated_sql = generated_sql[3:]

        generated_sql = generated_sql.strip()
        db_result = db.run(generated_sql)

        if not db_result:
            return f"The query executed successfully but returned no records from the database. (SQL: {generated_sql})"

        synthesis_prompt = f"""Given the user question, the generated SQL query, and the database execution result, 
        write a natural language response answering the user clearly. Do not mention technical terms like 'tuples' or 'rows' to the user.

        Question: {query}
        SQL Query: {generated_sql}
        Database Result: {db_result}
        Response:"""

        res = llm.invoke(synthesis_prompt)
        return res.content

    except Exception as e:
        return f"Error executing SQL Database Search: {str(e)}"

