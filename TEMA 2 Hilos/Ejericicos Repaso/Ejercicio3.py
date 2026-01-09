import threading

def trabajador():
    for _ in range(5):
        with cond:
            cond.wait()
            print(f"{threading.current_thread().name} está trabajando")
            cond.notify()


cond = threading.Condition()
listaTrabajadores = ["Pepe", "José"]
threads = []
for i in listaTrabajadores:
    thread = threading.Thread(target=trabajador, name=i)
    threads.append(thread)
    thread.start()

with cond:
    cond.notify()

for hilo in threads:
    hilo.join()


print("Fin del trabajo")