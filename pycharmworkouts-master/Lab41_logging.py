#pip install mysql-connector-python
#pip install python-dotenv
import mysql.connector
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename='mysql_query.log',level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",filemode="a") #DEBUG, INFO, WARNING, ERROR, CRITICAL

conn = None

try:
    conn = mysql.connector.connect(host=os.getenv("MYSQL_SERVERNAME"),
                                   user=os.getenv("MYSQL_USERNAME"),
                                   password=os.getenv("MYSQL_PASSWORD"),
                                   database=os.getenv("MYSQL_DBNAME"))
    logging.info("Connection successfully created")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblcustomer")
    results = cursor.fetchall()
    print("Total Rows:",cursor.rowcount)
    logging.info(f"Total Rows:{cursor.rowcount}")
    print("================")
    for row in results:

        print("CustId:",row[0])
        print("FirstName:", row[1])
        print("LastName:", row[2])
        print("Age:", row[3])
        print("Profession:", row[4])
        print("================")
        logging.info("Custid:" + str(row[0]))
except Exception as e:
    print("Error:", e)
    logging.error("Error:", e)
finally:
    if conn != None:
        cursor.close()
        conn.close()
        print("Connection closed.")
        logging.info("Database Connection closed.")


