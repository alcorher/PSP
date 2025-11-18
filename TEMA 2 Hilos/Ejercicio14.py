import threading
import time
contador = 0

def incrementarContador():
    global contador
    #lock.acquire()
    for _ in range(1000):
        contador += 1
        time.sleep(0.000001)
    #lock.release()
    

if __name__ == "__main__":
    hilos = []
    #lock = threading.Lock()
    for _ in range(20):
        t = threading.Thread(target=incrementarContador)
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()
   
    
    print(contador)