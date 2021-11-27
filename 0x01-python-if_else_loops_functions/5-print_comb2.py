#!/usr/bin/python3
comma = ", "
for i in range(0, 101):
    if i == 100:
        comma= ""
    print("{:02d}".format(i),end=comma)
print(" ")
