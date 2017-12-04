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
import datetime

class Schedule(object):
    def __init__(self, start_t, end_t, days):
        self.start_time = start_t
        self.end_time = end_t
        self.days = days
        self.last_sent = datetime.time(0)
