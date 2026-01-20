import socket
import time

HOST = '127.0.0.1'
PORT = 2000
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    mensaje = "Ping"
    s.sendto(mensaje.encode("utf-8"), (HOST, PORT))
    envioMensaje = time.time()
    print(f"Mensaje enviado al servidor {HOST}:{PORT}")

    data, addr = s.recvfrom(1024)
    recepcionMensaje = time.time()
    rtt = (recepcionMensaje - envioMensaje) * 1000  # Convertir a milisegundos
    print(f"RTT: {rtt:.2f} ms")
    print(f"Respuesta recibida del servidor: {data.decode('utf-8')}")