import socket
HOST = '127.0.0.1'
PORT = 2000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        contrasena = input("Introduce una contraseña segura:")
        s.send(contrasena.encode('utf-8'))
        respuesta = s.recv(1024).decode('utf-8')
        print(f"Respuesta servidor: {respuesta}")
        if respuesta == "Contraseña segura":
            break

