import socket
HOST = '127.0.0.1'
PORT = 2000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensaje = input("Escribe una frase: ")
    s.send(mensaje.encode('utf-8'))
    respuesta = s.recv(1024).decode('utf-8')
    print(f"Respuesta servidor: {respuesta}")