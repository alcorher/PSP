import threading
import time
import random

listAlumnos = ["Ana", "Luis", "María", "Pedro", "Sofía", "Jorge", "Marta", "Carlos", "Joselito"]

def examen():
    print(f"{threading.current_thread().name} ha llegado a clase.")
    
    with cond:
        cond.wait()
    print(f"{threading.current_thread().name} ha empezado el examen.")
    time.sleep(random.randint(1, 5))
    print(f"{threading.current_thread().name} ha terminado el examen")
        

cond = threading.Condition()

hilos = []

for alum in listAlumnos:
    t = threading.Thread(target=examen, name=alum)
    t.start()
    hilos.append(t)

print("Todos los alumnos han llegado a clase\nEl profesor empieza a repartir los examenes")
time.sleep(2)
print("El profesor da la orden de comenzar el exámen")
with cond:
    cond.notify_all()

for hilo in hilos:
    hilo.join()


print("El profesor se despide")
