from socket import *

host = ''
port = 8080
lastRecieved = 1


# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))

# server starts listening for incoming TCP requests
serverSocket.listen(1)
print ('Listening for TCP connection')

connectionSocket, clientAddress = serverSocket.accept()

showErrors = False
while True:

    # read sentence of bytes from socket sent by the client
    message = connectionSocket.recv(1024).decode()

    sequenceNumber = int(message.decode()[0:5])
    if (sequenceNumber != lastRecieved) and showErrors:
        print("ERROR: expected packet:%d, got packet:%d\n" % (lastRecieved, sequenceNumber))
    lastRecieved += 1


    # Print message and client address
    if showErrors == False:
        print (message.decode()[0:20] + "...\n")
        print (clientAddress)
    # close the TCP connection; the welcoming socket continues

connectionSocket.close()

