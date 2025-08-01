# Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number.

n=int(input("Enter the number: "))

list=[print(f"{n} X {i} = {n*i}") for i in range(11) ]
