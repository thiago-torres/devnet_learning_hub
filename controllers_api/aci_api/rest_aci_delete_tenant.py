from rest_aci_api_old import ACIapi

def main():
    api = ACIapi()

    response = api.delete_tenant("wingpy-xml")
    print(response)

if __name__ == "__main__":
    main()