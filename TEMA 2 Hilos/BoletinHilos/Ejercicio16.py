import threading
import time
saldo = 1000

def retirar_200():
    lock.acquire()
    global saldo
    if saldo >= 200:
        time.sleep(0.1)
        saldo -= 200
    else :
        print("Error saldo insuficiente")
    lock.release()

if __name__ == "__main__":
    lock = threading.Lock()
    hilos = []
    for _ in range(10):
        t = threading.Thread(target=retirar_200)
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()

    print(f"Saldo final: {saldo}")