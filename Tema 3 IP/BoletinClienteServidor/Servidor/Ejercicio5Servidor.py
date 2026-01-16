import socket
HOST = '127.0.0.1'
PORT = 2000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conexión existosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
        
        contieneLetra = False
        contieneDigito = False
        respuesta = "Contraseña insegura" 
        continuar = True
        while continuar:
            data = conn.recv(1024).decode('utf-8')
            if len(data) >= 8:
                for letra in data:
                    if letra.isdigit():
                        contieneDigito=True
                    if letra.isalpha():
                        contieneLetra=True
                if contieneLetra and contieneDigito:
                    respuesta = "Contraseña segura"
                    continuar = False
            
            conn.send(respuesta.encode('utf-8'))
            
            

        
        

        
                
                
                     
