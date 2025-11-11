import threading
import random
import time

def hilo():
    print(f"{threading.current_thread().name} iniciado")
    time.sleep(random.randint(1, 3))
    print(f"{threading.current_thread().name} terminado")


    

if __name__ == "__main__":
    hilos = []
    for i in range(3):
        t = threading.Thread(target=hilo, name=f"Hilo-{i+1}")
        hilos.append(t)
        t.start()

    
    while True:
        activos = threading.active_count()
        nombres = [t.name for t in threading.enumerate()]
        print(f"Hilos en ejecución: {activos}")
        print("Hilos activos:", ", ".join(nombres))
        if activos <= 1:
            print("Ejecución completada")
            break
        time.sleep(1)

    for t in hilos:
        t.join()
