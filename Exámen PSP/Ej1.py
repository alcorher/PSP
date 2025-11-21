import subprocess
import psutil


opcion = int(input("Introduce una opción"))
while opcion != 5:
    match opcion: 


        case 1:
           #Falta cpu
           for proceso in psutil.process_iter(['name' , 'pid', 'status']):
               print(f"Nombre: {proceso.info["name"]} PID: {proceso.info["pid"]} Estado: {proceso.info["status"]}")


        case 2: 
            proceso = subprocess.run("notepad.exe")
            print("El proceso se lanzó correctamente")


        case 3:

            #No funciona 

            procesoPID = input("Introduce el PID del proceso: ")
            for proceso in psutil.process_iter(['pid','name']):
                if int(procesoPID) == int(proceso.info["pid"]):
                    print(f"Nombre: {proceso.info['name']}  Prioridad: {proceso.nice()}")
                

        case 4: 
            procesoPID = input("Introduce el PID del proceso:")
            for proceso in psutil.process_iter(['name' , 'pid']):
                if proceso.info["pid"] == int(procesoPID):
                    proceso = psutil.Process(proceso.info["pid"])
                    proceso.terminate()

            #Falta comprobacion
                    print(f"Proceso terminado.")


            
    opcion = int(input("Introduce una opción"))
               
print("Saliendo del programa...")



