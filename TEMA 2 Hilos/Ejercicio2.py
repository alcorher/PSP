import threading
import random
import time

def saludo(n):
    print(f"Soy el hilo {n}")
    time.sleep(random.randint(1, 3))
    print(f"Hilo {n} finalizado")

hilos = []
for i in range(3):
    t = threading.Thread(target=saludo, args=(i+1,))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

print("Todos los hilos han terminado")
