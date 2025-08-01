#  Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 


class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector the 2-D vector is {self.i}i + {self.j}j")
    

class threeDVector(twoDvector,):
    def __init__(self,i,j,k):
        super()
        twoDvector.__init__(self,i,j)
        self.k=k
    def show(self):
        print(f"The vector the 3-D vector is {self.i}i + {self.j}j+{self.k}k")

a=twoDvector(1,2)
a.show()
b=threeDVector(4,5,6)
b.show()