from event import Event
from date import Date

#Returns True if there is any event in class1 overlaps class2
def OverlapConstraint(class1,class2):
    for e1 in class1.events:
        for e2 in [ e for e in class2.events if e.weekDay == e1.weekDay and e1.startDate.minutify() <= e.startDate.minutify()]:
            if e1.startDate.minutify() + e1.duration > e2.startDate.minutify():
                return True
    return False

#Returns dictionary with the solution
def search(self,domain, constraints):
    #Returns none if there is no solution
    if any([ domain[key] == [] for key in domain.keys()]):
        return None
    #Returns solution if found
    if all([ len(domain[key]) == 1 for key in domain.keys() ]):
        return domain

    #Orders keys in order of increasing length of domain
    keys = sorted(domain.keys(), key = len(domain[key]))
    #Missing picking value by most constraints created
    nDomain = dict(domain)
    for key in keys:
        if len(nDomain[key]) > 1:
            for value in nDomain[key]:
                #Pick a value
                nDomain[key] = [value]
                #Other variables values are the ones that are not constrained by picked value
                for x in [ x for x in keys if x != key ]:
                    nDomain[x] = [ x for x in nDomain[x] if not any([ y(nDomain[key],nDomain[x]) or y(nDomain[x],nDomain[key]) for y in constraints ]) ]
                solution = search(nDomain)
                if solution != None:
                    return solution
    return None


def Scheduler(classes):
    domain = { c.t: [] for c in classes}
    for c in classes:
        domain[c.t] += [c]
    return search(domain,[SubTypeConstraint,OverlapConstraint])
