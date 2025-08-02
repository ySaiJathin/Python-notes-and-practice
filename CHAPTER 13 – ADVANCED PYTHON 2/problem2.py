# Write a program to input name, marks and phone number of a student and format it 
# using the format function like below: 
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name=input("Enter the name: ")
marks=int(input("Enter the marks: "))
p_number=input("Enter the phone number of the student: ")
s="The name of the student is {0}, his marks are {1} and phone number is {2}".format(name,marks,p_number)

print(s)

