from socket import *

host = ''
port = 12000
lastRecieved = 1

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))


serverSocket.listen(1)
print ('Listening for TCP connection')


showErrors = True

while 1:
    receiverSocket, addr = serverSocket.accept()
    # read client's message and remember client's address (IP and port)
    message, clientAddress = receiverSocket.recvfrom(2048)

    sequenceNumber = int(message.decode()[0:5])
    if (sequenceNumber != lastRecieved) and showErrors:
        print("ERROR: expected packet:%d, got packet:%d\n" % (lastRecieved, sequenceNumber))
    lastRecieved += 1

    # Print message and client address
    if showErrors == False:
        print (message.decode()[0:20] + "...\n")
        print (clientAddress)

    receiverSocket.close()