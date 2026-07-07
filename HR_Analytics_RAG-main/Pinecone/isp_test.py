from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_4wWYPf_CCeut52SGVLv4z9jQ23rSde12Dczp3jQgFg2giR8Tsm32Tr3FLKbF7cLYdMdCSY")

index_info = pc.describe_index("inceptezdb")

print(index_info)