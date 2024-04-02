from socket import *

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)
    print('Server pronto.')
    vowels = ['a', 'e', 'i', 'o', 'u']

    while True:
        connectionSocket, clientAddress = serverSocket.accept()

        print('Client connesso: ', clientAddress)

        message = connectionSocket.recv(2048)
        message = message.decode('utf-8')

        result = len(message)
        for vowel in vowels:
            result -= message.lower().count(vowel)

        response = 'Il numero di consonanti è: ' + str(result)

        connectionSocket.send(response.encode('utf-8'))
        connectionSocket.close()