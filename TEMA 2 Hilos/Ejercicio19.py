import threading
import time


def hilo():
    print(f"{threading.current_thread().name}: Despertado y en espera")
    barrera.wait()
    print(f"{threading.current_thread().name}: Comenzando")
    time.sleep(2)
    print(f"{threading.current_thread().name}: Finalizado")

if __name__ == "__main__":
    barrera = threading.Barrier(10)
    for _ in range(10):
        t = threading.Thread(target=hilo)
        t.start()