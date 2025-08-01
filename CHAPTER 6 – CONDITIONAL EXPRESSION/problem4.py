# Write a program to find whether a given username contains less than 10 
# characters or not. 

name=input("Enter your username:")
if len(name)<=10:
    print("Valid username")
elif len(name)>10:
    print("Invalid username")
    