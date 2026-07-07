import requests

response = requests.get('https://inceptez-app1-d5eha2cpg3e5ajb7.centralindia-01.azurewebsites.net/api/addnum?num1=10&num2=20')

data = response.text

print(data)