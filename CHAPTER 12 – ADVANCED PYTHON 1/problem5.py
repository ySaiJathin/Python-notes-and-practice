#  Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

n=int(input("Enter the number: "))


[open("tables.txt", "a").write(f"{n} x {i} = {n * i}\n") for i in range(1, 11)]

