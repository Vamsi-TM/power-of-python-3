# This is an example to input the values from the command prompt.

dataType = int(input("Hello there, what would you like to enter?\n"))

if isinstance(dataType, int):
    print("You entered an integer.")
else:
    print("this is not an int")
