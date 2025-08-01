
# Add a static method in problem 2, to greet the user with hello.


class calculator:
    def __init__(self,n):
        self.n=n
    @staticmethod
    def greet():
        print("Hello")
        

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
calculator.greet()

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





