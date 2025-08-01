class addition:
    def __init__(self, n):
        self.n=n
    def __mul__(self,num): #this is a dunder method which uses the double underscore to store the numbers 
        # and it can to any function as long as the dunder is initialized 
        return self.n-num.n
n=addition(1)
m=addition(2)
    # as u can see in the return statement it is n-num and in the print is the n+m but it still prints
    # the sub operation which is given in the dunder method return statement
print(n+m)