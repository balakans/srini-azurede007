import requests

response = requests.get("http://127.0.0.1:8000/hello", headers={"Content-Type": "application/json"})

#response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m", headers={"Content-Type": "application/json"})

print("Status Code:", response.status_code)
print("Response:", response.json())


data = {
    "id": 1,
    "uname": "testuser",
    "pwd": "secret123"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post("http://127.0.0.1:8000/saveuser", json=data, headers=headers)

print("===============")
print(response.json())