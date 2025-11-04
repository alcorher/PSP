import subprocess


ruta = "https://search.google.com/search?q=" 
ruta += input("Ingrese su búsqueda: ")
subprocess.run(["C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe", ruta])