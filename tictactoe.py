import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "www.ingonline.nu"
PORT = 80

s.connect((HOST, PORT))

GetMessage = "GET /tictactoe/?board=xxxoooeee HTTP/1.1\r\nHost: www.ingonline.nu"

s.send(GetMessage.encode())
dataRecived = s.recv(2048)

s.close()

print(dataRecived.decode())

