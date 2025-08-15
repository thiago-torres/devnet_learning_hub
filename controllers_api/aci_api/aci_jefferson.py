import os # Usado para carregar as variaveis de ambiente
import requests
import json

session = requests.Session() #### Dessa forma o cookie será utilizado nas próximas requisições

def login():
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
                                                    
    response = session.post(url=url, headers=headers, json=body, verify=False)

    if response.status_code == 200:
        print("Login realizado com sucesso!")
    else:
        print(f'Error code: {response.status_code}\nError info: {response.text}')

def request_tenant():

    url = f"https://{os.getenv('ACI_ADDRESS')}:443/api/node/class/fvTenant.json"
    response = session.get(url, verify=False)
    
    for response in response.json()['imdata']:
        print(json.dumps(response, indent=4))

def create_app_profile():
    tenant = "test_thiago"
    app_profile = "test_thiago"

    url = f"https://{os.getenv('ACI_ADDRESS')}:443/api/node/mo/uni/tn-{tenant}/ap-{app_profile}.json"

    payload = {
        "fvAp": {
            "attributes": {
                "dn": f"uni/tn-{tenant}/ap-{app_profile}",
                "name": app_profile,
                "status": "created"
            }
        }
    }

    headers = {"Content-Type": "application/json"}
    response = session.post(url, headers=headers, json=payload, verify=False)

    if response.status_code == 200:
        print(f"Application Profile '{app_profile}' criado com sucesso.")
    else:
        print(f"Erro ao criar App Profile: {response.status_code}")
        print(response.text)

def create_epg():
    tenant = "test_thiago"
    app_profile = "test_thiago"
    epg_name = "VLAN010-epg"

    url = f"https://{os.getenv('ACI_ADDRESS')}:443/api/node/mo/uni/tn-{tenant}/ap-{app_profile}/epg-{epg_name}.json"

    payload = {
        "fvAEPg": {
            "attributes": {
                "dn": f"uni/tn-{tenant}/ap-{app_profile}/epg-{epg_name}",
                "name": epg_name,
                "status": "created"
            }
        }
    }

    headers = {"Content-Type": "application/json"}
    response = session.post(url, headers=headers, json=payload, verify=False)

    if response.status_code == 200:
        print(f"EPG '{epg_name}' criado com sucesso.")
    else:
        print(f"Erro ao criar EPG '{epg_name}': {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    login()
    # print(session.cookies.get("APIC-cookie"))
    request_tenant()
    # create_app_profile()
    # create_epg()



