# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# user. 

import random

youstr=input("Enter your choice:")
computer_input=random.choice([-1,0,1])
youdict={'s':1,"w":0,"g":-1}
you= youdict[youstr]
reversedict={
    1:"snake",
    0:"water",
    -1:"gun"
}
print(f" you chose {reversedict[you]} \n The computer chose {reversedict[computer_input]}")


if you==computer_input:
    print("Its a Draw!")


elif you==1 and computer_input==0:
    print("You win!")
elif you==1 and computer_input==-1:
    print("You lose!")


elif you==0 and computer_input==-1:
    print("You win!")
elif you==0 and computer_input==1:
    print("You lose!")


elif you==-1 and computer_input==1:
    print("You win!")
elif you==-1 and computer_input==0:
    print("You lose!")


else:
    print("Something went wrong")







