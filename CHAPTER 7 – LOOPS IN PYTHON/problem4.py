# Write a program to find whether a given number is prime or not.

n=int(input("Enter the number: "))

# for i in range(2,(int(n**0.5)+1)):
#     if n%i==0:
#         print("the number is not a prime number ")
#     else:
#         print("The number is a prime number")  this is the most efficient way to do so#


for i in range(2,n):
    if n%i==0:
        print("this is not a prime number")
        break
else:
    print("This is a prime number")

    
    