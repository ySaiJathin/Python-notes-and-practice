# Check that a tuple type cannot be changed in python.

tuple_example=(4,5,'fhsdf',845)
print(type(tuple_example))
a=tuple_example[2]
print(type(a))