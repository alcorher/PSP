import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Servidor UDP escuchando en {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)
        print(f"Mensaje recibido de {addr}: {data.decode('utf-8')}")
        s.sendto("Pong".encode("utf-8"), addr)
        print(f"Respuesta enviada a {addr}")
        