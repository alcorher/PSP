import subprocess

proceso = subprocess.Popen(["python", "contar_palabra.py"], stdin=subprocess.PIPE,  stderr=subprocess.PIPE,  stdout=subprocess.PIPE) 

texto = "Python es un lenguaje de programación muy popular. Python se utiliza en el desarrollo web, inteligencia artificial, análisis de datosy automatización de tareas. Muchas empresas confían en Python por su sencillez, legibilidad y amplia comunidad de usuarios. Aprender Python es una excelente decisión para cualquier programador."
palabra = "Python"
output, _ = proceso.communicate(b"Python es un lenguaje de programacion muy popular. Python se utiliza en el desarrollo web, inteligencia artificial, analisis de datos y automatizacion de tareas. Muchas empresas confian en Python por su sencillez, legibilidad y amplia comunidad de usuarios. Aprender Python es una excelente decision para cualquier programador.\nPython\n")
print(output.decode(errors="ignore"))

