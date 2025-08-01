# Write a recursive function to calculate the sum of first n natural numbers.

n=int(input("Enter the number:"))

def cal_sum(n):
    if n==1 :
        return 1
    return n+(cal_sum(n-1))

print(cal_sum(n))