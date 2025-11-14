import threading
import time

class ContadorHilo(threading.Thread):
    def __init__(self, limite, nombre):
        super().__init__()
        self.limite = limite
        self.nombre = nombre

    def run(self):
        for i in range(self.limite + 1):
            print(f"{self.nombre} --> {i}")
            time.sleep(0.2)


# Ejemplo de uso
if __name__ == "__main__":
    t1 = ContadorHilo(5, "Hilo-1")
    t2 = ContadorHilo(3, "Hilo-2")
    t3 = ContadorHilo(10, "Hilo-3")

    threads = []
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("Finalizado")