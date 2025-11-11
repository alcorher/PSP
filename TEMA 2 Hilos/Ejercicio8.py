import threading
import time
def contador(n):
    for i in range(0, n+1):
        print(threading.current_thread().name, ":", i , "segundos")
        time.sleep(1)


if __name__ == "__main__":
    hilos = []
    numeros = [5, 8, 10]

    for n in numeros:
        t = threading.Thread(target=contador, args=(n,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()
    
    print("Todos los hilos han finalizado")
