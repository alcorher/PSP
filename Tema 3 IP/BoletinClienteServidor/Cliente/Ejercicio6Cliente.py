import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s_addr = (HOST, PORT)
    comando = input("Ingrese 'fecha' para obtener la fecha o 'hora' para obtener la hora: ")
    s.sendto(comando.encode('utf-8'), s_addr)

    datos, addr = s.recvfrom(1024)
    print(f"Respuesta del servidor: {datos.decode('utf-8')}")