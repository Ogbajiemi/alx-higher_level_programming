#!/usr/bin/python3

def uppercase(str):
    for r in range(len(str)):
        var = ord(str[r])
        if var >= 97 and var <= 122:
            var = var - 32
        print("{}".format(chr(var)), end="")
    print()
