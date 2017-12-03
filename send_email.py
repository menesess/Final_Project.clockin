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
        self.compose_email()
        self.login()

    def check_time(self, schedule):

        if datetime.datetime.now().weekday() in schedule.days:
            if datetime.datetime.time(datetime.datetime.now()).hour == schedule.start_time.hour or datetime.datetime.time(datetime.datetime.now()).hour == schedule.end_time.hour:
                duration = datetime.datetime.combine(datetime.date.min,  datetime.datetime.now().time()) - datetime.datetime.combine(datetime.date.min, schedule.last_sent)
                if datetime.datetime.now().minute == schedule.start_time.minute and duration > datetime.timedelta(minutes = 5) :
                    print('send')
                    self.send_email()
                    quit()

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





