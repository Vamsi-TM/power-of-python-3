# This is the demo of for loop

years = [1990,92,93,94,96]
for x in years:
    print(int(x))

y = 1
while y < 100:
    print(y)
    y = y + 1

# Lists the countries using a while loop

simpleList = ['one', 'two', 'three']
while simpleList:
    print(simpleList.pop(-1))


# Sum using a while loop

number = [12, 13]
while number:
    for x in number:
        print(x)
    number.pop(-1)
#
