# Write a python function to remove a given word from a list ad strip it at the same time. 

l=["hi", "wow"," jathin", 'yo']

i=int(input("Enter the index of the word: "))
def strit(l,i):
    l.remove([i])

    l.strip([i])
    return l

print(strit(l,i))