from event import Event
from date import Date

#Returns True if there is any date overlap in the domain
def OverlapConstraint(domain):
    events = [ e for key in domain.keys() for c in domain[key] for e in c.events ]
    for e1 in events:
        for e2 in [ e for e in events if e.weekDay == e1.weekDay and e1.startDate.minutify() <= e.startDate.minutify()]:
            if e1.startDate.minutify() + e1.duration > e.startDate.minutify():
                return True
    return False

def Scheduler(classes):
    domain = { c.t: [] for c in classes}
    for c in classes:
        domain[c.t] += [c]
    cs = ConstraintSearch(domain,[SubTypeConstraint,OverlapConstraint])
    return cs.search()
