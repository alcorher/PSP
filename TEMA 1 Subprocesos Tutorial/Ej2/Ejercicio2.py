import subprocess
result = subprocess.run("notepad.exe")
if result.returncode == 0:
    print("El Bloc de notas se cerró correctamente.")