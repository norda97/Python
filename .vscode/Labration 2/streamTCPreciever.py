from socket import *

host = ''
port = 12000

# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))

# server starts listening for incoming TCP requests
serverSocket.listen(1)
print ('Listening for TCP connection')



while True:
    # server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept()

    # read sentence of bytes from socket sent by the client
    sentence = connectionSocket.recv(1024).decode()

    # print unmodified sentance and client address
    print (sentence)

    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()
