import requests

class ACIapi:
    def __init__(self, aci_address):
        self.aci_address = aci_address
        self.session = requests.Session() # Dessa forma o cookie será utilizado nas próximas requisições

    def login(self, username, password):
        url = f"https://{self.aci_address}:443/api/aaaLogin.json"
        headers = {'Content-type': 'application/json'}
        body = {
            "aaaUser": {
                "attributes": {
                    "name": username,
                    "pwd": password
                }
            }
        }
        try:
            response = self.session.post(url=url, headers=headers, json=body, verify=False)

            if response.status_code == 200:
                print("Login realizado com sucesso!")
                return True
            else:
                print(f"Erro no login: {response.status_code} - {response.text}")
                return False

        except Exception as e:
            print(f"Erro de conexão ao tentar fazer login no ACI: {e}")
            return False

    def request_tenant(self):
        url = f"https://{self.aci_address}:443/api/node/class/fvTenant.json"
        try:
            response = self.session.get(url, verify=False)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro no request tenant: {response.status_code} - {response.text}")
                return False

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return False

    def create_tenant(self, tenant):
        url = f"https://{self.aci_address}/api/node/mo/uni.json"
        payload = {
            "fvTenant": {
                "attributes": {
                    "dn": f"uni/tn-{tenant}", 
                    "name": tenant, 
                    "rn": f"tn-{tenant}", 
                    "status": "created"
                },
                "children": []
            }
        }

        try:
            response = self.session.post(url, json=payload, verify=False)
            if response.status_code == 200:
                print(f"Tenant {tenant} criado com sucesso!")
                return response.json()
            else:
                print(f"Erro ao criar o tenant: {response.status_code} - {response.text}")
                return False

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return False

    def delete_tenant(self, tenant):
        url = f"https://{self.aci_address}/api/node/mo/uni/tn-{tenant}.json"
        payload = {
            "fvTenant": {
                "attributes": {
                    "status": "deleted"
                }
            }
        }

        try:
            response = self.session.post(url, json=payload, verify=False)
            if response.status_code == 200:
                print(f"Tenant {tenant} deletado com sucesso!")
                return response.json()
            else:
                print(f"Erro ao deletar o tenant: {response.status_code} - {response.text}")
                return False

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return False

    def create_app_profile(self, tenant, app_profile):

        url = f"https://{self.aci_address}:443/api/node/mo/uni/tn-{tenant}/ap-{app_profile}.json"

        payload = {
            "fvAp": {
                "attributes": {
                    "dn": f"uni/tn-{tenant}/ap-{app_profile}",
                    "name": app_profile,
                    "status": "created"
                }
            }
        }

        headers = {"Content-Type": "application/json"} # redundante = json=payload

        try:
            response = self.session.post(url, headers=headers, json=payload, verify=False)

            if response.status_code == 200:
                print(f"Application Profile {app_profile} criado com sucesso.")
                return True
            else:
                print(f"Erro ao criar App Profile: {response.status_code}")
                print(response.text)
                return False

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return False

    def get_app_profile(self, tenant, app_profile):
        url = f"https://{self.aci_address}/api/node/mo/uni/tn-{tenant}/ap-{app_profile}.json"

        try:
            response = self.session.get(url, verify=False)

            if response.status_code == 200:
                data = response.json()
                print(f"Dados do App Profile {app_profile}:")
                print(data)
                return data
            else:
                print(f"Erro ao buscar App Profile: {response.status_code}")
                print(response.text)
                return None

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return None

    def list_app_profiles(self, tenant):
        url = f"https://{self.aci_address}/api/node/mo/uni/tn-{tenant}.json"
        params = {
            "query-target": "children",
            "target-subtree-class": "fvAp"
        }

        try:
            response = self.session.get(url, params=params, verify=False)

            if response.status_code == 200:
                data = response.json()
                app_profiles = []

                for obj in data.get("imdata", []):
                    fvAp = obj.get("fvAp", {})
                    attributes = fvAp.get("attributes", {})
                    name = attributes.get("name")
                    if name:
                        app_profiles.append(name)

                print(f"Application Profiles encontrados no tenant {tenant}:")
                for ap in app_profiles:
                    print(f"- {ap}")

                return app_profiles

            else:
                print(f"Erro ao listar App Profiles: {response.status_code}")
                print(response.text)
                return []

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return []

    def create_epg(self, tenant, app_profile, epg_name):
        url = f"https://{self.aci_address}:443/api/node/mo/uni/tn-{tenant}/ap-{app_profile}/epg-{epg_name}.json"

        payload = {
            "fvAEPg": {
                "attributes": {
                    "dn": f"uni/tn-{tenant}/ap-{app_profile}/epg-{epg_name}",
                    "name": epg_name,
                    "status": "created"
                }
            }
        }

        try:

            response = self.session.post(url, json=payload, verify=False)

            if response.status_code == 200:
                print(f"EPG '{epg_name}' criado com sucesso.")
            else:
                print(f"Erro ao criar EPG {epg_name}: {response.status_code}")
                print(response.text)

        except Exception as e:
            print(f"Erro de exceção: {e}")
            return []

