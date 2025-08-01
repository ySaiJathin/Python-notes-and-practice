# Write a program to find out whether a given post is talking about “Harry” or not.

word="harry" 

text=input("Enter the post: ").lower()

if word in text:
    print("Yes, the post is talking about harry")
else:
    print("No, it is now talking about harry")

