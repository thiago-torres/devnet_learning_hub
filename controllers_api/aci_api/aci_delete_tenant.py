import os
import requests
import json

def main():
    tenant_name = 'TRIPPLEH'
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
    
    session = requests.Session()                                                #### Dessa forma o cookie será utilizado
    response = session.post(url=url, headers=headers, json=body, verify=False)  #### nas próximas requisições conforme abaixo

    
    tenant_url = f"https://{os.getenv('ACI_ADDRESS')}/api/node/mo/uni/tn-{tenant_name}.json"
    tenant_data = {
        "fvTenant": {
            "attributes": {
                "status": "deleted"
            }
        }
    }

    response = session.post(tenant_url, json=tenant_data, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error deleting tenant: {response.status_code} - {response.text}")
if __name__ == "__main__":
    main()

