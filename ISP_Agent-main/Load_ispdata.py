import os
import pandas as pd
from pinecone import Pinecone
from dotenv import load_dotenv
# -----------------------------
# Configuration
# -----------------------------
load_dotenv()

PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

HOST = "https://inceptez-isp-ticket-nzq5bbi.svc.aped-4627-b74a.pinecone.io"

NAMESPACE = "isptickets"

CSV_FILE = r"KB\isp_resolutions.csv"

EMBED_MODEL = "llama-text-embed-v2"

# ==========================================
# Connect Pinecone
# ==========================================

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(host=HOST)

# ==========================================
# Read CSV
# ==========================================

df = pd.read_csv(CSV_FILE)

print(f"Records Found : {len(df)}")

# ==========================================
# Process Records
# ==========================================

BATCH_SIZE = 20

for start in range(0, len(df), BATCH_SIZE):

    batch = df.iloc[start:start + BATCH_SIZE]

    texts = []

    for _, row in batch.iterrows():

        text = f"""
Issue Category: {row['issue_category']}

Issue Description:
{row['issue_description']}

Resolution:
{row['resolution']}
"""

        texts.append(text)

    # ======================================
    # Generate Embeddings
    # ======================================

    embeddings_response = pc.inference.embed(
        model=EMBED_MODEL,
        inputs=texts,
        parameters={
            "input_type": "passage",
            "truncate": "END"
        }
    )

    vectors = []

    for idx, (_, row) in enumerate(batch.iterrows()):

        vectors.append({
            "id": str(row["id"]),
            "values": embeddings_response[idx]["values"],
            "metadata": {
                "issue_category": str(row["issue_category"]),
                "issue_description": str(row["issue_description"]),
                "resolution": str(row["resolution"])
            }
        })

    index.upsert(
        vectors=vectors,
        namespace=NAMESPACE
    )

    print(f"Loaded {len(vectors)} records")

print("Completed Successfully")

# ==========================================
# Verify
# ==========================================

stats = index.describe_index_stats()

print(stats)