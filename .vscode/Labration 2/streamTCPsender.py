from socket import *
import time

SERVER = '192.168.2.4'
PORT = 12000
frequence = 50  # medd/s
packageCounter = 1 # for sequence number
timer = 10 # how long will you send packets for
packageSize = 1000 # size in bytes

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((SERVER, PORT))

data = ""

for i in range(0, packageSize):
    data += "A"

frequence = 1/frequence
t0 = time.time() 
t1 = 0
 
while (t1 - t0) < timer:
    msg = str(packageCounter).zfill(5) + ";" + data
    packageCounter += 1
    print("Packet sent: " + msg[0:8] + "...\n")
    clientSocket.send(msg.encode())
    
    time.sleep(frequence)
    t1 = time.time()
  


clientSocket.close()
