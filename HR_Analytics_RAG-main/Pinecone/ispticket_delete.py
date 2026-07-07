from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_4wWYPf_CCeut52SGVLv4z9jQ23rSde12Dczp3jQgFg2giR8Tsm32Tr3FLKbF7cLYdMdCSY")

index = pc.Index(
    host="https://inceptezdb-nzq5bbi.svc.aped-4627-b74a.pinecone.io"
)

#Delete a Specific Record
index.delete(
    ids=["ISP0001"],
    namespace="isp-tickets"
)

print("Record deleted")

#Delete Multiple Records
index.delete(
    ids=[
        "ISP0001",
        "ISP0002",
        "ISP0003"
    ],
    namespace="isp-tickets"
)

print("Records deleted")

#Delete All Records in a Namespace
index.delete(
    delete_all=True,
    namespace="isp-tickets"
)

print("All records deleted from namespace")

#Delete Records by Metadata Filter:
# Delete all Critical tickets
index.delete(
    namespace="isp-tickets",
    filter={
        "priority": {"$eq": "Critical"}
    }
)

# Delete all Chennai tickets:
index.delete(
    namespace="isp-tickets",
    filter={
        "region": {"$eq": "Chennai"}
    }
)

#Verify Records Are Deleted
stats = index.describe_index_stats()

print(stats)
