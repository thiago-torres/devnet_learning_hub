import json

def main():
    with open("devices.json", "r") as file:
        read = json.load(file)
    
    print(read)

if __name__ == "__main__":
    main()