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
from schedule import Schedule
from send_email import Email_reminder
import datetime

def main():
    """
    Everything is called here.
    :return: none
    """
    MWF_morning = Schedule(datetime.time(8), datetime.time(9, 10), [0,2,4])  # Schedule is set here and put into a list.
    MWF_afternoon = Schedule(datetime.time(12), datetime.time(1), [0,2,4])
    TR_morning = Schedule(datetime.time(9), datetime.time(11), [1,3])
    TR_afternoon = Schedule(datetime.time(12), datetime.time(13), [1,3])
    test = Schedule(datetime.time(17, 44), datetime.time(17, 46), [6])

    schedules = [test, MWF_morning, MWF_afternoon, TR_morning, TR_afternoon]

    body = "Hi, Pollito! Please click on the link below to clock in/out. /n https://timemachine1-vm.berea.edu/UltraTime/UltraPunch/login.aspx?ReturnUrl=%2fultratime%2fultrapunch%2findex.aspx"

    email_reminder = Email_reminder("guillermoramos330179@gmail.com", body)

    while True:                                     # while loop goes on forever
        for schedule in schedules:
            email_reminder.check_time(schedule)

if __name__ == "__main__":
    main()
