import subprocess

process = subprocess.Popen(["python", "Ej7\\AreaRectangulo.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output, errors = process.communicate(b"5\n10\n")
print(output.decode(errors='ignore'))
