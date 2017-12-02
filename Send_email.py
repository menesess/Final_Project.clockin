import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

class Email_reminder():
    def __init__(self, subject, body):
        self.subject = subject
        self.message = body
        self.recipient = "guillermoramos330179@gmail.com"
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)

    def check_time(self, schedule):
        if datetime.datetime.now().day == schedule.start_time.day:
            if datetime.datetime.now().hour == schedule.start_time.hour:
                if datetime.datetime.now().minute == schedule.start_time.minute:
                    self.send_email()

    def compose_email(self):
        self.msg['From'] = "justcallmemarvin@gmail.com"
        self.msg['To'] = self.recipient
        self.msg['subject'] = "TIME-PUNCH REMINDER"
        self.msg.attach(MIMEText(self.message, 'plain'))

    def send_email(self):
        self.server.sendmail("justcallmemarvin@gmail.com", self.recipient, self.msg.as_string())
        self.server.quit()

    def login(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login("justcallmemarvin@gmail.com", "Enilorac08!")

def main():
    while True:
        return email.check_time

    body = "Hi, Pollito! Please click on the link below to clock in/out. /n https://timemachine1-vm.berea.edu/UltraTime/UltraPunch/login.aspx?ReturnUrl=%2fultratime%2fultrapunch%2findex.aspx"




