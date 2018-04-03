import socket
import threading
import time
import sys

print("Hosting server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8080

s.bind((host, port))
print("Server hosted at adress " + str(host) + " and port " + str(port))
s.listen(1)

connections = []

def handler(connection, adress):
    while True:
        data = connection.recvfrom(1024)
        
        for c in connections:
            c.send(bytes(data[0]))
        if not data:
            connections.remove(connection)
            connection.close()
            print(str(adress) + " disconnected")
            break

while True:
    connection, adress = s.accept()
    
    connectionThread = threading.Thread(target = handler, args = (connection, adress))
    connectionThread.daemon = True
    connectionThread.start()

    connections.append(connection)
    print(connections)