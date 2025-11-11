import threading
import time

def imprimirY():
    for i in range(1000):
        print("Y")
        time.sleep(0.001)
        


hilo = threading.Thread(target=imprimirY)
hilo.start()
for i in range(1000):
    print("X")
    time.sleep(0.001)
    
