import socket
HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conexión existosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
        while True:
            data = conn.recv(1024).decode("utf-8")
            conn.send(f"Buenos días {data}".encode('utf-8'))
            if not data:
                break