import threading

def imprimir5Veces(letra):
    for i in range(5):
        print(f" Hilo {letra} ")


t1 = threading.Thread(target=imprimir5Veces, args=("a"))
t2 = threading.Thread(target=imprimir5Veces, args=("b"))
t3 = threading.Thread(target=imprimir5Veces, args=("c"))
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()



