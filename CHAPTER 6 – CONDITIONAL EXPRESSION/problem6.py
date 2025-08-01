#  Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F

m=int(input("Enter the marks of the student: "))

if 90<m<=100:
    print("EX")
elif 80<m<=90:
    print('A')
elif 70<m<=80:
    print("B")
elif 60<m<=70:
    print("C")
elif 50<m<=60:
    print("D")
elif m<=50:
    print("F")
