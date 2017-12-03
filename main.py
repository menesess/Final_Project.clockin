from schedule import Schedule
from send_email import Email_reminder
import datetime

def main():
    monday_morning = Schedule(datetime.time(8), datetime.time(9, 10), [1,3,5])
    monday_afternoon = Schedule(datetime.time(12), datetime.time(1), [1,3,5])
    tuesday_morning = Schedule(datetime.time(9), datetime.time(11), [2,4])
    tuesday_afternoon = Schedule(datetime.time(12), datetime.time(13), [2,4])
    test = Schedule(datetime.time(17, 44), datetime.time(17, 46), [6])

    schedules = [test, monday_morning, monday_afternoon, tuesday_morning, tuesday_afternoon]

    body = "Hi, Pollito! Please click on the link below to clock in/out. /n https://timemachine1-vm.berea.edu/UltraTime/UltraPunch/login.aspx?ReturnUrl=%2fultratime%2fultrapunch%2findex.aspx"

    email_reminder = Email_reminder('Clock In/Clock Out', body)
    while True:
        for schedule in schedules:
            email_reminder.check_time(schedule)

if __name__ == "__main__":
    main()
