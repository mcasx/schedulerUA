class Date:
    def __init__(self,weekDay,hour,minute):
        self.weekDay = weekDay
        self.hour = hour
        self.minute = minute

    def minutify(self):
        return self.hour*60 + self.minute
