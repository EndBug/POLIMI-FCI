from socket import *

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)

    while True:
        print('Server pronto.')
        connectionSocket, clientAddress = serverSocket.accept()

        print('Client connesso: ', clientAddress)

        while True:
            sentence = connectionSocket.recv(1024)
            sentence = sentence.decode('utf-8')

            if sentence == '.':
                break

            upper = sentence.upper()
            connectionSocket.send(upper.encode('utf-8'))

        connectionSocket.close()
