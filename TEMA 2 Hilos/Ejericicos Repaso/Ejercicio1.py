import threading
import time
import random

listCaballos = ["Relámpago", "Trueno", "Tornado", "Pegaso", "Centella", "Viento", "Sombra", "Cometa"]


def caballo():
    print(f"{threading.current_thread().name} está en la linea de Salida")
    barrier.wait()
    print(f"{threading.current_thread().name} empieza a correr")
    time.sleep(random.randint(1,5))
    print(f"{threading.current_thread().name} ha llegado a la meta")


barrier = threading.Barrier(len(listCaballos))
hilos = []

for c in listCaballos:
    t = threading.Thread(target=caballo, name=c)
    t.start()
    hilos.append(t)

for hilo in hilos:
    hilo.join()

print("Carrera terminada")