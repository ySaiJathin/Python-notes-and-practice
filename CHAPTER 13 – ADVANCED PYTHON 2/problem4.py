# . Write a program to filter a list of numbers which are divisible by 5.

def div(i):
        if i%5==0:
            return True
        return False
        
l=[5,67,345,56,34,265,754,5753]
s=list(filter(div,l))
print(s)