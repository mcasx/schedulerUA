from event import Event
from date import Date

#Returns True if there is any event in class1 overlaps class2
def OverlapConstraint(class1,class2):
    for e1 in class1.events:
        for e2 in [ e for e in class2.events if e.weekDay == e1.weekDay and e1.startDate.minutify() <= e.startDate.minutify()]:
            if e1.startDate.minutify() + e1.duration > e2.startDate.minutify():
                return True
    return False

def Scheduler(classes):
    domain = { c.t: [] for c in classes}
    for c in classes:
        domain[c.t] += [c]
    cs = ConstraintSearch(domain,[SubTypeConstraint,OverlapConstraint])
    return cs.search()
