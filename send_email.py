#######################################################################################################
# Author: Nina Meneses
# Username: menesess
#
# Assignment: Final Project: Email Reminder
#
# Purpose: To send Guillermo automated email reminders according to his work schedule
#
########################################################################################################
# Acknowledgements: Python Software Foundation, Stack Overflow, Python Library Reference and Guillermo
########################################################################################################
import smtplib  #imports e-mail sending capabilities
from email.mime.multipart import MIMEMultipart  # divides message
from email.mime.text import MIMEText    # creates MIME objects

import datetime # imports datetime library for datetime objects

class Email_reminder():
    """
    This class represents all the necessary components of an email
    """
    def __init__(self,recipient, body):
        """
        Conects to email server and logs in.
        :param recipient: set fro whomever you want to send the reminder to
        :param body: Holds the main message of the email, what you want the recipient to know.
        """
        self.message = body
        self.recipient = recipient
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.compose_email()
        self.login()

    def check_time(self, schedule):
        """
        This function constantly checks the time and compares it to the times set in to the clock-in/out time in schedule
        If the times match up, then the email is sent.
        :param schedule: passing in a schedule object
        :return: none
        """

        if datetime.datetime.now().weekday() in schedule.days:
            if datetime.datetime.time(datetime.datetime.now()).hour == schedule.start_time.hour or datetime.datetime.time(datetime.datetime.now()).hour == schedule.end_time.hour:
                duration = datetime.datetime.combine(datetime.date.min,  datetime.datetime.now().time()) - datetime.datetime.combine(datetime.date.min, schedule.last_sent)
                if datetime.datetime.now().minute == schedule.start_time.minute and duration > datetime.timedelta(minutes = 5) :
                    print('send')
                    self.send_email()
                    schedule.last_sent = datetime.datetime.now().time()

    def login(self):
        """
        Logs in to server with my username and password
        :return: none
        """
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login("example@gmail.com", "Password")  # insert your own username and password

    def compose_email(self):
        """
        Sets email info.
        :return: none
        """
        self.msg['From'] = "example@gmail.com"
        self.msg['To'] = self.recipient
        self.msg['subject'] = "TIME-PUNCH REMINDER"
        self.msg.attach(MIMEText(self.message, 'plain'))

    def send_email(self):
        """
        Sends the email
        :return: none
        """
        self.server.sendmail("justcallmemarvin@gmail.com", self.recipient, self.msg.as_string())
        self.server.quit()
