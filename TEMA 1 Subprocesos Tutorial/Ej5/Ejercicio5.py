import subprocess
import time


process = subprocess.Popen("calc.exe")
time.sleep(5)
process.terminate()
while process.poll is None:
    print("La calculadora sigue abierta.")
   

