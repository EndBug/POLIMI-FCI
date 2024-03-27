from socket import *

if __name__ == '__main__':
    serverPort = 12000
    testTimeout = False  # Imposta a True per simulare un timeout

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print("Il server è pronto a ricevere.")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print('Datagramma da: ', clientAddress)

        message = message.decode().lower()
        vowels = ['a', 'e', 'i', 'o', 'u']

        result = len(message)
        for vowel in vowels:
            result -= message.count(vowel)

        reply = "Il messaggio contiene " + str(result) + " consonanti."

        if not testTimeout:
            serverSocket.sendto(reply.encode('utf-8'), clientAddress)
