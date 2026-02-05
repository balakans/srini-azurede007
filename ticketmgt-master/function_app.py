import logging
import azure.functions as func
import mysql.connector
import json
import os
import re
from azure.eventhub import EventHubProducerClient, EventData
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Setup Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.2,
    google_api_key=os.environ["GEMINI_API_KEY"]
)

vhost = os.environ["MYSQL_HOST"]
vuser = os.environ["MYSQL_USER"]
vpassword = os.environ["MYSQL_PWD"]
vdatabase = os.environ["MYSQL_DB"]


@app.route(route="createTicket", methods=["POST"])
def create_ticket(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing create ticket request.")
    try:
        data = req.get_json()
        data["status"] = "New"

        required = ["channel", "title", "description", "category", "issue_date"]
        if not all(field in data for field in required):
            return func.HttpResponse("Missing required fields.", status_code=400)

        # Step 1: Insert into MySQL
        conn = mysql.connector.connect(
            host=vhost,
            user=vuser,
            password=vpassword,
            database=vdatabase
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tickets (channel, title, description, category, issue_date, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data["channel"],
            data["title"],
            data["description"],
            data["category"],
            data["issue_date"],
            data["status"]
        ))

        # ✅ Get the newly inserted ticket ID
        ticketid = cursor.lastrowid
        data["ticketid"] = ticketid  # Add to the payload

        conn.commit()
        cursor.close()
        conn.close()

        # Step 2: Send to Event Hub
        connection_str = os.environ.get("EVENT_HUB_CONNECTION_STRING")
        eventhub_name = os.environ.get("EVENT_HUB_NAME")

        producer = EventHubProducerClient.from_connection_string(
            conn_str=connection_str,
            eventhub_name=eventhub_name
        )
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(json.dumps(data)))
        producer.send_batch(event_data_batch)
        producer.close()

        return func.HttpResponse(
            json.dumps({
                "message": "Ticket created successfully.",
                "ticketid": ticketid
            }),
            status_code=201,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Server error.", status_code=500)


# ✅ 2. List Tickets
@app.route(route="listTickets", methods=["GET"])
def list_tickets(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing list tickets request.")
    sqlquery = """
        SELECT
        t.id,
        t.title,
        t.description,
        CASE
            WHEN i.sentiment_score <= -0.5 THEN 'Bad'
            WHEN i.sentiment_score BETWEEN -0.5 AND 0.2 THEN 'Neutral'
            WHEN i.sentiment_score > 0.2 THEN 'Good'
            ELSE 'Unknown'
        END AS sentiment_label,
        i.priority,
        t.channel,
        t.status,
        t.issue_date
        FROM tickets t
        LEFT OUTER JOIN ticketqueue i
        ON t.id = i.ticketid order by created_ts desc
    """
    try:
        conn = mysql.connector.connect(
            host=vhost,
            user=vuser,
            password=vpassword,
            database=vdatabase
        )
        cursor = conn.cursor()
        cursor.execute(sqlquery)

        columns = [col[0] for col in cursor.description]
        rows = []
        for row in cursor.fetchall():
            record = dict(zip(columns, row))
            # Convert date or datetime to ISO string
            for key, value in record.items():
                if hasattr(value, 'isoformat'):
                    record[key] = value.isoformat()
            rows.append(record)

        cursor.close()
        conn.close()

        return func.HttpResponse(
            json.dumps(rows),
            status_code=200,
            mimetype="application/json"
        )
    except mysql.connector.Error as err:
        logging.error(f"MySQL Error: {err}")
        return func.HttpResponse("Database error", status_code=500)
    except Exception as e:
        logging.error(f"Unhandled Exception: {e}")
        return func.HttpResponse("Server error", status_code=500)


# ✅ 3. Delete Ticket by ID
@app.route(route="deleteTicket", methods=["DELETE"])
def delete_ticket(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing delete ticket request.")
    try:
        ticket_id = req.params.get("id")
        if not ticket_id:
            return func.HttpResponse("Missing 'id' query parameter.", status_code=400)

        conn = mysql.connector.connect(
            host=vhost,
            user=vuser,
            password=vpassword,
            database=vdatabase
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
        conn.commit()
        cursor.close()
        conn.close()

        return func.HttpResponse("Ticket deleted.", status_code=200)
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error deleting ticket.", status_code=500)

# ✅ 4. Get the tickets count by status
@app.route(route="getTicketCounts", methods=["GET"])
def get_ticket_counts(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing ticket count request.")

    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="103.86.177.4",
            user="kbnhzraf_retail",
            password="Inspire123$",
            database="kbnhzraf_ticketdb"
        )
        cursor = conn.cursor()

        # Get total count
        cursor.execute("SELECT COUNT(*) FROM tickets")
        total = cursor.fetchone()[0]

        # Get count by status
        cursor.execute("""
            SELECT status, COUNT(*) 
            FROM tickets 
            GROUP BY status
        """)
        status_counts = dict(cursor.fetchall())

        # Ensure all keys are present
        result = {
            "total": total,
            "new": status_counts.get("New", 0),
            "inprogress": status_counts.get("InProgress", 0),
            "resolved": status_counts.get("Resolved", 0)
        }

        cursor.close()
        conn.close()

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Server error", status_code=500)

@app.function_name(name="formatTicket")
@app.route(route="formatTicket", methods=["POST"])
def format_ticket(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing speech text rephrasing.')

    try:
        body = req.get_json()
        input_text = body.get('text', '').strip()

        if not input_text:
            return func.HttpResponse(
                json.dumps({ "error": "Text is required" }),
                mimetype="application/json",
                status_code=400
            )

        # Gemini setup
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

        # 🔍 Prompt Gemini to extract and return subject + description in JSON format
        prompt = f"""
        The following is a user's raw speech input. Please:
        1. Identify the subject of the issue (as a short title).
        2. Rephrase and summarize the rest as a clear description.
        3. Return both fields in JSON format with keys "subject" and "description" only.

        Input:
        \"\"\"{input_text}\"\"\"
        """

        response = model.generate_content(prompt)
        result_text = response.text.strip()
        clean_text = re.sub(r"^```json\s*|\s*```$", "", result_text.strip(), flags=re.IGNORECASE)

        # 🧠 Try to parse the LLM response as JSON
        try:
            result_json = json.loads(clean_text)
        except json.JSONDecodeError:
            # If Gemini returns unstructured text, fallback
            return func.HttpResponse(
                json.dumps({
                    "error": "LLM response not in JSON format",
                    "raw": result_text
                }),
                mimetype="application/json",
                status_code=500
            )

        return func.HttpResponse(
            json.dumps(result_json),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            json.dumps({ "error": "Internal server error", "details": str(e) }),
            mimetype="application/json",
            status_code=500
        )


@app.route(route="createVoiceTicket", methods=["POST"])
def create_voice_ticket(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing create ticket request.")
    try:
        data = req.get_json()
        data["category"] = ""
        required = ["channel", "title", "description", "category", "issue_date"]
        if not all(field in data for field in required):
            return func.HttpResponse("Missing required fields.", status_code=400)

        # Step 1: Insert into MySQL
        conn = mysql.connector.connect(
            host=vhost,
            user=vuser,
            password=vpassword,
            database=vdatabase
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tickets (channel, title, description, category, issue_date, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data["channel"],
            data["title"],
            data["description"],
            data["category"],
            data["issue_date"],
            data["status"]
        ))

        # ✅ Get the newly inserted ticket ID
        ticketid = cursor.lastrowid
        data["ticketid"] = ticketid  # Add to the payload

        conn.commit()
        cursor.close()
        conn.close()

        # Step 2: Send to Event Hub
        connection_str = os.environ.get("EVENT_HUB_CONNECTION_STRING")
        eventhub_name = os.environ.get("EVENT_HUB_NAME")
        logging.info(f"EVENT_HUB_CONNECTION_STRING: {os.environ.get('EVENT_HUB_CONNECTION_STRING')}")
        logging.info(f"EVENT_HUB_NAME: {os.environ.get('EVENT_HUB_NAME')}")
        producer = EventHubProducerClient.from_connection_string(
            conn_str=connection_str,
            eventhub_name=eventhub_name
        )
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(json.dumps(data)))
        producer.send_batch(event_data_batch)
        producer.close()

        return func.HttpResponse(
            json.dumps({
                "message": "Ticket created successfully.",
                "ticketid": ticketid
            }),
            status_code=201,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Server error.", status_code=500)