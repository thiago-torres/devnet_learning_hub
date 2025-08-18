import requests

url = "https://webexapis.com/v1/messages"
token = ""
room_id = ""

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

mensagem = "Teste"

payload = {
    "roomId": f"{room_id}",
    "text": "teste mensagem",
    "markdown": "Essa API **funciona**\n\n>Teste!"
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())