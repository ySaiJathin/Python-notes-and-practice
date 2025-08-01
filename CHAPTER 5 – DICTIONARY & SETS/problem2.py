# Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
i1=int(input())
i2=int(input())
i3=int(input())
i4=int(input())
i5=int(input())
i6=int(input())
i7=int(input())
i8=int(input())


s=set()
s.add(i1)
s.add(i2)
s.add(i3)
s.add(i4)
s.add(i5)
s.add(i6)
s.add(i7)
s.add(i8)
print(s)
print(type(s))