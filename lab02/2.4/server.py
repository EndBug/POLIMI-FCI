from socket import *
import math


def is_prime(s):
    try:
        n = int(s)

        for i in range(2, math.floor(n / 2) + 1):
            if n % i == 0:
                return False

        return True
    except:
        return False


if __name__ == '__main__':
    serverPort = 12000
    testTimeout = False  # Imposta a True per simulare un timeout

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print("Il server è pronto a ricevere")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print("Datagramma da: ", clientAddress)

        isPrime = is_prime(message.decode('utf-8'))

        serverSocket.sendto(str(isPrime).encode('utf-8'), clientAddress)
