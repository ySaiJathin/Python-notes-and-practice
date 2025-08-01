#  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

sub1=int(input("Enter the first subject marks:"))
sub2=int(input("Enter the second subject marks:"))
sub3=int(input("Enter the third subject marks:"))

if sub1/100<=0.33:
    print("student failec in sub1")
elif sub2/100<=0.33:
    print("student failed in sub2")
elif sub3/100<=0.33:
    print("student failed in sub3")
elif (100*(sub1+sub2+sub3))/300<=40:
    print("student failed by total marks alloted")
else:
    print("student passed ")