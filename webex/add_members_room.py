import requests

token = ""
url = "https://webexapis.com/v1/memberships"

room_id = ""
person_email = ""

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

payload = {
    "roomId": f"{room_id}",
    "personEmail": f"{person_email}",
    "isModerator": False
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())