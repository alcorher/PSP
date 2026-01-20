import socket 
import datetime

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s_addr = (HOST, PORT)
    s.bind(s_addr)

    datos, addr = s.recvfrom(1024)
    datos = datos.decode('utf-8')
    print(f"Recibido: {datos} ")
    if datos.lower() == "fecha":
        s.sendto(str(datetime.datetime.now().date()).encode("utf-8"), addr)
    if datos.lower() == "hora":
        s.sendto(str(datetime.datetime.now().time()).encode("utf-8"), addr)
    else:
        s.sendto("Comando no reconocido".encode("utf-8"), addr)