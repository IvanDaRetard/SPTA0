import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg['Subject']='SteamGameTrackerAlpha0.01'
msg['From']='Suzi'
msg['To']= input("plz input your email :P")

with open('T&p per hour.csv') as myfile:
    data=myfile.read()
    msg.set_content(data)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("server_mail","server_password")
    server.send_message(msg)

print("Data Sented(๑•̀ㅂ•́)و✧")

