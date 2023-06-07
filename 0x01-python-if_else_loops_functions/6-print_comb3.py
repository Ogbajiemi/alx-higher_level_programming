#!/usr/bin/python3

for k in range(0, 10):
    for p in range(1, 10):
        if k >= p:
            continue
        elif k == 8 and p == 9:
            print("{}{}".format(k, p))
        else:
            print("{}{}, ".format(k, p), end="")
