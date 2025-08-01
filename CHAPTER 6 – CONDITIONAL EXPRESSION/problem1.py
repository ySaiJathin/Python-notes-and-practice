#  Write a program to find the greatest of four numbers entered by the user. 

a=input("Enter the first num:")
b=input("Enter the second num:")
c=input("Enter the third num:")
d=input("Enter the fourth num:")

if a==b or a==c or a==d or b==c or b==d or c==d:
    print("please enter unique nums")
elif a>b and a>c and a>d:
    print("A is greater")
elif b>a and b>c and b>d:
    print("B is greater")
elif c>a and c>b and c>d:
    print("C is greater")
elif d>a and d>b and d>c:
    print("D is greater")
