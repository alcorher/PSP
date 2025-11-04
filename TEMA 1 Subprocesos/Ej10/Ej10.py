import psutil

nombre_proceso = input("Introduce el nombre del proceso a matar: ") + ".exe"

for proceso in psutil.process_iter(['name' , 'pid']):
    if proceso.info["name"] == nombre_proceso:
        proceso = psutil.Process(proceso.info["pid"])
        proceso.terminate()
        print(f"Proceso {nombre_proceso} terminado.")