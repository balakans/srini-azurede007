import pandas as pd
from pinecone import Pinecone

# ==========================================
# Configuration
# ==========================================

PINECONE_API_KEY = "xxxxx"

CSV_FILE = r"D:\Training\data\GenAI\isp_tickets.csv"

INDEX_HOST = "https://inceptezdb-nzq5bbi.svc.aped-4627-b74a.pinecone.io"

NAMESPACE = "isp-tickets"

# ==========================================
# Connect to Pinecone
# ==========================================

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index = pc.Index(
    host=INDEX_HOST
)

# ==========================================
# Read CSV
# ==========================================

df = pd.read_csv(CSV_FILE)

print(f"Loaded {len(df)} tickets")

# ==========================================
# Build records
# ==========================================

records = []

for _, row in df.iterrows():

    ticket_text = f"""
    Ticket ID: {row['TicketId']}
    Customer ID: {row['CustomerId']}
    Service Type: {row['ServiceType']}
    Category: {row['IssueCategory']}
    Description: {row['IssueDescription']}
    Priority: {row['Priority']}
    Region: {row['Region']}
    SLA Status: {row['SLAStatus']}
    Resolution: {row['ResolutionSummary']}
    """

    record = {
        "_id": str(row["TicketId"]),
        "text": ticket_text,  # REQUIRED
        "customer_id": str(row["CustomerId"]),
        "service_type": str(row["ServiceType"]),
        "category": str(row["IssueCategory"]),
        "priority": str(row["Priority"]),
        "region": str(row["Region"]),
        "sla_status": str(row["SLAStatus"]),
        "created_date": str(row["CreatedDate"])
    }

    records.append(record)
# ==========================================
# Upsert with Integrated Embedding
# ==========================================

BATCH_SIZE = 50

for i in range(0, len(records), BATCH_SIZE):

    batch = records[i:i+BATCH_SIZE]

    try:

        index.upsert_records(
            namespace=NAMESPACE,
            records=batch
        )

        print(
            f"Successfully inserted {len(batch)} records"
        )

    except Exception as e:
        print(f"Failed batch starting at {i}")
        print(str(e))

