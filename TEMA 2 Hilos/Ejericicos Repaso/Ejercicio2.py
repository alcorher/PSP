import threading
import time

listNombres = ["Ana", "Luis", "María", "Pedro", "Lucía", "Carlos", "Elena", "Javier", "Sara", "Miguel"]

def ascensor():
    print(f"{threading.current_thread().name} está esperando para subir al ascensor")
    s.acquire()
    print(f"{threading.current_thread().name} ha subido al ascensor")
    time.sleep(2)
    print(f"{threading.current_thread().name} ha bajado del ascensor")
    s.release()

s = threading.Semaphore(4)

hilos = []
for n in listNombres:
    t = threading.Thread(target=ascensor, name=n)
    t.start()
    hilos.append(t)

for hilo in hilos:
    hilo.join()

print("El ascensor se ha quedado vacio.")
