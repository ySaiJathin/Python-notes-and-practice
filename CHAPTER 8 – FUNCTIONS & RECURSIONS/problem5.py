#  Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

n=int(input("Enter the number: "))

def pattern(n):
    while n>=1:
        print("*"*n)
        n-=1

pattern(n)