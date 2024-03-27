from socket import *

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(2)

    number = input('Inserisci un numero: ')
    clientSocket.sendto(number.encode('utf-8'), (serverName, serverPort))

    try:
        response, serverAddress = clientSocket.recvfrom(2048)
        print("Numero primo? ", response.decode('utf-8'))
    except timeout:
        print("Errore: server non raggiungibile.")
    finally:
        clientSocket.close()
