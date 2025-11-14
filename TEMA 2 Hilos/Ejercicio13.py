import threading
import random 

def sumaRandom():
    resultado = 0
    for _ in range(1000):
        resultado += random.randint(1,100)
    print(resultado)

t1 = threading.Thread(target=sumaRandom)
t2 = threading.Thread(target=sumaRandom)
t3 = threading.Thread(target=sumaRandom)

hilos = []
hilos.append(t1)
hilos.append(t2)
hilos.append(t3)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Acabado")