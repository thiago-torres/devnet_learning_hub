import requests

token = ""
url = "https://webexapis.com/v1/rooms"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

payload = {"title":"Teste_Python"}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())