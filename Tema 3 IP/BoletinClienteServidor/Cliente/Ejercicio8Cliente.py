import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print(f"Servidor UDP escuchando en {HOST}:{PORT}")

    while True:
        
        n = int(input("Adivina el número campeón: "))
        s.sendto(str(n).encode('utf-8'), (HOST,PORT))
        data, addr = s.recvfrom(1024)
        print(f"Mensaje recibido de: {data.decode('utf-8')}")