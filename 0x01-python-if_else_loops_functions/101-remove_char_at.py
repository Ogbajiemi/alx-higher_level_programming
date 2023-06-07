#!/usr/bin/python3
def remove_char_at(str, p):

    newStr = ""
    for k in range(len(str)):
        if k == p:
            continue
        else:
            newStr += str[k]
    return newStr
