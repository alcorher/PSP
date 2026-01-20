import socket

HOST = '127.0.0.1'
PORT = 2001

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    opcion = input("Elige Piedra, Papel o Tijeras: ")
    s.sendto(opcion.encode(), (HOST, PORT))
    data, addr = s.recvfrom(1024)
    print(f"Respuesta del servidor: {data.decode()}")