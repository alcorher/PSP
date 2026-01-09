import threading

def hilo(n1, n2):
    for i in range(n1, n2):
        print(i)



n1 = 1
n2 = 51
print(f"Entre {n1} y {n2} hay {n2-n1} números")
t = threading.Thread(target=hilo, args=(n1, n2))
t.start()