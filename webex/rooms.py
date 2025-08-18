import requests
import json

token = ""
url = "https://webexapis.com/v1/rooms"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(json.dumps(response.json(), indent=4))