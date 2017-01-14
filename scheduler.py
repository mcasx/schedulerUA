from event import Event
from event import Class
from date import Date

#Returns True if there is any event in events2 that is overlapped by event
def OverlapConstraint(events1,events2):
    for e1 in events1:
        for e2 in [ e for e in events2 if e.startDate.weekDay == e1.startDate.weekDay and e1.startDate.minutify() <= e.startDate.minutify() ]:
            if e1.startDate.minutify() + e1.duration > e2.startDate.minutify():
                return True
    return False

#Returns dictionary with the solution
def search(domain, constraints):
    #Returns none if there is no solution
    if any([ domain[key] == [] for key in domain.keys()]):
        return None
    #Returns solution if found
    if all([ len(domain[key]) == 1 for key in domain.keys() ]):
        return [ domain ]

    #Orders keys in order of increasing length of domain
    keys = sorted(domain.keys(), key = lambda x: len(domain[x]))
    #Missing picking value by most constraints created
    solutions = []
    for key in keys:
        if len(domain[key]) > 1:
            for value in domain[key]:
                nDomain = dict(domain)
                #Pick a value
                nDomain[key] = [value]
                #Other variables values are the ones that are not constrained by picked value
                for key2 in [ x for x in keys if x != key ]:
                    nDomain[key2] = [ x for x in nDomain[key2] if not any([ y(value.events,[ e for c in nDomain[key2] for e in c.events ]) or y([ e for c in nDomain[key2] for e in c.events ],value.events) for y in constraints ]) ]
                solutions += [ x for x in search(nDomain, constraints) ]
    return solutions

def Scheduler(classes):
    domain = { c.t: [] for c in classes}
    for c in classes:
        domain[c.t] += [c]
    return search(domain,[OverlapConstraint])
"""
BDP1 = Class("BD-P",1)
BDP2 = Class("BD-P",2)
BDP3 = Class("BD-P",3)
BDP4 = Class("BD-P",4)
BDP5 = Class("BD-P",5)
BDP6 = Class("BD-P",6)
ARP1 = Class("AR-P",1)
ARP3 = Class("AR-P",3)
ARP4 = Class("AR-P",4)
ARP5 = Class("AR-P",5)
BDP1.events += [ Event( Date(1,16,0), 120 ) ]
BDP2.events += [ Event( Date(2,14,0), 120 ) ]
BDP3.events += [ Event( Date(4,11,0), 120 ) ]
BDP4.events += [ Event( Date(1,9,0), 120 ) ]
BDP5.events += [ Event( Date(1,11,0), 120 ) ]
BDP6.events += [ Event( Date(4,9,0), 120 ) ]
ARP1.events += [ Event( Date(4,14,0), 180 ) ]
ARP3.events += [ Event( Date(1,13,0), 180 ) ]
ARP4.events += [ Event( Date(5,10,0), 180 ) ]
ARP5.events += [ Event( Date(5,14,0), 180 ) ]


classes = [ BDP1, BDP2, BDP3, BDP4, BDP5, BDP6, ARP1, ARP3, ARP4, ARP5 ]
s = Scheduler(classes)
print( [ [ y.t + str(y.st) for key in x for y in x[key] ] for x in s ] )
"""
