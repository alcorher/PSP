import threading
import time


class RelojHijo(threading.Thread):
    def __init__(self, segundos ):
        super().__init__()
        self.segundos = segundos

    def run(self):
        for i in range(self.segundos, 0, -1):
            print(f"Reloj: {i}")
            time.sleep(1)
    


if __name__ == "__main__":
    t1 = RelojHijo(5)
    
    t1.start()
    
    t1.join()
    
    print("Finalizado")