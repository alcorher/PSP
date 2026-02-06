import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText


#direccion, contraseña y destinatario
enviado_por = 'acorher2911@g.educaand.es'
password = 'jefg bufp pwjj kwik'
to = input('Introduce el correo del destinatario: ')
#Establecimiento MIME
mensaje = MIMEMultipart()

mensaje['From'] = enviado_por

mensaje[ 'To'] = to

mensaje[ 'Subject'] = input('Introduce el asunto del correo: ')
body=input('Introduce el cuerpo del correo: ')
#Cuerpo y adjuntos para el correo
mensaje.attach(MIMEText (body, 'plain'))
#Sesión SMTP para el envío del correo 
try:
    session= smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port 
    session.starttls() #enable security
    session.login(enviado_por, password) #login with mail id and password
    text = mensaje.as_string()
    session.sendmail (enviado_por, to, text)
    session.quit()
    print('Mensaje enviado')
except Exception as e:
    print ('Algo fue incorrecto...', e)