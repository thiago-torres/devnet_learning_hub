
def main():
    with open ("devices.yaml", "r") as file:
        read = file.read()

    print(read)

if __name__ == "__main__":
    main()