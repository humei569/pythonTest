import math
import os
from os import write

print(78542)

year = 2021
event = "Hackathon"

print("{} {}".format(year, event))
print(f"{year} {event} time is end")

print(f'The value of pi is approximately {math.pi:.3f}.')

# write(99999, 111)

for i in range(0, 11):
    print(repr(i).rjust(2), repr(i*i). rjust(i*i), end = '  ')
    print(repr(i * i * i).rjust(i*i))


num = '66'
num2 = '-0.99'
print(num.zfill(2), num2.zfill(20))

# file = open('input.txt', 'w', encoding='utf-8')
# file.write("test input content")
# file.close()

if os.path.exists('input.txt'):
    file = open('input.txt', 'r+', encoding='utf-8')
    # print(file.read())
    # file.write("\nappend new content")
    file.close()

with open('input.txt', 'r', encoding='utf-8') as file:
    # read_data = file.read()
    line_data = file.readlines()
    for line in line_data:
        print(line)
    # print(line_data)
    print(file.tell())
