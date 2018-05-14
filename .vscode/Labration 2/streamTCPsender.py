from socket import *
import time
from time import sleep

host = '193.11.187.146'
port = 8080
frequence = 2  # medd/s
packageCounter = 1 # for sequence number
timer = 1 # how long will you send packets for
packageSize = 1000 # size in bytes


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((host, port))

data = ""

for i in range(0, packageSize):
    data += "A"

frequence = 1/frequence
t0 = time.time() 
t1 = 0
print("t1: %f  -  t0: %f    <   timer:%f" % (t1, t0, timer))
while (t1 - t0) < timer:
    msg = str(packageCounter).zfill(5) + ";" + data
    packageCounter += 1
    print("Packet sent: " + msg[0:8] + "...\n")
    clientSocket.send(msg.encode())
    
    sleep(frequence)
    t1 = time.time()

clientSocket.close()

