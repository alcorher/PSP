import multiprocessing

def cuadrado(numero):
    print (f"El cuadrado de {numero} = {numero ** 2}")
    

if __name__ == "__main__":
    numeros = [2,4,6,8,10]
    procesos = []
    for n in numeros:
        proceso = multiprocessing.Process(target=(cuadrado), args=(n,))
        procesos.append(proceso)

    for p in procesos:
        p.start()
        print(p, "Está en ejecución")


    for p in procesos:
        p.join()

    print("Ha terminado")
