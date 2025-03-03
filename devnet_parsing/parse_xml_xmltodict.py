import xmltodict

def main():
    with open("devices.xml", "r") as file:
        data = xmltodict.parse(file.read())
        
    print(data)

if __name__ == "__main__":
    main()