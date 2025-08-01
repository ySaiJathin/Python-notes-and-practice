# Write a program to detect double space in a string. 

s=input()
s2=s.replace("  ", " ")
if "  " in s:
    print("Double space found")
else:
    print("No double space found")


print(s2)