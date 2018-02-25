#!/usr/bin/python3

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

cont = 6
def contador():
	global cont
	if cont == 0:			
		cont = 5			
	else:
		cont -=1
	return cont

try:
	while True:
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('HTTP request received:')
		received = recvSocket.recv(2048)
		print(str(received))
		url = str(received).split()[1]
		print(url)
		if url == '/cont':
			recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                     		  "<html><body><h1>Contador simple:<br><br>" 
							  + str(contador()) + 
							  "</h1></body></html>" +
							  "\r\n", 'utf-8'))
		else:
			recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                     		  "<html><body><h1>ERROR<br><br>" 
							  + "Url debe ser: http://localhost:1235/cont" + 
							  "</h1></body></html>" +
							  "\r\n", 'utf-8'))
		recvSocket.close()
except KeyboardInterrupt:
	print(" --Closing binded socket")

mySocket.close()
