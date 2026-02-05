import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="dboperations.log",  # Log file name
    level=logging.INFO,           # INFO, DEBUG, ERROR
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#method
def addnum(a,b):
    return a + b

#varible
dbinfo = "MySQL"

#class
class DBOperations:
    def __init__(self):
        try:
            host = os.getenv("DB_HOST")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            database = os.getenv("DB_NAME")

            if not all([host, user, password, database]):
                raise ValueError("One or more required DB environment variables are missing.")

            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            logging.info("Database connection established successfully.")

        except Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise
        except Exception as ex:
            logging.error(f"Unexpected error: {ex}")
            raise

    def getall_databases(self):
        try:
            logging.info("Fetching all databases...")
            self.cursor.execute("SHOW DATABASES")
            dbs = self.cursor.fetchall()
            for db in dbs:
                print(db)
            logging.info("Databases fetched successfully.")
        except Error as e:
            logging.error(f"Error fetching databases: {e}")

    def getall_tables(self):
        try:
            logging.info("Fetching all tables...")
            self.cursor.execute("SHOW TABLES")
            tbls = self.cursor.fetchall()
            for t in tbls:
                print(t)
            logging.info("Tables fetched successfully.")
        except Error as e:
            logging.error(f"Error fetching tables: {e}")

    def insert_customer(self, cust_data):
        try:
            insert_sql = """
            INSERT INTO tblcustomer (custid, fname, lname, age, profession)
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.executemany(insert_sql, cust_data)
            self.conn.commit()
            logging.info(f"Inserted {self.cursor.rowcount} customer records successfully.")
        except Error as e:
            logging.error(f"Error inserting customer data: {e}")

    def execute_query(self, query, params=None):
        try:
            logging.info(f"Executing query: {query}")
            self.cursor.execute(query, params or ())
            results = self.cursor.fetchall()
            logging.info("Query executed successfully.")
            return results
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return None

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
            logging.info("Database connection closed.")
        except Error as e:
            logging.error(f"Error closing database connection: {e}")

class MySQLDatabase(DBOperations):

    def getdatabaseinfo(self):
        print("This is mysql server")