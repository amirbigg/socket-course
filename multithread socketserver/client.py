import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect(('127.0.0.1', 8001))
	sock.send(bytes('message from client', 'UTF-8'))
	print(str(sock.recv(1024), 'UTF-8'))
