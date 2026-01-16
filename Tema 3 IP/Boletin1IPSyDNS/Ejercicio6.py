import socket

try:
	print(socket.gethostbyaddr('8.8.8.8')[0])
except socket.error as e:
	print(f"Error: {e}")