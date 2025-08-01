# Write a program to accept marks of 6 students and display them in a sorted 
# manner. 

m1=int(input("enter the marks: "))
m2=int(input("enter the marks: "))
m3=int(input("enter the marks: "))
m4=int(input("enter the marks: "))
m5=int(input("enter the marks: "))
m6=int(input("enter the marks: "))


marks_list=[]
marks_list.append(m1)
marks_list.append(m2)
marks_list.append(m3)
marks_list.append(m4)
marks_list.append(m5)
marks_list.append(m6)

marks_list.sort()
print(marks_list)
