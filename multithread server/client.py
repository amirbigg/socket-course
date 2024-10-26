import socket


server_ip = "127.0.0.1"
server_port = 8000


def run_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((server_ip, server_port))

	try:
		while True:
			msg = input("Enter message: ")
			client.send(msg.encode("utf-8")[:1024])

			response = client.recv(1024)
			response = response.decode("utf-8")

			if response.lower() == "closed":
				break

			print(f"Received : {response}")

	except Exception as e:
		print(f"ERROR {e}")
	finally:
		client.close()
		print("Connection to server closed!")


run_client()
