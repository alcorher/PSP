import socket

print(f"IP de www.google.es: {socket.gethostbyaddr('www.google.es')[2]}")
print(f"IP de www.github.com: {socket.gethostbyaddr('www.github.com')[2]}")

