import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading

def enviar_archivo(destinatario, asunto, cuerpo, archivo):
    # Configuración del servidor SMTP
    servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Cambia esto según tu proveedor de correo
    servidor.starttls()
    servidor.login('alcorher2@gmail.com', 'tuwe mkiw rsjx pnlb')  # Cambia por tus credenciales

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = 'alcorher2@gmail.com'
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo
    with open(archivo, 'rb') as adjunto:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={archivo}')
        mensaje.attach(parte)

    # Enviar el mensaje
    servidor.send_message(mensaje)
    servidor.quit()

# Uso del código

def enviar_10_veces():
    mensaje = random.randint(1, 76495473)
    while True:
        mensaje += 1
        enviar_archivo('serteme06@gmail.com', f"Mondongo {mensaje}", f"{mensaje}", 'mondongo.png')
        print('Archivo enviado con éxito')


def pepe():
    thread = threading.Thread(target=enviar_10_veces)
    thread.start()

    thread.join()


if __name__ == "__main__":
    while True:
        h = threading.Thread(target=pepe).start()
        h.join()
    
