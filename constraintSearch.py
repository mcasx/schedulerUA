def ConstraintSearch:
    def __init__(self,domain,constraints):
        #Domain is a dictionary with var as key and a list of values as value
        self.domain = domain
        #Constraints is a list of functions which require domain as the argument
        self.constraints = constraints

    def search(self):
        #Returns none if there is no solution
        if any([ domain[key] == [] for key in domain.keys()]):
            return None
        pass
