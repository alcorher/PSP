import socket
HOST = '127.0.0.1'
PORT = 2000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.connect((HOST, PORT))
   while True:
       mensaje = input("Escribe un numero para el servidor (escribe '0' para terminar): ")
       s.sendall(mensaje.encode("utf-8"))
       if mensaje.lower() == "0":
           print("Conexión terminada.")
           break
       data = s.recv(1024)
       print('Respuesta del servidor:', data.decode("utf-8"))