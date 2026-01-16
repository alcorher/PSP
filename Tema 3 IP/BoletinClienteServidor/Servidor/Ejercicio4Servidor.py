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
        data = conn.recv(1024).decode('utf-8')
        nVocales = 0
        vocalesList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for palabra in data:
            for letra in palabra:
                if letra in vocalesList:
                    nVocales += 1
        conn.send(str(nVocales).encode('utf-8'))

        
                
                
                     
