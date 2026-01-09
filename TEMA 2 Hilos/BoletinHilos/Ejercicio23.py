import threading
import time


s = threading.Semaphore(1)

def imprimir():
    
    print(f"Hilo {threading.current_thread().name} está esperando para imprimir")
    s.acquire()
    try:
        print(f"Hilo {threading.current_thread().name} comienza a imprimir")
        time.sleep(2)
        print(f"Hilo {threading.current_thread().name} termina de imprimir")
    finally:
        s.release()

threads = []
for i in range(1, 7):
    t = threading.Thread(target=imprimir)
    threads.append(t)
    t.start()

for t in threads:
    t.join()