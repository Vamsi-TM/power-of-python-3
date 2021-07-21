# Dictionaries in python are key value pairs

my_favourites = {'food': 'pizza', 'car': 'BMW'}
print(my_favourites['food'].title())

my_favs = {
    'Name': 'Vamsi',
    'Age': '40',
    'Sex': 'male',
    'City': 'London',
}
print(my_favs)

for k, v in my_favs.items():
    print("\nKey: " + k)
    print("Value: " + v)
