import requests

response = requests.get('https://inceptez-app1-d5eha2cpg3e5ajb7.centralindia-01.azurewebsites.net/api/getusers')

data = response.json()

for user in data:
    print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

