import xml.etree.ElementTree as ET  # Importa a biblioteca para manipulação de XML

def main():
    # Abre o arquivo XML
    with open("devices.xml", "r") as file:
        # Parseia o conteúdo do arquivo XML
        tree = ET.parse(file)
        
    # Obtém o elemento raiz (tag <devices>)
    root = tree.getroot()

    # Itera sobre os elementos <device> e extrai os dados
    for device in root.findall("device"):  # Encontra todas as tags <device>
        nome = device.find("nome").text  # Encontra a tag <nome> dentro de <device>
        ip = device.find("ip").text  # Encontra a tag <ip> dentro de <device>
        modelo = device.find("modelo").text  # Encontra a tag <modelo> dentro de <device>
        status = device.find("status").text  # Encontra a tag <status> dentro de <device>
        
        # Imprime os dados extraídos
        print(f"Nome: {nome}, IP: {ip}, Modelo: {modelo}, Status: {status}")

if __name__ == "__main__":
    main()
