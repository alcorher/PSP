import threading

def saludo():
    print("Hola desde el hilo secundario")



for i in range(5):
    print("Hola desde el hilo principal")

    hilo = threading.Thread(target=saludo)
    hilo.start()