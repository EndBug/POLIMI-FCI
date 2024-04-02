from socket import *

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    clientSocket.settimeout(2)

    message = input('Inserire parola: ')
    clientSocket.send(message.encode('utf-8'))

    try:
        modifiedMessage = clientSocket.recv(2048)
        modifiedMessage = modifiedMessage.decode('utf-8')
        print(modifiedMessage)
    except timeout:
        print('Server non raggiungibile, riprova più tardi.')
    finally:
        clientSocket.close()