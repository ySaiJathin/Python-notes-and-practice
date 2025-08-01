# Write a python function which converts inches to cms.

inches=float(input("Enter the measurement:"))

def convert(inches):
    cm=inches*2.54
    return (f"The convertion of {inches} inches is {cm:.2f} cms")

print(convert(inches))