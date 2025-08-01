# Write a program to print multiplication table of a given number using for loop. 

ie=int(input("Enter the number: "))

for i in range(1,11):
    print(f"{ie} X {i} = {ie*i}")
    i +=1
