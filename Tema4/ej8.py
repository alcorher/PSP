import imaplib
#direccion, contraseña y destinatario
user= 'acorher2911@g.educaand.es'
password = 'jefg bufp pwjj kwik'
#conexion al servidor
mail = imaplib.IMAP4_SSL('imap.gmail.com')

def get_emails():
    try:
        mail.login(user, password)
        mail.select('inbox')
        

        status, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()
        print(f"Total de correos: {len(email_ids)}")
    except imaplib.IMAP4.error as e:
        print(f"Error de IMAP: {e}")
    finally:
        mail.close()
        mail.logout()

    get_emails()