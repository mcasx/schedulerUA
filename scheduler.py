from event import Event
from event import Class
from date import Date

def freeMornings(solution,weight):
    mornings = [ True ] * 7
    events = [ e for key in solution.keys() for c in solution[key] for e in c.events]
    for e in events:
        if e.startDate.hour < 12:
            mornings[e.startDate.weekDay] = False
    return sum(mornings)*weight

def freeAfternoons(solution,weight):
    afternoons = [ True ] * 7
    events = [ e for key in solution.keys() for c in solution[key] for e in c.events]
    for e in events:
        if e.startDate.hour > 12:
            afternoons[e.startDate.weekDay] = False
    return sum(afternoons)*weight

def freeDays(solution,weight):
    weekdays = [ True ] * 7
    events = [ e for key in solution.keys() for c in solution[key] for e in c.events]
    for e in events:
        weekdays[e.startDate.weekDay] = False
    return sum(weekdays)*weight

def evaluation(solution, weights):
    return freeMornings(solution,weights[0]) + freeAfternoons(solution,weights[1]) + freeDays(solution,weights[2])

#Returns True if any event in c1 overlaps any event in c2
def OverlapConstraint(c1,c2):
    for e in c1.events:
        for e2 in c2.events:
            if e.startDate.weekDay == e2.startDate.weekDay and e.startDate.minutify() + e.duration > e2.startDate.minutify():
                return True
    return False

#Returns dictionaries with the solutions
def search(domain, constraints):
    #Returns none if there is no solution
    if any([ domain[key] == [] for key in domain.keys()]):
        return None
    #Returns solution if found
    if all([ len(domain[key]) == 1 for key in domain.keys() ]):
        return [ domain ]

    #Orders keys in order of increasing length of domain
    keys = sorted(domain.keys(), key = lambda x: len(domain[x]))
    key = [ k for k in keys if len(domain[k]) > 1 ][0]
    #Missing picking value by most constraints created
    solutions = []
    for value in domain[key]:
        nDomain = dict(domain)
        #Pick a value
        nDomain[key] = [value]
        #Other variables values are the ones that are not constrained by picked value
        for key2 in [ x for x in keys if x != key ]:
            nDomain[key2] = [ clas for clas in nDomain[key2] for func in constraints if not func(value,clas) or not func(clas,value) ]
        s = search(nDomain, constraints)
        if s:
            solutions += [ x for x in search(nDomain, constraints) ]
    return solutions

def Scheduler(classes,n):
    weights = [0]*3
    print("Rate your interest [0,10]:")
    print("free mornings -> ", end = "")
    weights[0] = input()
    print("free afternoons -> ", end = "")
    weights[1] = input()
    print("free days -> ", end = "")
    weights[2] = input()
    domain = { c.t: [] for c in classes}
    for c in classes:
        domain[c.t] += [c]
    s = search(domain,[OverlapConstraint])
    s.sort(key = lambda x: evaluation(x,weights), reverse = True)
    return s[:n]


BDP1 = Class("BD-P",1)
BDP2 = Class("BD-P",2)
BDP3 = Class("BD-P",3)
BDP4 = Class("BD-P",4)
BDP5 = Class("BD-P",5)
BDP6 = Class("BD-P",6)
BDTP1 = Class("BD-TP",1)
BDTP2 = Class("BD-TP",2)
BDP1.events += [ Event( Date(1,14,0), 120 ) ]
BDP2.events += [ Event( Date(2,9,0), 120 ) ]
BDP3.events += [ Event( Date(4,15,0), 120 ) ]
BDP4.events += [ Event( Date(2,11,0), 120 ) ]
BDP5.events += [ Event( Date(1,16,0), 120 ) ]
BDP6.events += [ Event( Date(2,14,0), 120 ) ]
BDTP1.events += [ Event( Date(1,11,0), 120) ]
BDTP2.events += [ Event( Date(1,9,0), 120) ]

ARP1 = Class("AR-P",1)
ARP3 = Class("AR-P",3)
ARP4 = Class("AR-P",4)
ART1 = Class("AR-T",1)
ARP1.events += [ Event( Date(4,15,0), 180 ) ]
ARP3.events += [ Event( Date(5,14,0), 180 ) ]
ARP4.events += [ Event( Date(1,16,0), 180 ) ]
ART1.events += [ Event( Date(2,16,0), 60 ), Event( Date(4,14,0), 60) ]

IHCP1 = Class("IHC-P",1)
IHCP2 = Class("IHC-P",2)
IHCP3 = Class("IHC-P",3)
IHCP4 = Class("IHC-P",4)
IHCP5 = Class("IHC-P",5)
IHCP6 = Class("IHC-P",6)
IHCTP1 = Class("IHC-TP",1)
IHCTP2 = Class("IHC-TP",2)
IHCP1.events += [ Event( Date(4,11,0), 120 ) ]
IHCP2.events += [ Event( Date(2,11,0), 120 ) ]
IHCP3.events += [ Event( Date(2,11,0), 120 ) ]
IHCP4.events += [ Event( Date(2,16,0), 120 ) ]
IHCP5.events += [ Event( Date(4,9,0), 120 ) ]
IHCP6.events += [ Event( Date(3,13,0), 120 ) ]
IHCTP1.events += [ Event( Date(2,14,0), 120 ) ]
IHCTP2.events += [ Event( Date(2,9,0), 120 ) ]

PEITP1 = Class("PEI-TP",1)
PEITP2 = Class("PEI-TP",2)
PEITP3 = Class("PEI-TP",3)
PEITP1.events += [ Event( Date(3,13,0), 120 ) ]
PEITP2.events += [ Event( Date(3,9,0), 120 ) ]
PEITP3.events += [ Event( Date(3,11,0), 120 ) ]

classes = [ BDP1, BDP2, BDP3, BDP4, BDP5, BDP6, BDTP1, BDTP2, ARP1, ARP3, ARP4, ART1, IHCP1, IHCP2, IHCP3, IHCP4, IHCP5, IHCP6, IHCTP1, IHCTP2, PEITP1, PEITP2, PEITP3 ]
print("Number of schedules to be generated? -> ", end = "")
n = int(input())
s = Scheduler(classes,n)
print([ [ x.t + str(x.st) for key in solution for x in solution[key] ] for solution in s ])
