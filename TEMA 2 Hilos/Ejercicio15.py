import threading
import time
def tareaImpresion():
    #lock.acquire()
    print(f"Iniciando impresion impresora: {threading.current_thread().name}")
    for i in range(10):
        print(f"Imprimiendo página {i}...")
        time.sleep(0.15)
    print(f"Finalizado ({threading.current_thread().name})")
    #lock.release()

if __name__ == "__main__":
    #lock = threading.Lock()
    hilos = []
    for _ in range(5):
        t = threading.Thread(target=tareaImpresion)
        hilos.append(t)
        t.start()  

    for t in hilos:
        t.join()    

    print("Todas las impresiones han finalizado.")
  