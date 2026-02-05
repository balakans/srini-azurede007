import pandas as pd

#Creating Dataframe
#From a dictionary
data = {"studname":["Mani","Sschin","Vinod"], "stud-maths":[90,98,100],"stud-sci":[89,99,97]}

print(data)

df = pd.DataFrame(data)

print(df)

print("==================")
#From a list of dictionaries
data = [{'Name': 'Varun', 'Age': 25}, {'Name': 'Karthik', 'Age': 30}]
df = pd.DataFrame(data)
print(df)

#From a single Series
s = pd.Series([90, 95, 99], name='Marks')

print(s)

df = pd.DataFrame(s)
print("==================")
print(df)

#From multiple Series (same index)
name = pd.Series(['Alice', 'Bob', 'Charlie'])
age = pd.Series([25, 30, 35])

df = pd.DataFrame({'Name': name, 'Age': age})
print("==================")
print(df)

#From Series using concat()
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Column-wise (default: axis=1)
df = pd.concat([s1, s2], axis=1)
df.columns = ['A', 'B']
print(df)

#From a CSV file
df = pd.read_csv('D:\Training\pycharmworkouts\Data\TopRichestInWorld.csv')
#df = pd.read_csv('Data\TopRichestInWorld.csv', sep='$', header=None, names=['id', 'name', 'score'])
print(df)

#Top 5 records
print(df.head())

#Top n records
print(df.head(6))

#Ignore the last 10 records
print(df.head(-10))

#Last 5 records
print(df.tail())

#Last n records
print(df.tail(6))

#Read from excel file
#pip install openpyxl
df = pd.read_excel('D:\\Training\\pycharmworkouts\Data\\flights.xlsx', sheet_name='flights')
print(df.head())

#Read from json file
df = pd.read_json("D:\\Training\\pycharmworkouts\Data\\student.json")
print(df.head())

#Read from mysql
#From mysql
from dotenv import load_dotenv
import mysql.connector
import os
load_dotenv()

conn = mysql.connector.connect(
            host=os.getenv("MYSQL_SERVERNAME"),
            user=os.getenv("MYSQL_USERNAME"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DBNAME")
            )

df = pd.read_sql("SELECT * FROM tblcustomer", conn)
print(df)


