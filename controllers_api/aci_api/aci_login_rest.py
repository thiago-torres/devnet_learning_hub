import os
import json
import requests

def main():
    url = f"https://{os.getenv('ACI_ADDRESS')}:443/api/aaaLogin.json"
    headers = {'Content-type': 'application/json'}
    body = {
        "aaaUser": {
            "attributes": {
                "name": os.getenv('ACI_USERNAME'),
                "pwd": os.getenv('ACI_PASSWORD')
            }
        }
    }
    print(url)
    print(headers)
    print(body)
    session = requests.Session()

    print("[COOKIE] Session cookies:", session.cookies.get_dict())
    print("[COOKIE] APIC-cookie:", session.cookies.get("APIC-cookie"))

    response = session.post(url=url, headers=headers, json=body, verify=False)
    
    print("[COOKIE] Session cookies:", session.cookies.get_dict())
    print("[COOKIE] APIC-cookie:", session.cookies.get("APIC-cookie"))

    print(json.dumps(response.json(), indent=4))  

if __name__ == "__main__":
    main()
