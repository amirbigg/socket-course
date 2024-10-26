import socketserver


class SimpleTCPHandler(socketserver.BaseRequestHandler):
	def setup(self):
		print("Before processing data..!")
		return

	def handle(self):
		data = self.request.recv(1024)
		print(f"Received -> {data}".encode('utf-8'))
		self.request.send("Thanks".encode('utf-8'))
		return

	def finish(self):
		print("After processing data..!")
		return socketserver.BaseRequestHandler.finish(self)


class SimpleTCPServer(socketserver.TCPServer):
	def server_activate(self):
		print("Server activated..!")
		return socketserver.TCPServer.server_activate(self)

	def server_close(self):
		print("Server is shutting down..!")
		return socketserver.TCPServer.server_close(self)

	def verify_request(self, request, client_address):
		# print("Blocking some ip addresses..!")
		# return socketserver.TCPServer.verify_request(self, request, client_address)
		return False

	def finish_request(self, request, client_address):
		print("Sending data to request handler..!")
		return socketserver.TCPServer.finish_request(self, request, client_address)


server = SimpleTCPServer(('127.0.0.1', 8001), SimpleTCPHandler)
ip, port = server.server_address
print(ip, port)
server.serve_forever()
