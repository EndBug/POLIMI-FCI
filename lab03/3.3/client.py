from socket import *


if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    clientSocket.settimeout(10)

    message = input('Inserire numero: ')
    clientSocket.send(message.encode('utf-8'))

    try:
        isprime = clientSocket.recv(2048)
        isprime = isprime.decode('utf-8')

        if isprime == '1':
            print('Numero primo')
        elif isprime == '0':
            print('Numero non primo')
        else:
            print('Numero non valido')
    except timeout:
        print('Server non raggiungibile, riprova più tardi.')
    finally:
        clientSocket.close()
