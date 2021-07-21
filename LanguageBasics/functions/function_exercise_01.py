# Write a function that accepts a the list of toppings a customer wants on his sandwich

def sandwich_toppings(*my_toppings):
    """These are going to be the toppings on your sandwich"""
    print('\n Making sandwich with the following toppings:')
    for topping in my_toppings:
        print("-" + topping)
