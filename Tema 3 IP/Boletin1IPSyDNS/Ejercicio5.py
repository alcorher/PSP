import socket

dominios = ['www.amazon.es', 'www.este-dominio-no-existe.com']

for dominio in dominios:
    try:
        ip = socket.gethostbyname(dominio)
        print(f"IP de {dominio}: {ip}")
    except socket.error as e:
        print(f"Error de socket para '{dominio}': {e}")
