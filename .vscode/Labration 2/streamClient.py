from socket import *
from time import sleep

host = '192.168.0.4'
port = 8080
frequence = 21  #meddelanden/s
packageCounter = 1
packageAmount = 200
packageSize = 1000 #size in bytes

clientSocket = socket(AF_INET, SOCK_DGRAM)


data = ""

for i in range(0, 100):
    data += "ABCDEFGHIJ"



while packageCounter < packageAmount:
    msg = str(packageCounter).zfill(5) + ";" + data
    packageCounter += 1
    print("Packet sent: " + msg[0:8] + "...\n")
    clientSocket.sendto(msg.encode(),(host, port))
    sleep(1/frequence)
 