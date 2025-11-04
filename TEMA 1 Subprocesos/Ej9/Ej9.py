import psutil

try:
    for proc in psutil.process_iter():
        print(f"PID: {proc.pid}, Nombre: {proc.name()}, Uso de memoria: {proc.memory_percent()}")

except:
    print("Error")

  
print("")
pid = int(input("Ingrese el PID del proceso que desea finalizar: "))
if psutil.pid_exists(pid):
    proceso = psutil.Process(pid)
    proceso.terminate()
    print(f"Proceso con PID {pid} finalizado.")
else:
    print(f"No existe un proceso con PID {pid}.")

