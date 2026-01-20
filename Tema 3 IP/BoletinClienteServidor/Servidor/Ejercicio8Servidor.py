import socket
import random

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Servidor UDP escuchando en {HOST}:{PORT}")
    
    numeroRandom = random.randint(0,1000) 
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Mensaje recibido")
        if (int(data.decode('utf-8')) == numeroRandom):
            s.sendto("Has acertado".encode('utf-8'),addr)
            break
        if (int(data) < numeroRandom):
            s.sendto("El numero es mayor".encode('utf-8'),addr)
        if (int(data) > numeroRandom):
            s.sendto("El numero es menor".encode('utf-8'),addr)