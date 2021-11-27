#!/usr/bin/python3
comma = ", "
for i in range(1, 100):
    if i == 99:
        comma= ""
    print("{:02d}".format(i),end=comma)
print(" ")
