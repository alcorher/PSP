import threading
import time
import random

puntuacion = 0
listaJuez = ['JUANJUEZ', 'PEDROJUEZ', 'MARIOJUEZ', 'LUISJUEZ', 'CARLOJUEZ', 'JUANAJUEZ']

def incrementar_puntuacion():
    global puntuacion
    lock.acquire()
    puntos = random.randint(1, 10)
    print(f"{threading.current_thread().name} añade {puntos} puntos.")
    puntuacion += puntos
    lock.release()
        







lock = threading.Lock()
hilos = []
for j in listaJuez:
    t = threading.Thread(target=incrementar_puntuacion, name=j)
    t.start()
    hilos.append(t)

for hilo in hilos:
    hilo.join()

print(f"Puntuacion total: {puntuacion}")
