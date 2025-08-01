# Write a python program using function to convert Celsius to Fahrenheit. 

c=int(input("Enter the temperature: "))

def temp_cal(c):
    f=(c*9/5)+32
    return (f"The temperature in {c} C is equal to {f} F ")

print(temp_cal(c))
