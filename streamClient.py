from socket import *
from time import sleep

host = ""
port = 8080
frequence = 1  #time in seconds
packageCounter = 0
packageAmount = 40
packageSize = 1000 #size in bytes
sequenceNumber = 10000

clientSocket = socket(AF_INET, SOCK_DGRAM)


data = ""
for i in range(0, 100):
    data += "ABCDEFGHIJ"



while packageCounter < packageAmount:
    msg = str(sequenceNumber + packageCounter) + ";" + data
    packageCounter += 1
    print("Packet sent: " + msg[0:8] + "...\n")
    clientSocket.sendto(msg.encode(),(host, port))
    sleep(frequence)
 