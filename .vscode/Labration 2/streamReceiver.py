from socket import *

host = '192.168.0.4'
port = 8080

receiverSocket = socket(AF_INET, SOCK_DGRAM)
receiverSocket.bind((host, port))
lastRecieved = 1

print ("Server socket bound to port: %d and host: %s" % (port, host))

print ("The UDP server is ready to recieve")
showErrors = True

while 1:
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


