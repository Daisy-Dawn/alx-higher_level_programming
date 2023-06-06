#!/usr/bin/python3

for num in range(0, 10):
    for number in range(num+1,10):
        print("{:d}{:d}".format(num, number), end="")
        if num != 8 or number != 9:
            print(", ", end="")
print()
