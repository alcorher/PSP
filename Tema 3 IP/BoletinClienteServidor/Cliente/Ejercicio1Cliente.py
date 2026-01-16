import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    nombre = input("Introduce tu nombre: ")
    s.sendall(nombre.encode("utf-8"))
    data = s.recv(1024)

print('Respuesta del servidor:', data.decode("utf-8"))