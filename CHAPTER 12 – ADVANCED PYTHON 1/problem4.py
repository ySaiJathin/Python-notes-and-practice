#  Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’. 


a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
try:
    print(a/b)

except ZeroDivisionError as e:
    e="infinite"

    print(e)
