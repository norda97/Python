from socket import *

s = socket((AF_INET, SOCK_DGRAM))

host = gethostbyname(gethostname())
port = 8080

s.bind(host, port)

print ("Server socket bound to port: %d and host: %s" % (port, host))
