# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals():
    def __init__(self,sounds):
        self.sounds=sounds

class Pets(Animals):
    def __init__(self,sounds,legs):
        super().__init__(sounds)
        self.legs=legs
class dog(Pets):
    def __init__(self,sounds,legs):
        super().__init__(sounds,legs)

    def display(self):
        print(f"The sound the dog makes is {self.sounds} and it has {self.legs} legs.")

a=dog("Bow Bow!",4)
a.display()