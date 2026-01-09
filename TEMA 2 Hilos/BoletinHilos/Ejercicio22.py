import threading
import time

def simularTareas(s):
    with s:
        print(f"{threading.current_thread().name} voy a hacer una tarea. ENTRO")
        time.sleep(1)
        print(f"{threading.current_thread().name} ya he terminado. SALGO")


if __name__ == "__main__":
    s = threading.Semaphore(3)
    for _ in range(8):
        t = threading.Thread(target=simularTareas, args=(s,))
        t.start()
        