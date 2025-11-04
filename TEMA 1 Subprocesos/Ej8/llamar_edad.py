import subprocess

process = subprocess.Popen(["python", "Ej8\\ComprobarEdad.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output, errors = process.communicate(b"18\n")
print(output.decode(errors='ignore'))
