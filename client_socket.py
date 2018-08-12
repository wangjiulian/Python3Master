import socket
import sys

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9998

clientSocket.connect((host,port))

msg = clientSocket.recv(1024)

clientSocket.close()

print(msg.decode('utf-8'))