# This is to test the conditions in python
#  Demo for if and elsif

number = int(input("Please enter a number to check\n"))
if number <100:
    print("the number is less that 100")
elif number == 100:
    print("the number is equal to 100")
else:
    print("number is more than 100\n")

# this part
city = ['Tokyo', 'New York', 'Toronto', 'Hong Kong']
for name in city:
    print('City: ' + name)

print('\n')  # newline

num = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))
