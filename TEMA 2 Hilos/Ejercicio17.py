import threading

def imprimirPares(cond):
    for i in range (11):
        with cond:
            cond.wait()
            if (i % 2 == 0):
                print(f"{threading.current_thread().name}: {i}")
            cond.notify()

def imprimirImpares(cond):
    for i in range (10):
        with cond:
            cond.wait()
            if (i % 2 != 0):
                print(f"{threading.current_thread().name}: {i}")
            cond.notify()

        

cond = threading.Condition()

t1 = threading.Thread(target=imprimirPares, args=(cond,))
t2 = threading.Thread(target=imprimirImpares, args=(cond,))

t1.start()
t2.start()
with cond:
    cond.notify()




