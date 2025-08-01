# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

i=input()

f=open("Hi-score.txt")
high=f.read()
if high<int(i):
    f.truncate()
    f.write(i)
else:
    print("You need to have a high score")


print(f.read())
    

    


