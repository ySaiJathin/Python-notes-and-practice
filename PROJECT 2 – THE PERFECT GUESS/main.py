import random

n=random.randint(1,100)


a=-1
guesses=0
while a!=n:
    guesses+=1
    a=int(input("Guess the number in the range of 1 to 100: "))
    if a<n:
        print("Guess higher")
    elif a>n:
        print("Guess lower")
    else:
        print("You have guessed correctly!")

print(f"You have guesssed the {n} in {guesses} attempts!")