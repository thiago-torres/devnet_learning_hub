import json
from rest_aci_api_old import ACIapi

def main():
    api = ACIapi()
    print('api instance OK')
    try:
        response = api.request_tenant()
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        tenants = response.json()
        print(tenants)
    except Exception as e:
        print(e)

    # for tenant in tenants:
    #     print(json.dumps(tenant, indent=4))

if __name__ == "__main__":
    main()
