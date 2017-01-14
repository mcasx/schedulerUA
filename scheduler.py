from event import Event
from date import Date

#Returns True if there are different subtypes for a type
def SubTypeConstraint(domain):
    for key in domain.keys():
        if len(set([ e.st for e in domain[key])) != 1:
                return True
    return False

#Returns True if there is any date overlap in the domain
def overlapConstraint(domain):
    pass

def Scheduler(events):
    domain = { e.t: [] for e in events}
    for e in events:
        domain[e.t] += [e]
