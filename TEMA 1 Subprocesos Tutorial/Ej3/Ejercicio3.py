import subprocess
process = subprocess.Popen(["ping", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
print(output.decode(errors='ignore'))
print(error.decode(errors='ignore'))