from socket import *

if __name__ == '__main__':
    serverPort = 12000

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print("Il server è pronto a ricevere")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print("Datagramma da: ", clientAddress)
        message = message.decode('utf-8')
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
