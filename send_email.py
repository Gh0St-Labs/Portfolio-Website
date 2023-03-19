import smtplib
import ssl

def send_email(msg):
    host = "smtp.gmail.com"
    port = 465

    gmail = 'syondukeabraham@gmail.com'
    password = "bbspwcsoexkyddsp"

    receiver = 'syondukeabraham@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(gmail, password)
        server.sendmail(from_addr=gmail, to_addrs=receiver, msg=msg)
