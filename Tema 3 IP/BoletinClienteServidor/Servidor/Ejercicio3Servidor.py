import socket
HOST = '127.0.0.1'
PORT = 2000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    acumulador = 0
    with conn:
         print(f"Conexión existosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
         while True:
            data = conn.recv(1024).decode('utf-8')
            acumulador += int(data)
            conn.send(str(acumulador).encode('utf-8'))
            if data == 0:
                break
                
                
                     
                