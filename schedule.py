import datetime

class Schedule(object):
    def __init__(self, start_t, end_t, days):
        self.start_time = start_t
        self.end_time = end_t
        self.days = days
        self.last_sent = datetime.time(0)
