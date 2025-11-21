import threading
import time

def productor(cond):
    global numero
    for i in range (1,6):
        with cond:
            cond.wait()
            numero = i
            time.sleep(0.5)
            print (f" {threading.current_thread().name} Valor {i} producido")
            cond.notify()

def consumidor(cond):
    global numero
    for i in range (1,6):
        with cond:
            cond.wait()
            time.sleep(0.5)
            print(f" {threading.current_thread().name}  He comsumido el numero {numero}")
            cond.notify()


if __name__ == "__main__":
    cond = threading.Condition()
    t1 = threading.Thread(target=productor, args=(cond,))
    t2 = threading.Thread(target=consumidor, args=(cond,))

    t1.start()
    t2.start()

    with cond:
        cond.notify()
