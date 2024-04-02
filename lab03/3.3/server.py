from socket import *
import math


def is_prime(num):
    try:
        num = int(num)

        for i in range(2, math.floor(num / 2) + 1):
            if num % i == 0:
                return 0

        return 1
    except:
        return -1


if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))

    serverSocket.listen()
    print('Server pronto.')

    while True:
        connectionSocket, clientAddress = serverSocket.accept()

        print('Client connesso: ', clientAddress)

        message = connectionSocket.recv(2048)
        message = message.decode('utf-8')

        result = is_prime(message)

        connectionSocket.send(str(result).encode('utf-8'))
        connectionSocket.close()