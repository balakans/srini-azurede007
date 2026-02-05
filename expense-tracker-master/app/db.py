import mysql.connector
import os
from dotenv import load_dotenv
from utils import logger

# Load environment variables
load_dotenv()

# ==========================
# Database Connection
# ==========================
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        logger.info("Database connection established")
        return conn
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise

# ==========================
# Insert Expense Method
# ==========================
def insert_expense(description: str, amount: float, date: str, category_id: int = None):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (description, amount, date, category_id) VALUES (%s, %s, %s, %s)",
            (description, amount, date, category_id)
        )
        conn.commit()
        logger.info(f"Inserted expense: {description}, {amount}, {date}, category={category_id}")
        return True
    except Exception as e:
        logger.error(f"Error inserting expense: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ==========================
# Get All Expenses Method
# ==========================
def fetch_expenses():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT e.id, e.description, e.amount, e.date, 
                   c.name AS category
            FROM expenses e
            LEFT JOIN expense_categories c ON e.category_id = c.id
            ORDER BY e.date DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        logger.info(f"Fetched {len(rows)} expenses")
        return rows
    except Exception as e:
        logger.error(f"Error fetching expenses: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ==========================
# Delete Expense by Id Method
# ==========================
def delete_expense(expense_id: int):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id=%s", (expense_id,))
        conn.commit()
        affected = cursor.rowcount
        if affected > 0:
            logger.info(f"Deleted expense ID={expense_id}")
        else:
            logger.warning(f"No expense found with ID={expense_id}")
        return affected > 0
    except Exception as e:
        logger.error(f"Error deleting expense {expense_id}: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# ==========================
# Get All Expense Category Methods
# ==========================

def fetch_categories():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM expense_categories ORDER BY name ASC")
        rows = cursor.fetchall()
        logger.info(f"Fetched {len(rows)} categories")
        return rows
    except Exception as e:
        logger.error(f"Error fetching categories: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":

    #Insert Method
    insert_expense("Travel to hometown",2000,'2025-08-20',1)
    print("Record Inserted")

    #Insert Method
    records = fetch_expenses()
    print(records)

    #Delete Method
    delete_expense(1)
    print("Record Deleted")

    #get category Method
    cat = fetch_categories()
    print(cat)

