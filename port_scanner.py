import socket
import sys


def scan_ip(ip, start_port, end_port):
	print(f"[*] Starting TCP port scan on host {ip}")
	tcp_scan(ip, start_port, end_port)
	print(f"[*] TCP port scan on host {ip} completed")


def scan_domain(domain, start_port, end_port):
	print(f"[*] Starting TCP port scan on host {domain}")
	ip = socket.gethostbyname(domain)
	tcp_scan(ip, start_port, end_port)
	print(f"[*] TCP port scan on host {domain} completed")


def tcp_scan(ip, start_port, end_port):
	for port in range(start_port, end_port+1):
		try:
			tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			if not tcp.connect_ex((ip, port)):
				print(f"[+] {ip}:{port}/TCP Open")
				tcp.close()
		except Exception:
			pass


if __name__ == '__main__':
	socket.setdefaulttimeout(0.1)

	if len(sys.argv) < 4:
		print("Usage: ./port_scanner.py <ip> <start port> <end port>")
		print("Usage: ./port_scanner.py <domain> <start port> <end port> -n")

	elif len(sys.argv) >= 4:
		network = sys.argv[1]
		start_port = int(sys.argv[2])
		end_port = int(sys.argv[3])

	if len(sys.argv) == 4:
		scan_ip(network, start_port, end_port)

	if len(sys.argv) == 5:
		scan_domain(network, start_port, end_port)
