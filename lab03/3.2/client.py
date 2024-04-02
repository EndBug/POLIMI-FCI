from socket import *

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    while True:
        sentence = input('Inserisci lettere (. per fermare): ')
        clientSocket.send(sentence.encode())

        if sentence == '.':
            break;

        modifiedSentence = clientSocket.recv(1024)
        modifiedSentence = modifiedSentence.decode('utf-8')

        print('Dal server: ', modifiedSentence)

    clientSocket.close()
