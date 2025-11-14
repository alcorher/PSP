import threading
import time

class SumaRango(threading.Thread):
    def __init__(self, inicio, fin, resultado):
        super().__init__()
        self.inicio = inicio
        self.fin = fin
        self.resultado = 0

    def run(self):
        for i in range (self.inicio, self.fin):
            self.resultado += i


if __name__ == "__main__":
    hilo1 = SumaRango(1, 50000000, 0)

    hilo1.start()

    hilo1.join()
    
    print(f"El resultado es: {hilo1.resultado}")