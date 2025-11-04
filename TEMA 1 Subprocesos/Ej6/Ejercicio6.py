import subprocess

opcion = -1

while opcion != 0:
    print("\n=== MENÚ DE APLICACIONES ===")
    print("1. Bloc de notas (Notepad)")
    print("2. Calculadora")
    print("3. Paint")
    print("4. WordPad")
    print("5. Explorador de archivos")
    print("0. Salir")   
    print("============================")
    
    opcion = int(input("Ingrese una opción (0 para salir): "))
    
    match opcion:
        case 1:
            print("Abriendo Bloc de notas")
            result = subprocess.run(["notepad.exe"])
            print(f"Bloc de notas cerrado.")

        case 2:
            print("Abriendo Calculadora")
            result = subprocess.run(["calc.exe"])
            print(f"Calculadora cerrada.")
            
        case 3:
            print("Abriendo Paint")
            result = subprocess.run(["mspaint.exe"])
            print(f"Paint cerrado.")
            
        case 4:
            print("Abriendo WordPad")
            result = subprocess.run(["write.exe"])
            print(f"WordPad cerrado.")
            
        case 5:
            print("Abriendo Explorador de archivos")
            result = subprocess.run(["explorer.exe"])
            print(f"Explorador cerrado.")
            
        case 0:
            print("Saliendo del programa.")
            
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")