import socket
direcciones = ['8.8.8.8', '127.0.0.1']

for d in direcciones:
    try:
        host = socket.gethostbyaddr(d)[0]
        print(f"Dirección {d} host {host}")
    except socket.error as e:
        print(f"Error: {e}")