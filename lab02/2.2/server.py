from socket import *

if __name__ == '__main__':
    serverPort = 12000
    testTimeout = False  # Imposta a True per simulare un timeout

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print("Il server è pronto a ricevere.")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print("Datagramma da: ", clientAddress)
        message = message.decode('utf-8')
        modifiedMessage = message.upper()

        if not testTimeout:
            serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
