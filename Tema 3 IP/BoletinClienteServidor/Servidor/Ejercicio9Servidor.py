import socket
import random

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Servidor UDP escuchando en {HOST}:{PORT}")
    
    match (random.randint(1,3)):
        case 1:
            opcion = "Tijeras"
        case 2:
            opcion = "Papel"
        case 3:
            opcion = "Piedra"


    while True:
        data, addr = s.recvfrom(1024)
        print(f"Mensaje recibido de {addr}: {data.decode()}")
        if data.decode().lower() == opcion.lower():
            respuesta = "Empate"
        elif (data.decode().lower() == "tijeras" and opcion == "Papel") or \
             (data.decode().lower() == "papel" and opcion == "Piedra") or \
                (data.decode().lower() == "piedra" and opcion == "Tijeras"):
            respuesta = "Ganaste"
        else:
            respuesta = "Perdiste"

        s.sendto(respuesta.encode('utf-8'), addr)
        print(f"Respuesta enviada a {addr}: {respuesta}")
        break