import yaml

def main():
    with open("devices.yaml", "r") as file:
        read = yaml.safe_load(file) 
    
    print(read)

if __name__ == "__main__":
    main()