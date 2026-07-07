import azure.functions as func
import logging
import mysql.connector
import json
import os
import pandas as pd
import io
import os
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient
import requests
from datetime import datetime


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

vhost = os.getenv("mysql_host")
vuser = os.getenv("mysql_user")
vpassword = os.getenv("mysql_password")
vdatabase = os.getenv("mysql_database")


@app.route(route="testfunc")
def testfunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="addnum")
def addnum(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    num1 = req.params.get('num1')
    num2 = req.params.get('num2')
    if num1 and num2:
        result = float(num1) + float(num2)
        return func.HttpResponse(f"The sum of {num1} and {num2} is {result}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass two numbers in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="createuser")
def createuser(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    uname = req.params.get('name')
    uemail = req.params.get('email')
    if uname and uemail:
        try:
            conn = mysql.connector.connect(
                host=vhost,
                user=vuser,
                password=vpassword,
                database=vdatabase
            )
            cursor = conn.cursor()
            insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(insert_query, (uname, uemail))
            conn.commit()
            cursor.close()
            conn.close()
            return func.HttpResponse(f"User {uname} with email {uemail} created successfully.")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
            return func.HttpResponse("Failed to create user due to a database error.", status_code=500)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass two numbers in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="getusers")
def getusers(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to fetch all users.')

    try:
        # Establish connection
        conn = mysql.connector.connect(
            host=vhost,
            user=vuser,
            password=vpassword,
            database=vdatabase
        )
        
        # Use dictionary=True to make mapping to JSON easier
        cursor = conn.cursor(dictionary=True)
        
        # Execute query
        select_query = "SELECT id, name, email FROM users"
        cursor.execute(select_query)
        
        # Fetch all records
        users = cursor.fetchall()
        
        cursor.close()
        conn.close()

        # Return the data as JSON
        return func.HttpResponse(
            body=json.dumps(users),
            mimetype="application/json",
            status_code=200
        )

    except mysql.connector.Error as err:
        logging.error(f"Database Error: {err}")
        return func.HttpResponse(
            "Error connecting to the database or fetching records.", 
            status_code=500
        )
    except Exception as e:
        logging.error(f"General Error: {e}")
        return func.HttpResponse("An unexpected error occurred.", status_code=500)
    

@app.blob_output(arg_name="archive_blob", path="users/archive/{name}",
                               connection="inceptezadls_STORAGE")

@app.blob_trigger(arg_name="myblob", path="users/input/{name}",
                               connection="inceptezadls_STORAGE") 
def bulkload(myblob: func.InputStream, archive_blob: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    
    try:
        # 1. Read CSV from Stream
        df = pd.read_csv(io.BytesIO(myblob.read()))
        data_to_insert = list(df.itertuples(index=False, name=None)) # Convert to list of tuples

        # 2. Bulk Insert to MySQL
        conn = mysql.connector.connect(host=vhost, user=vuser, password=vpassword, database=vdatabase)
        cursor = conn.cursor()
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.executemany(insert_query, data_to_insert) # Use executemany for performance
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Successfully inserted {len(data_to_insert)} records.")
        output_text = df.to_csv(index = False)
        archive_blob.set(output_text.encode('utf-8'))

        # 4. DELETE the source file from users/inputs/
        # Get the connection string from environment variables
        import os   
        conn_str = os.getenv("inceptezadls_STORAGE")
        
        # Initialize BlobClient for the specific source blob
        # myblob.name contains the path "users/inputs/filename.csv"
        blob_client = BlobClient.from_connection_string(conn_str, 
                                                        container_name=myblob.name.split('/')[0], 
                                                        blob_name='/'.join(myblob.name.split('/')[1:]))
        
        blob_client.delete_blob()
        logging.info(f"Deleted source blob: {myblob.name}")

    except Exception as e:
        logging.error(f"Error in bulkload: {e}")


#Get API key from environment variable and construct the Weather API URL
API_KEY = os.getenv("apikey")
WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?lat=13.06&lon=80.23&appid={API_KEY}&units=metric"

@app.timer_trigger(schedule="0/30 * * * * *", arg_name="readweather", run_on_startup=True, use_monitor=False)
def weather_timer_func(readweather: func.TimerRequest) -> None:
    if readweather.past_due:
        logging.info('The timer is past due!')

    logging.info(f"Weather sync started at: {datetime.now()}")

    try:
        # 1. Fetch data from Weather API
        response = requests.get(WEATHER_URL)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()

        # Extract relevant fields
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        city_name = data['name']

        # 2. Write into MySQL
        conn = mysql.connector.connect(
            host=vhost,
            user=vuser,
            password=vpassword,
            database=vdatabase
        )
        cursor = conn.cursor()
        
        insert_query = """
            INSERT INTO weather_logs (city, temperature, humidity, description, recorded_at) 
            VALUES (%s, %s, %s, %s, %s)
        """
        record_time = datetime.now()
        cursor.execute(insert_query, (city_name, temp, humidity, desc, record_time))
        
        conn.commit()
        cursor.close()
        conn.close()

        logging.info(f"Successfully logged weather for {city_name}: {temp}°C, {desc}")

    except requests.exceptions.RequestException as e:
        logging.error(f"API Request Error: {e}")
    except mysql.connector.Error as err:
        logging.error(f"Database Error: {err}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")