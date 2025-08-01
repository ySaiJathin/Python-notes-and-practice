# Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

eng_hindi={
    "bro":"bhai",
    "how are u":"tum kese ho",
    "name":"naam",
    "rose":"gulab"

}

inputn=input()
print(eng_hindi.get(inputn))