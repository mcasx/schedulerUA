class ConstraintSearch:
    def __init__(self,domain,constraints):
        #Domain is a dictionary with var as key and a list of values as value
        self.domain = domain
        #Constraints is a list of functions which require domain as the argument
        self.constraints = constraints

    def search(self,domain = None):
        if domain == None:
            domain = self.domain
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
                        nDomain[x] = [ x for x in nDomain[x] if not any([ y(nDomain[key],nDomain[x]) for y in self.constraints ]) ]
                    solution = self.search(nDomain)
                    if solution != None:
                        return solution
        return None
