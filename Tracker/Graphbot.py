import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


msg=MIMEMultipart()
msg['Subject']='SteamGameTrackerAlpha0.01'
msg['From']='Suzi'
msg['To']= input("plz input your email :P")

with open('day.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename="day.jpg")
    msg.attach(img)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("eess25853@gmail.com","403010Ab")
    server.send_message(msg)

print("Graph Sented(๑•̀ㅂ•́)و✧")

