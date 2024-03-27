from socket import *

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(2)

    message = input('Inserisci lettere: ')
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessage = modifiedMessage.decode('utf-8')
        print(modifiedMessage)
    except timeout:
        print('Timeout scaduto: server non raggiungibile')
    finally:
        clientSocket.close()
