from socket import *
import time
from time import sleep

host = '192.168.0.3'
port = 8080
frequence = 50  # medd/s
packageCounter = 1 # for sequence number
timer = 10 # how long will you send packets for
packageSize = 1000 # size in bytes

clientSocket = socket(AF_INET, SOCK_DGRAM)


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
    clientSocket.sendto(msg.encode(),(host, port))
    
    sleep(frequence)
    t1 = time.time()
  