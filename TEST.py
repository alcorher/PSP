import subprocess
import threading
import sys
import time

# Lanzar ollama (usa "ollama run" en modo interactivo)
proc = subprocess.Popen(
    ["ollama", "run", "llama3.1:8b"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

# Función/hilo para redirigir salida del modelo
def forward_output():
    try:
        for line in proc.stdout:
            if line:
                print(line, end="")
    except Exception as e:
        print(f"[HILO] Error leyendo stdout: {e}")

t = threading.Thread(target=forward_output, daemon=True)
t.start()

try:
    while True:
        prompt = input("Enter prompt (or /bye to exit): ")

        if prompt.strip() == "/bye":
            break

        if proc.poll() is not None:
            print("El proceso de Ollama ha terminado inesperadamente.")
            break

        try:
            proc.stdin.write(prompt + "\n")
            proc.stdin.flush()
        except Exception as e:
            print("No se pudo enviar el prompt al modelo:", e)
            break

finally:
    try:
        proc.stdin.close()
    except:
        pass

    try:
        proc.terminate()
        proc.wait(timeout=3)
    except:
        try:
            proc.kill()
        except:
            pass

    print("Proceso cerrado correctamente.")
