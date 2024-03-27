from socket import *

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(5)

    message = input('Inserisci una parola (senza caratteri speciali): ')
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

    try:
        response, serverAddress = clientSocket.recvfrom(2048)
        print(response.decode('utf-8'))
    except timeout:
        print('Errore: server irraggiungibile.')
    finally:
        clientSocket.close()
