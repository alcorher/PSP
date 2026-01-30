import ftplib

FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

def listCallback(line):
    print(line)

try:
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"

    print(ftp.getwelcome())

    fichero = "archivo_subido.txt"
    fichero_renombrado = "archivo_subido_renombrado.txt"

    ftp.rename(fichero, fichero_renombrado)

    print("--------")
    ftp.retrlines("LIST", listCallback)

    ftp.delete(fichero_renombrado)

except ftplib.all_errors as e:
    print(f"Error FTP: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar conexión
    ftp.quit()
