class Date:
    def __init__(self,weekDay,hour,minute):
        self.weekDay = weekDay
        self.hour = hour
        self.minute = minute

    def minutify(self):
        return hour*60 + minute
