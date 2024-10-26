import socketserver
import threading


class ThreadedTCPHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data = self.request.recv(1024)
		cur_thread = threading.current_thread()
		response = f"{cur_thread.name}, {data}".encode('utf-8')
		print("Sending response...")
		self.request.send(response)
		return


class ThreadedTCPServer(socketserver.ThreadingTCPServer):
	pass


server = ThreadedTCPServer(("127.0.0.1", 8001), ThreadedTCPHandler)
t = threading.Thread(target=server.serve_forever)
t.start()
