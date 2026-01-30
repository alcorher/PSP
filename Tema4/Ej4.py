import ftplib

#credenciales FTP, la contraseña la cambian cada cierto tiempo
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

def listCallback(line):
    print(line)


ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

ftp.encoding = "utf-8"
welcomeMessage = ftp.getwelcome()
print(welcomeMessage)
fichero_enServidor = "archivo_subido.txt"
fichero_local = "archivo_descargado.txt"
with open(fichero_local, "wb") as file:
    ftp.retrbinary(f"RETR {fichero_enServidor}", file.write)
respMessage = ftp.retrlines("LIST")
print("--------------------")
print(respMessage)



#cerrar la conexión
ftp.quit()