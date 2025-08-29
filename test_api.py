import requests

url = "http://127.0.0.1:5000/bfhl"

# Example input
payload = {
    "data": [1, "2", "a", "B", "@", 6, "z"]
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
