from dotenv import load_dotenv
import smtplib, ssl
import os

load_dotenv()

username = os.getenv("MAIL_USER")
password = os.getenv("MAIL_PASS")
receiver = os.getenv("RECEIVER_EMAIL")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
