from socket import *
import time


if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    for a in range(100):
        clientSocket.send('A'.encode('utf-8'))
        time.sleep(0.02)

    time.sleep(1)

    clientSocket.send('.'.encode('utf-8'))
    clientSocket.close()
