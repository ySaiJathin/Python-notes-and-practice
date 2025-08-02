# . Write a program to find the maximum of the numbers in a list using the reduce 
# function.

from functools import reduce
l=[5,67,345,56,34,265,754,5753]

def greater(a,b):
    if a>b:
        return a
    return b


print(reduce(greater,l))


