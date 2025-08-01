#  Write a program to calculate the factorial of a given number using for loop.

n=int(input("Enter the number: "))

end=1
for i in range(1,n+1):
    end*=i
    i+=1

print(end)
