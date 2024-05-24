import socket
import sys

args = sys.argv[1:]

server_ip = args[0]
server_port = int(args[1])
num_connections = 10000

socks = []

for i in range(num_connections):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((server_ip, server_port))
    print(f"Connection to {server_ip} port {server_port} succeeded! ({i+1})")
    socks.append(sock)
    # Optionally, you can perform further operations like sending/receiving data
