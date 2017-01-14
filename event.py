class Class:
    def __init__(self,t,st):
        #self.t is type of event, pe: AC1-P
        self.t = t
        #self.st is subtype of event, p.e.: 1
        self.st = st
        self.events = []

class Event:
    def __init__(self,startDate,duration):
        self.startDate = startDate
        #duration in minutes
        self.duration = duration


