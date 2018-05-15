from socket import *
import time
from time import sleep

SERVER = '192.168.0.4'
PORT = 8080
frequence = 20  # medd/s
packageCounter = 1 # for sequence number
timer = 10.0 # how long will you send packets for
packageSize = 1000 # size in bytes

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((SERVER, PORT))

data = ""

for i in range(0, packageSize):
    data += "A"

frequence = 1.0/frequence
timeElapsed = 0.0
 
while (timeElapsed) < timer:
    msg = str(packageCounter).zfill(5) + ";" + data
    packageCounter += 1
    print(msg[0:10] + "...\n")
    clientSocket.send(msg.encode())
    
    sleep(frequence)
    timeElapsed += frequence

clientSocket.send("end".encode())

clientSocket.close()

