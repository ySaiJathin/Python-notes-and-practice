#  Write a program using functions to find greatest of three numbers. 

def greatest(a,b,c):
    if a>b and a>c :
        print("A is the greatest")
    elif b>a and b>c:
        print("B is the greatest")
    elif c>a and c>b:
        print("C is the greatest")
    elif a==b or b==c or c==a:
        print("Please enter distinct numbers")

a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
greatest(a,b,c)