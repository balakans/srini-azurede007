from pinecone import Pinecone
import pandas as pd
pc = Pinecone(api_key="pcsk_4wWYPf_CCeut52SGVLv4z9jQ23rSde12Dczp3jQgFg2giR8Tsm32Tr3FLKbF7cLYdMdCSY")

index = pc.Index(
    host="https://inceptezdb-nzq5bbi.svc.aped-4627-b74a.pinecone.io"
)

while True:

    query = input("\nAsk about tickets: ")

    if query.lower() == "exit":
        break

    results = index.search(
        namespace="isp-tickets",
        query={
            "top_k": 5,
            "inputs": {
                "text": query
            }
        }
    )

    print("\nMatching Tickets:\n")
    rows = []

    for hit in results.result.hits:
        rows.append({
            "TicketId": hit.id,
            "Score": hit.score,
            "CustomerId": hit.fields.get("customer_id"),
            "Category": hit.fields.get("category"),
            "Priority": hit.fields.get("priority"),
            "Region": hit.fields.get("region"),
            "SLAStatus": hit.fields.get("sla_status")
        })

    df = pd.DataFrame(rows)

    print(df)