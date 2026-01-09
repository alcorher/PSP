import threading
import time
import random

# Ejercicio25.py

def f():
    print(f"{threading.current_thread().name} Está esperando para comenzar la fase 1")
    barrier1.wait()
    print(f"{threading.current_thread().name} Ha comenzado la fase 1")
    time.sleep(random.randint(0,2))
    print(f"{threading.current_thread().name} Ha terminado la fase 1")
    barrier2.wait()
    print(f"{threading.current_thread().name} Ha comenzado la fase 2")
    time.sleep(random.randint(0,2))
    print(f"{threading.current_thread().name} Ha terminado la fase 2")
    


if __name__ == "__main__":
    barrier1 = threading.Barrier(6)
    barrier2 = threading.Barrier(6)

    threads = []
    for i in range(1, 7):
        t = threading.Thread(target=f)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()