import threading
import time

def accesoBD(s):
    with s:
        print(f"{threading.current_thread().name} está accediendo a la base de datos.")
        time.sleep(2)    
        print(f"{threading.current_thread().name} ha terminado de acceder a la base de datos.")
        time.sleep(0.1)

if __name__ == "__main__":
    s = threading.Semaphore(3)  
    for _ in range(10):
        t = threading.Thread(target=accesoBD, args=(s,))
        t.start()


