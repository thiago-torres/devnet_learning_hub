import os
from rest_aci_api import ACIapi

def main():
    print(os.getenv('ACI_ADDRESS'))
    print(os.getenv('ACI_USERNAME'))
    print(os.getenv('ACI_PASSWORD'))
    api = ACIapi(os.getenv('ACI_ADDRESS'))

    login = api.login(username=os.getenv('ACI_USERNAME'), password=os.getenv('ACI_PASSWORD')) 
    if login:
        # api.create_tenant('thiago_teste')        
        # api.create_app_profile(tenant='thiago_teste', app_profile="thiago_app")
        # api.create_app_profile(tenant='thiago_teste', app_profile="thiago_app2")
        # api.create_app_profile(tenant='thiago_teste', app_profile="thiago_app3")
        # api.get_app_profile(tenant='thiago_teste', app_profile="thiago_app")
        # api.list_app_profiles(tenant='thiago_teste')
        api.create_epg(tenant='thiago_teste', app_profile="thiago_app", epg_name="teste_de_EPG")

        tenant_request = api.request_tenant()
        if tenant_request:
            print(tenant_request['imdata'][-1])
        


if __name__ == "__main__":
        main()