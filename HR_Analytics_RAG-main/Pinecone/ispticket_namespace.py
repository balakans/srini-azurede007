from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_4wWYPf_CCeut52SGVLv4z9jQ23rSde12Dczp3jQgFg2giR8Tsm32Tr3FLKbF7cLYdMdCSY")

index = pc.Index(
    host="https://inceptezdb-nzq5bbi.svc.aped-4627-b74a.pinecone.io"
)

index.delete(
    namespace="isp-tickets",
    delete_all=True
)

print("Namespace cleared")

pc.delete_index("inceptezdb")

print("Index deleted")