import threading
import time
barrier = threading.Barrier(5)

def tarea():
    time.sleep(1)
    print(f"Hilo {threading.current_thread().name} estan detenidos")
    barrier.wait()
    time.sleep(1)
    print(f"Hilo {threading.current_thread().name} ha continuado")
threads = []
for i in range(5):
    t = threading.Thread(target=tarea)
    threads.append(t)
    t.start()

for t in threads:
    t.join()