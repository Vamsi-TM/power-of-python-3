# This is an example for user input

while True:
    city = input("Enter the city you love to visit.")
    if city == 'quit':
        break
    else:
        print("I would love to go to " + city.title() + "!")
