import threading

listaLetras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def imprimirMinusculas(cond):
    global listaLetras
    for letra in listaLetras:
        with cond:
            cond.wait()
            print(letra.lower())
            cond.notify()

def imprimirMayusculas(cond):
    global listaLetras
    for letra in listaLetras:
        with cond:
            cond.wait()
            print(letra.upper())
            cond.notify()
    

if __name__ == "__main__":
    cond = threading.Condition()
    t1 = threading.Thread(target=imprimirMinusculas, args=(cond,))
    t2 = threading.Thread(target=imprimirMayusculas, args=(cond,))

    t1.start()
    t2.start()

    with cond:
        cond.notify()