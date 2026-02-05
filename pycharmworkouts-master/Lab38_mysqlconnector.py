#pip install mysql-connector-python

import mysql.connector

conn = None
try:
    conn = mysql.connector.connect(host="103.86.177.4",user="kbnhzraf_retail",password="Inspire123$",database="kbnhzraf_ticketdb")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblcustomer")
    results = cursor.fetchall()
    print("Total Rows:",cursor.rowcount)
    print("================")
    for row in results:

        print("CustId:",row[0])
        print("FirstName:", row[1])
        print("LastName:", row[2])
        print("Age:", row[3])
        print("Profession:", row[4])
        print("================")

except Exception as e:
    print("Error:", e)
finally:
    if conn != None:
        cursor.close()
        conn.close()
        print("Connection closed.")

