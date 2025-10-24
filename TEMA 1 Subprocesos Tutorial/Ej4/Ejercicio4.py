#LLamar suma
import subprocess

process = subprocess.Popen(["python", "Ej4\\sumar_dos_numeros.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

subprocess_input = (b"3\n5\n")
output, error = process.communicate(input=subprocess_input)

print(output.decode())
print(error.decode())
