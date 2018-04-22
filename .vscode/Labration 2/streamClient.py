from socket import *
from time import sleep

host = ''
port = 8080
frequence = 0.001  #time in seconds
packageCounter = 1
packageAmount = 100
packageSize = 1000 #size in bytes

clientSocket = socket(AF_INET, SOCK_DGRAM)


data = ""
for i in range(0, packageSize / 10):
    data += "ABCDEFGHIJ"



while packageCounter < packageAmount:
    msg = str(packageCounter).zfill(5) + ";" + data
    packageCounter += 1
    print("Packet sent: " + msg[0:8] + "...\n")
    clientSocket.sendto(msg.encode(),(host, port))
    sleep(frequence)
 