import os
import requests

class ACIapi:
    def __init__(self):
        self.aci_address = os.getenv('ACI_ADDRESS')
        self.session = self.request_cookie()

    def request_cookie(self):
        url = f"https://{self.aci_address}:443/api/aaaLogin.json"
        headers = {'Content-type': 'application/json'}
        body = {
            "aaaUser": {
                "attributes": {
                    "name": os.getenv('ACI_USERNAME'),
                    "pwd": os.getenv('ACI_PASSWORD')
                }
            }
        }
        session = requests.Session()
        response = session.post(url=url, headers=headers, json=body, verify=False)#, timeout=5)
        if response.status_code == 200:
            return session
        else:
            raise Exception(f"Error requesting cookie: {response.status_code} - {response.text}")

    def request_tenant(self):
        tenant_url = f"https://{self.aci_address}:443/api/node/class/fvTenant.json"
        tenant_response = self.session.get(tenant_url, verify=False)
        return tenant_response

    def create_tenant(self, tenant_name):
        tenant_url = f"https://{self.aci_address}/api/node/mo/uni.json"
        tenant_data = {
            "fvTenant": {
                "attributes": {
                    "dn": f"uni/tn-{tenant_name}", 
                    "name": tenant_name, 
                    "rn": f"tn-{tenant_name}", 
                    "status": "created"
                },
                "children": []
            }
        }

        response = self.session.post(tenant_url, json=tenant_data, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error creating tenant: {response.status_code} - {response.text}")

    def delete_tenant(self, tenant_name):
        tenant_url = f"https://{self.aci_address}/api/node/mo/uni/tn-{tenant_name}.json"
        tenant_data = {
            "fvTenant": {
                "attributes": {
                    "status": "deleted"
                }
            }
        }

        response = self.session.post(tenant_url, json=tenant_data, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error deleting tenant: {response.status_code} - {response.text}")
