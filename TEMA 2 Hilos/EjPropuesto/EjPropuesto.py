
import threading

areas = []

def areaTriangulo(base, altura):
    area = (base * altura) / 2
    areas.append(area)
    print("Area es : ", area)

def areaRectángulo(base,altura):
    area = base * altura
    areas.append(area)
    print("Area es : ", area)


hilos = []
t1 = threading.Thread(target=areaTriangulo, args=(10,12))
t2 = threading.Thread(target=areaRectángulo, args=(8,12))
t3 = threading.Thread(target=areaRectángulo, args=(6,5))
t4 = threading.Thread(target=areaTriangulo, args=(2,5))

hilos.append(t1)
hilos.append(t2)
hilos.append(t3)
hilos.append(t4)

for hilo in hilos:
    hilo.start()
    print("Hilo ", hilo.name, " iniciando")
for hilo in hilos:
    hilo.join()


print("Total: ", sum(areas))
