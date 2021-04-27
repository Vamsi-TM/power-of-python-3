# This is a demo to read a file

filename = "text.txt"

with open(filename) as file:
    content = file.readlines()
    print(content)

destination = "summer holiday at beach"
mySlice = destination[0:6]
print(mySlice)

import time

timenow = time.localtime(time.time())
# print(timenow)

timeIs = time.asctime()
print(timeIs)

timeIs = time.ctime()
print(timeIs)

try:
    open("tet.txt")
except:
    print("File not found")
