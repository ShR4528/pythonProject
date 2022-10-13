import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with smtplib.SMTP('smtp.zone.eu', 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('python@mrartful.com', 'qwe576!sdf')

    msg = MIMEMultipart()
    msg['From'] = 'python@mrartful.com'
    msg['To'] = 'shr4528@gmail.com'
    msg['Subject'] = 'Python test email sent robot'
    body = 'Python test mail'
    body2 = f'<h1>Hello World<h2>' \
                   f'<p style="color: red"> Hello people</p>'
    #msg.attach(MIMEText(body, 'html'))
    msg.attach(MIMEText(body2, 'html'))
    text = msg.as_string()

    server.sendmail('python@mrartful.com', 'shr4528@gmail.com', text)



