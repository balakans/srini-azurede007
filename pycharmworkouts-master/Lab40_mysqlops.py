import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename='app.log',format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO) #DEBUG, INFO, WARNING, ERROR, CRITICAL

def create_connection():
    """Create and return a database connection."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_SERVERNAME"),
            user=os.getenv("MYSQL_USERNAME"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DBNAME")
        )
        if conn.is_connected():
            print("Database connection established.")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_all_databases(conn):
    """Fetch and display all databases."""
    if not conn:
        print("No database connection.")
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            dbs = cursor.fetchall()
            print("=== Database List ===")
            for db in dbs:
                print(db)
    except Error as e:
        print(f"Error fetching databases: {e}")

def get_all_tables(conn):
    """Fetch and display all tables."""
    if not conn:
        print("No database connection.")
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tbls = cursor.fetchall()
            print("=== Table List ===")
            for t in tbls:
                print(t)
    except Error as e:
        print(f"Error fetching tables: {e}")

def get_table_data(conn, tablename):
    """Fetch and display data from a specific table."""
    if not conn:
        print("No database connection.")
        return
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM `{tablename}`"
            cursor.execute(query)
            rows = cursor.fetchall()
            print(f"=== Table Data: {tablename} ===")
            for row in rows:
                print(row)
    except Error as e:
        print(f"Error fetching table data: {e}")

def insert_customer_data(conn, custid, fname, lname, age, prof):
    """Insert a record into tblcustomer."""
    if not conn:
        print("No database connection.")
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO tblcustomer (custid, fname, lname, age, profession) VALUES (%s, %s, %s, %s, %s)", (custid, fname, lname, age, prof))
            conn.commit()
            print("Record inserted successfully.")
    except Error as e:
        print(f"Error inserting customer data: {e}")

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        logging.info("Database Connection Success!")
        get_all_databases(conn)
        get_all_tables(conn)
        get_table_data(conn, "tblcustomer")
        insert_customer_data(conn, 1006, "Manoj", "Prabakar", 35, "Sports")
        logging.info("Record Inserted")
        conn.close()
        print("Database connection closed.")
        logging.info("Database connection closed")