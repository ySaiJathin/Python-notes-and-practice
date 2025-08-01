# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

# no it doesnt change the class attribute but what it does is to call the instance attribute
# let's see what it does

class att:
    attribute=7

n=att()
n.attribute=0
print(n.attribute)
