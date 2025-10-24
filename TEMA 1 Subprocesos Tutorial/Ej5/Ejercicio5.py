import subprocess
import time


process = subprocess.Popen("calc.exe")
time.sleep(5)
process.terminate()