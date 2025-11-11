import threading

contador = 0

def incrementar():
    global contador
    for _ in range(1000):
        contador += 1

hilos = []  
for i in range(2):
    t = threading.Thread(target=incrementar)
    hilos.append(t)

for t in hilos:
    t.start()
for t in hilos:
    t.join()
print("Valor final del contador:", contador)