from socket import *

host = ''
port = 8080

receiverSocket = socket(AF_INET, SOCK_DGRAM)
receiverSocket.bind((host, port))

print ("Server socket bound to port: %d and host: %s" % (port, host))

print ("The UDP server is ready to recieve")

while True:
    # read client's message and remember client's address (IP and port)
    message, clientAddress = receiverSocket.recvfrom(2048)

    # Print message and client address
    print (message.decode()[0:20] + "...\n")
    print (clientAddress)


