import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(subject, body):
    smtp_server = "email_server
    port = 587 #servico aberto smtp
    sender_email = "email_enviar"
    password = "senha"
    receiver_email = "email_receber"

    if sender_email is None or password is None:
        print("Erro: Variáveis de ambiente EMAIL_USERNAME ou EMAIL_PASSWORD não foram definidas.")
        return

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("E-mail enviado com sucesso!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Erro de autenticação: {e}")
    except smtplib.SMTPException as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")
    finally:
        server.quit()
