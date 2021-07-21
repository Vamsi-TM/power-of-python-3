# This is going to be an example for functions in python

def build_person(first_name, last_name):
    """Return a dictionary information about a person."""
    person = {'first': first_name, 'last': last_name}
    print("The person you just added")
    return person


musician = build_person('Jimmy', 'Choo')
print(musician)
