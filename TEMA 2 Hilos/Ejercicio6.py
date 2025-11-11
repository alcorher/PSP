import threading

def mostrar_numeros(nombre, inicio, fin):
    for i in range(inicio, fin):
        print(f"{nombre}: {i}")

t1 = threading.Thread(target=mostrar_numeros, args=("Hilo 1", 1, 10))
t2 = threading.Thread(target=mostrar_numeros, args=("Hilo 2", 20, 30))

t1.start()
t2.start()

t1.join()
t2.join()

print("Finalizado")
