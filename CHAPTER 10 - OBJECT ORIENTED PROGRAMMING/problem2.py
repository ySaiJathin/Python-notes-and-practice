# Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class calculator:
    def __init__(self,n):
        self.n=n
        

    def square(self):
        if self.n>=0:
            return (self.n**2)
        
    def cube(self):
        if self.n>=0:
            return (self.n**3)
    
    def square_root(self):
        return (self.n**0.5)

n=int(input("Enter the number: "))
h=input("Enter the operation you need: ").lower()

cal=calculator(n)
if h=="square":
    print(cal.square())
elif h=="cube":
    print(cal.cube())
elif h=='root':
    print(cal.square_root())
else:
    print("Enter a valid operation")

print("End of the program")





